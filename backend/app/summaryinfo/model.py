
import tensorflow as tf 
import os
from ....msmg import MessageManager

tensorboardLogPath = None

def interface_save_summary(trainName):
    
   
    msMg = MessageManager()
    msMg.band_projectName(trainName)

    summaryInfoDictList = msMg.pull(topic="summaryInfoDict")

    for summaryInfo in summaryInfoDictList:
        summaryWriter = tf.summary.FileWriter(tensorboardLogPath) # 实例化一个FileWriter的类对象，并将当前TensoirFlow的计算图写入【日志文件】

        step = summaryInfo["step"]
        summaryStr = summaryInfo["summaryStr"]
        runMetadata = summaryInfo["runMetadata"]
        graph = summaryInfo["graph"]

        summaryWriter.add_graph(graph)

        summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)

        summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str


