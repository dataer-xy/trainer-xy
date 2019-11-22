# 项目结构示例

## tensorflow


### 构建数据集

buildds.py 文件


``` python
import numpy as np 
import pandas as pd

from dataset import DataSet 

def build_dataset():
    
    # 
    nSample = 5000 # 样本数量
    xData = np.random.rand(2, nSample)
    wTrue = [0.100, 0.200]
    bTrue = 0.300
    
    pdf = pd.DataFrame()
    pdf["yTrue"] = np.dot(wTrue, xData) + bTrue
    pdf["x"] = xData.T.tolist()

    # 
    ds = DataSet(pdf)

    # 设置
    ds.batchSize = 64 # 批次大小

    return ds
```


### 构建模型

model.py 文件 

``` python 
import tensorflow as tf
import numpy as np
from .modelconfig import modelConfig

class LineModel(object):
    def __init__(self):

        self.x = tf.placeholder(dtype=tf.float32,shape=[None,2],name="x")
        self.yTrue = tf.placeholder(dtype=tf.float32,shape=[None],name="yTrue")
        # 构造一个线性模型
        b = tf.Variable(tf.zeros([1]),name="bias")
        W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0),name="weight")
        yHat = tf.matmul(W, self.x, transpose_b=True) + b

        # 最小化方差
        self.loss_op = tf.reduce_mean(tf.square(yHat - self.yTrue))
        self.accuracy_op = 1-tf.reduce_sum(tf.square(yHat - self.yTrue)) / modelConfig.deno # 区别于R2，固定值
        optimizer = tf.train.AdadeltaOptimizer(modelConfig.learnRate)
        tf.train
        self.train_op = optimizer.minimize(self.loss_op)


    def try_run(self):
        """ 运行 """
        x = np.random.uniform(size=(63,2))
        yTrue = np.random.uniform(size=(63,))

        with tf.Session() as sess:

            init = tf.global_variables_initializer()
            sess.run(init)

            feed_dict = {
                self.x:x,
                self.yTrue:yTrue
            }

            a,b = sess.run([self.loss_op,self.accuracy_op],feed_dict=feed_dict)
            print(a,b)
```



### 模型的配置文件


modelconfig.py

``` python
import os

from trainer.utils.pathJoinUtils import my_path_join
from trainer.utils.dirFileUtils import mkdir_my

from trainer import ModelConfigBase 

#--------------------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)) # 父级目录

OUTPUT_BASE = my_path_join(BASE_DIR,r"outputs")

checkpointPath = my_path_join(OUTPUT_BASE,r"checkpointPath")
mkdir_my(checkpointPath)

tensorboardLogPath = my_path_join(OUTPUT_BASE,r"tensorboardLogPath")
mkdir_my(tensorboardLogPath)

exportPath = my_path_join(OUTPUT_BASE,r"exportPath") # NOTE: 不能存在
# mkdir_my(exportPath)

historyPath = my_path_join(OUTPUT_BASE,r"historyPath")
mkdir_my(historyPath)



class ModelConfig(ModelConfigBase):
    # NOTE: 注意这里的继承

    def __init__(self):
        self.learnRate = 0.5 # 学习率
        self.deno = 12 # 分母

        # 训练部分
        self.batchSize = 64 # OK

        self.epochs = 100 # epoch 次数 step = epochs*批次数 NOTE: 10 epoch 需要 1/4 天

        self.validFrequency = 2 # ? 个 epoch 验证 1 次

        self.runMetaDataFrequency = None # 多少尺度运行一次 runmetadata

        #---------------------------------------------------
        # 存储

        self.printStep = 20 # OK
        self.validStep = 50

        self.summaryStepSave = 20 # 每 20 step 保存一次 summary
        
        self.modelStepSave = 1000 # 每 1000 step 保存一次 model

        self.hiddenLayerStepSave = 50 # 每 50 step 保存一次 history

        self.checkpointPath = checkpointPath # NOTE: 需要是一个空文件夹。存储保存路径，保存了graph和网络参数值

        self.checkpointModelName = "linemodel"

        self.tensorboardLogPath = tensorboardLogPath # 可视化的保存路径，按epoch记录 # OK

        self.exportPath = exportPath # save_model 保存模型 # OK

        self.historyPath = historyPath # OK
    

modelConfig = ModelConfig()

```


### 训练程序

trains.py

