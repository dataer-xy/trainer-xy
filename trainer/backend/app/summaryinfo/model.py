
import tensorflow as tf 
import os
from ....core.msmg import MessageManager

from ..basemodel import get_modelconfig_from_sql

def interface_summary_dynamic_info(trainName,isGetAll):
    """ 保存 summary 信息 """

    # 
    msMg = MessageManager()
    msMg.band_trainName(trainName)

    summaryInfoDictList = msMg.pull_deplete(topic="summaryInfoDict")

    # 
    modelConfig = get_modelconfig_from_sql(trainName)

    for summaryInfo in summaryInfoDictList:
        summaryWriter = tf.summary.FileWriter(modelConfig["tensorboardLogPath"]) # 实例化一个FileWriter的类对象，并将当前TensoirFlow的计算图写入【日志文件】

        step = summaryInfo["step"]
        summaryStr = summaryInfo["summaryStr"]
        runMetadata = summaryInfo["runMetadata"]
        graph = summaryInfo["graph"]
        
        if graph is not None:
            summaryWriter.add_graph(graph)
        if runMetadata is not None:
            summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)

        summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str


