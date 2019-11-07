import tensorflow as tf 
import os
from ....core.msmg import MessageManager

from ..basemodel import get_modelconfig_from_sql


def interface_sess_dynamic_info(trainName,isGetAll=False):
    """保存 sess"""
    
    # 
    msMg = MessageManager()
    msMg.band_projectName(trainName)

    sessInfoDictList = msMg.pull_deplete("sessInfoDict")

    # 
    modelConfig = get_modelconfig_from_sql(trainName)


    for sessInfo in sessInfoDictList:
        sess = sessInfo["sess"]
        step = sessInfo["step"]
        saver = tf.train.Saver(max_to_keep=4) # TODO 能行嘛？

        saver.save(
            sess, 
            os.path.join(modelConfig["checkpointPath"],modelConfig["checkpointModelName"]), 
            global_step=step
        )