``` python 
import os
import time
import tensorflow as tf
import subprocess

from .modelconfig import modelConfig 

from trainer import run_sysinfo_subprocess
from trainer import is_continue_in_batchState
from trainer import is_continue_in_epochState


def build_trainer_name(timefloat):
    """要能够排列大小"""
    
    trainName = time.strftime('%Y%m%d%H%M%S',time.localtime(timefloat)) 

    return trainName


def train(lineModel,trainDataSet,validDataSet,msMg,projectName):


    # 创建时间
    startTime = time.time()
    # 创建 trainName
    trainName = build_trainer_name(startTime)


    #----------------------------------------------------------------------------
    # 没有绑定 trainName 之前，发送到公共队列的信息

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
    epochs = modelConfig.epochs 
    nBatch = trainDataSet.nBatch # 可以分成多少批次 
    totalStep = epochs * nBatch
    step = 0  

    trainStaticInfoDict = {
        "projectName":projectName,
        "trainName":trainName,
        "startTime":startTime,
        "totalStep":totalStep,
        "allEpoch":epochs,
        "allBatch":nBatch
    }

    msMg.push(trainStaticInfoDict,"trainStaticInfoDict")

    #
    modelConfigStaticInfoDict = modelConfig.to_dict()
    msMg.push(modelConfigStaticInfoDict,"modelConfigStaticInfoDict")

    # 
    tdsStaticInfoDict,_ = trainDataSet.describe()
    msMg.push(tdsStaticInfoDict,"tdsStaticInfoDict")
    if validDataSet is not None:
        vdsStaticInfoDict,_ = validDataSet.describe()
        msMg.push(vdsStaticInfoDict,"vdsStaticInfoDict")


    msmgInfoDict = msMg.describe()
    msMg.push(msmgInfoDict,"msmgInfoDict")

    #----------------------------------------------------------------------------
    # 机器信息

    sysInfoSubprocess = run_sysinfo_subprocess(trainName)


    #----------------------------------------------------------------------------

    #
    tf.summary.scalar('loss_op', lineModel.loss_op) # histogram、image...
    tf.summary.scalar("accuracy_op", lineModel.accuracy_op)
    merged_summary_op = tf.summary.merge_all()

    saver = tf.train.Saver(max_to_keep=4) 

    summaryWriter = tf.summary.FileWriter(modelConfig.tensorboardLogPath)

    tfconfig = tf.ConfigProto(allow_soft_placement=True) # 需要在没有GPU的情况下，转为CPU
    tfconfig.gpu_options.allow_growth = True # 动态申请显存
    # gpu_options.per_process_gpu_memory_fraction = 0.4 # 占用40%显存

    try:
        with tf.Session(config=tfconfig) as sess: # graph=trainGraph, 
            
            init = tf.global_variables_initializer() # 全局变量初始化
            sess.run(init)

            summaryWriter.add_graph(sess.graph)

            #----------------------------------------------------------------------------
            for epoch_i in range(epochs):
  
                if not is_continue_in_epochState(msMg):
                    sysInfoSubprocess.kill()
                    return 0

                batch_i = 0
                trainDataSet.shuffle_idxs() # 每迭代一次都要 shuffle idxs
                
                for outputDict in trainDataSet:

                    print("第{i}次...".format(i=step))
                    
                    if not is_continue_in_batchState(msMg):
                        sysInfoSubprocess.kill()
                        return 0
                    
                    #----------------------------------------------------------------------------
                    # 训练 NOTE 尽量保持同名
                    
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
                        summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)
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

                    # 模型保存
                    if step % modelConfig.modelStepSave == 0:
                        saver.save(
                            sess, 
                            os.path.join(modelConfig.checkpointPath,modelConfig.checkpointModelName), 
                            global_step=step
                        )

                    # 模型可视化 - tensorboard
                    if step % modelConfig.summaryStepSave == 0:


                        summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str
                        

                    #----------------------------------------------------------------------------
                    # 验证集

                    if validDataSet is not None:

                        if step % (modelConfig.validStep) == 0:
                            
                            #----------------------------------------------------------------------------
                            # 计算 validation loss

                            validDataSet.batchSize=validDataSet.sampleNum # TODO 但对大数据量不行，不行就不行，内存装不下怎么样也不行。keras 是如何做到迭代验证的？

                            for outputDict in validDataSet:
                        
                                feed_dict = {
                                    lineModel.x: outputDict["x"], 
                                    lineModel.yTrue: outputDict["yTrue"],
                                }
                                valid_loss,valid_accuracy = sess.run(
                                    [lineModel.loss_op, lineModel.accuracy_op], 
                                    feed_dict=feed_dict
                                )
                            
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

                            msMg.push(trainIterInfoDict,topic="trainIterInfoDict")

                    # 
                    time.sleep(1)
                    step += 1
                    batch_i += 1       
    except Exception as e:
        # 清空队列
        msMg.clear_trainName(trainName=trainName)
        msMg.free_trainName()
        raise e
    finally:
        sysInfoSubprocess.kill() # 在 Windows 上， kill() 是 terminate() 的别名。


```


### main

main.py


``` python 
from trainer import MessageManager
msMg = MessageManager()

from .modelconfig import modelConfig 

from .buildds import build_dataset

ds = build_dataset()
ds.batchSize = modelConfig.batchSize

trainDataSet,validDataSet,testDataSet = ds.split_dataset(strategyValidate=2)

from .model import LineModel
lineModel = LineModel()

from .trains import train


projectName = "testProj" # NOTE 这里要标记 trainer 的项目名称
train(lineModel,trainDataSet,validDataSet,msMg,projectName)

```


