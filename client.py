
from .modelconfig import modelConfig 

msMg = MessageManager()

from .buildds import build_dataset

ds = build_dataset()
ds.batchSize = 10

trainDataSet,validDataSet,testDataSet = ds.split_dataset(strategyValidate=2)

from .model import LineModel
lineModel = LineModel()


train(lineModel,trainDataSet,validDataSet,msMg) # NOTE 是一个解

import time
import tensorflow as tf

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


def train(lineModel,trainDataSet,validDataSet,msMg):
    epochs = 100
    step = 0
    
    # 创建时间
    startTime = time.time()
    # 创建 trainName
    trainName = str(startTime)

    nBatch = _get_maxIter(trainDataSet)

    totalStep = epochs * epochs

    #
    tf.summary.scalar('loss_op', lineModel.loss_op) # histogram、image...
    tf.summary.scalar("accuracy_op", lineModel.accuracy_op)
    merged_summary_op = tf.summary.merge_all()


    #----固定消息--------------------------------------------
    
    # 
    trainStaticInfoDict = {
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


    # 数据集信息1
    # 模型信息1
    # 训练信息1
    # 消息队列信息
    # 机器信息1

    tfconfig = tf.ConfigProto(allow_soft_placement=True) # 需要在没有GPU的情况下，转为CPU
    tfconfig.gpu_options.allow_growth = True # 动态申请显存
    # gpu_options.per_process_gpu_memory_fraction = 0.4 # 占用40%显存

    with tf.Session(config=tfconfig) as sess: # graph=trainGraph, 
        
        init = tf.global_variables_initializer() # 全局变量初始化
        sess.run(init)

        msMg.push(sess.graph,"graph")
        
        # --------------------------------------------------
        for epoch_i in range(epochs):
            epochState = msMg.pull(topic="epochState") # --> int
            if epochState == 2:
                # pause 暂停，只能继续消费队列，找到继续/终止命令
                while epochState != 3 or epochState != 0:
                    epochState = msMg.pull(topic="epochState") # --> int
                
                # 2 3 6 None
                if epochState == 0:
                    return 0 # TODO 终止
            elif epochState == 0:
                return 0 # TODO 终止
            else:
                pass    
            
            batch_i = 0
            trainDataSet.shuffle_idxs() # 每迭代一次都要 shuffle idxs
            
            for outputDict in trainDataSet:

                batchState = msMg.pull(topic="batchState") # --> int
                if batchState == 4:
                    # pause 暂停，只能继续消费队列，找到继续/终止命令
                    while batchState != 3 or batchState != 0:
                        batchState = msMg.pull(topic="batchState") # --> int
                    
                    # 2 3 6 None
                    if batchState == 0:
                        return 0 # TODO 终止
                elif batchState == 0:
                    return 0 # TODO 终止
                else: # 3 4 5 None
                    pass
                
                #----------------------------------------------------------------------------
                # NOTE 尽量保持同名
                
                feed_dict = {
                    lineModel.x: outputDict["x"], 
                    lineModel.yTrue: outputDict["yTrue"],
                }

                if step % int(modelConfig.runMetaDataFrequency * modelConfig.nSteps) == 0:
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
                    # summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)

                # 数据集信息
                dsIterInfo = outputDict["_info"]
                msMg.push(dsIterInfo,topic="dsIterInfo")

                #----------------------------------------------------------------------------
                # 训练信息

                # 计算平均loss并显示出来
                if step % modelConfig.printStep == 0:
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
                    msMg.push(sess,topic="sess")
                    # saver.save(
                    #     sess, os.path.join(modelConfig.checkpointPath,modelConfig.checkpointModelName), 
                    #     global_step=step
                    # )

                # 模型可视化 OK - tensorboard
                if step % modelConfig.summaryStepSave == 0:
                    msMg.push(summaryStr,topic="summaryStr")
                    # summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str



                #----------------------------------------------------------------------------
                # 验证集
                if validDataSet is not None:

                    if step % int(modelConfig.nSteps / modelConfig.validFrequency) == 0:
                        
                        #----------------------------------------------------------------
                        # 计算 validation loss

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
                        
                        #----------------------------------------------------------------
                        trainIterInfoDict = {
                            "step":step,
                            "epoch":epoch_i,
                            "batch":batch_i,
                            "loss":loss,
                            "acc":accuracy,
                            "loss_val":valid_loss,
                            "acc_val":valid_accuracy
                        }

                step += 1
                batch_i += 1
