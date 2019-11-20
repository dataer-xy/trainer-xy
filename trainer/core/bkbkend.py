"""这个地方放train 函数"""


import os
import time
import tensorflow as tf
import subprocess

from .modelconfig import modelConfig 

from trainer.core import sysinfo

# TODO 添加到 dataset 中，并且去掉 iter 中重复的
def _get_maxIter(dataset):
    """ 获取最大迭代次数
    
    NOTE:
        不足一块的会被当成一块
    """
    span,mod = divmod(dataset.sampleNum,dataset.batchSize) # 取商取余

    if mod > 0:
        return span+1
    else:
        return span

def build_trainer_name(timefloat):
    
    trainName = time.strftime('%Y%m%d%H%M%S',time.localtime(timefloat)) 

    return trainName

def train(lineModel,trainDataSet,validDataSet,msMg,projectName):


    # 创建时间
    startTime = time.time()
    # 创建 trainName
    trainName = build_trainer_name(startTime)

    # 
    epochs = modelConfig.epochs
    step = 0
    nBatch = _get_maxIter(trainDataSet) # 可以分成多少批次

    totalStep = epochs * nBatch

    #
    tf.summary.scalar('loss_op', lineModel.loss_op) # histogram、image...
    tf.summary.scalar("accuracy_op", lineModel.accuracy_op)
    merged_summary_op = tf.summary.merge_all()

    # 没有绑定 trainName 之前 发送到公共队列的信息
    trainListStaticInfo = {
        "projectName": projectName,
        "trainName":trainName,
    }
    msMg.push(trainListStaticInfo,"trainListStaticInfo") 
    
    

    #----------------------------------------------------------------------------
    # 固定消息：
    # 数据集信息1 2 | 1 2  （静态，动态，后端静态，后端动态）
    # 模型信息1 | 1
    # 训练信息1 2 | 1 2
    # 消息队列信息1 | 1
    # 机器信息1 2 | 1 2

    # 绑定 -- 向某个固定的集合/trainer 发送消息
    msMg.band_trainName(trainName)
    
    # 
    trainStaticInfoDict = {
        "projectName": projectName,
        "trainName":trainName,
        "startTime":startTime,
        "totalStep":totalStep,
        "allEpoch":epochs,
        "allBatch":nBatch
    }

    msMg.push(trainStaticInfoDict,"trainStaticInfoDict")

    modelConfigStaticInfoDict = modelConfig.to_dict()
    msMg.push(modelConfigStaticInfoDict,"modelConfigStaticInfoDict")

    tdsStaticInfoDict,_ = trainDataSet.describe()
    vdsStaticInfoDict,_ = validDataSet.describe()

    msMg.push(tdsStaticInfoDict,"tdsStaticInfoDict")
    msMg.push(vdsStaticInfoDict,"vdsStaticInfoDict")


    msmgInfoDict = msMg.describe()
    msMg.push(msmgInfoDict,"msmgInfoDict")

    #----------------------------------------------------------------------------
    # 机器信息

    # Popen对象创建后，主程序不会自动等待子进程完成
    # 什么时间停止子进程？异常时需要主动杀死，因为不会自动关闭
    pyFile = os.path.abspath(sysinfo.__file__)
    cmd = "python {pyFile} \"{trainName}\"".format(pyFile=pyFile,trainName=trainName)
    sysInfoSubprocess = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)


    #----------------------------------------------------------------------------

    tfconfig = tf.ConfigProto(allow_soft_placement=True) # 需要在没有GPU的情况下，转为CPU
    tfconfig.gpu_options.allow_growth = True # 动态申请显存
    # gpu_options.per_process_gpu_memory_fraction = 0.4 # 占用40%显存

    try:
        with tf.Session(config=tfconfig) as sess: # graph=trainGraph, 
            
            init = tf.global_variables_initializer() # 全局变量初始化
            sess.run(init)

            
            #----------------------------------------------------------------------------
            for epoch_i in range(epochs):

                epochState = msMg.pull(topic="epochState") # --> int
                if epochState == 2:
                    # pause 暂停，只能继续消费队列，找到继续/终止命令
                    print("在epoch暂停！")
                    while epochState != 3 or epochState != 0:
                        epochState = msMg.pull(topic="epochState") # --> int
                    
                    # 2 3 6 None
                    if epochState == 0:
                        sysInfoSubprocess.kill()
                        return 0 # TODO 终止
                elif epochState == 0:
                    sysInfoSubprocess.kill()
                    return 0 # TODO 终止
                else:
                    pass    
                
                batch_i = 0
                trainDataSet.shuffle_idxs() # 每迭代一次都要 shuffle idxs
                
                for outputDict in trainDataSet:

                    print("第{i}次...".format(i=step))
                    
                    batchState = msMg.pull(topic="batchState") # --> int
                    if batchState == 4:
                        # pause 暂停，只能继续消费队列，找到继续/终止命令
                        print("在 batch 暂停！")
                        while batchState != 3 or batchState != 0:
                            batchState = msMg.pull(topic="batchState") # --> int
                        
                        # 2 3 6 None
                        if batchState == 0:
                            sysInfoSubprocess.kill()
                            return 0 # TODO 终止
                    elif batchState == 0:
                        sysInfoSubprocess.kill()
                        return 0 # TODO 终止
                    else: # 3 4 5 None
                        pass
                    
                    #----------------------------------------------------------------------------
                    # 训练
                    # NOTE 尽量保持同名
                    
                    feed_dict = {
                        lineModel.x: outputDict["x"], 
                        lineModel.yTrue: outputDict["yTrue"],
                    }

                    if False:
                        # NOTE: 每次都新定义一个
                        runOptions = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE) # 配置运行时需要记录的信息的protocolmessage
                        runMetadata = tf.RunMetadata() # 运行时记录运行信息的protocol message 
                        _, loss, accuracy, summaryStr = sess.run(
                            [
                                lineModel.train_op, 
                                lineModel.loss_op, 
                                lineModel.accuracy_op, 
                                merged_summary_op
                            ], 
                            feed_dict=feed_dict,
                            options=runOptions,
                            run_metadata=runMetadata
                        )
                    else:
                        runMetadata = None
                        _, loss, accuracy, summaryStr = sess.run(
                            [
                                lineModel.train_op, 
                                lineModel.loss_op, 
                                lineModel.accuracy_op, 
                                merged_summary_op
                            ], 
                            feed_dict=feed_dict
                        )


                    # loss 等
                    if step % modelConfig.printStep == 0:

                        #----------------------------------------------------------------------------
                        # 数据集信息

                        dsIterInfoDict = outputDict["_info"]
                        tempDict = {}
                        for _,v in dsIterInfoDict.items():
                            tempDict.update(v)
                        dsIterInfoDict = tempDict 
                        dsIterInfoDict["step"] = step
                        msMg.push(dsIterInfoDict,topic="dsIterInfoDict")


                        #----------------------------------------------------------------------------
                        # 训练信息
                        trainIterInfoDict = {
                            "step":step,
                            "epoch":epoch_i,
                            "batch":batch_i,
                            "loss":loss,
                            "acc":accuracy,
                            "loss_val":None,
                            "acc_val":None
                        }

                        msMg.push(trainIterInfoDict,topic="trainIterInfoDict")


                    # 模型保存 OK
                    if step % modelConfig.modelStepSave == 0:
                        sessInfoDict = {
                            "step":step,
                            "sess":sess
                        }
                        # msMg.push(sessInfoDict,topic="sessInfoDict")
                        # TODO sess 无法序列化 SwigPyObject objects


                    # 模型可视化 OK - tensorboard
                    if step % modelConfig.summaryStepSave == 0:
                        if False: # step == 0:
                            g = sess.graph
                        else:
                            g = None

                        summaryInfoDict = {
                            "step":step,
                            "summaryStr":summaryStr,
                            "runMetadata":runMetadata,
                            "graph":g
                        }

                        msMg.push(summaryInfoDict,topic="summaryInfoDict")
                        # TODO Cannot serialize socket object



                    #----------------------------------------------------------------------------
                    # 验证集

                    if validDataSet is not None:

                        if step % (modelConfig.validStep) == 0:
                            
                            #----------------------------------------------------------------------------
                            # 计算 validation loss

                            validDataSet.batchSize=validDataSet.sampleNum # TODO 但对大数据量不行，不行就不行，内存装不下怎么样也不行

                            for outputDict in validDataSet:
                        
                                feed_dict = {
                                    lineModel.x: outputDict["x"], 
                                    lineModel.yTrue: outputDict["yTrue"],
                                }
                                valid_loss,valid_accuracy = sess.run(
                                    [lineModel.loss_op, lineModel.accuracy_op], 
                                    feed_dict=feed_dict
                                )
                                
                                # break
                            
                            #----------------------------------------------------------------------------
                            # 信息
                            trainIterInfoDict = {
                                "step":step,
                                "epoch":epoch_i,
                                "batch":batch_i,
                                "loss":loss,
                                "acc":accuracy,
                                "loss_val":valid_loss,
                                "acc_val":valid_accuracy
                            }
                    # 
                    time.sleep(1.5)
                    step += 1
                    batch_i += 1
            

    except Exception as e:
        print(e)
        # 
        sysInfoSubprocess.kill() # 在 Windows 上， kill() 是 terminate() 的别名。

        # 清空队列
        msMg.clear_trainName(trainName=trainName)
        msMg.free_trainName()
        raise e


