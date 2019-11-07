import tensorflow as tf 
import os
from ....msmg import MessageManager

checkpointPath = None
checkpointModelName = None

def interface_save_sess(trainName):
    
   
    msMg = MessageManager()
    msMg.band_projectName(trainName)

    sessInfoDictList = msMg.pull_deplete("sessInfoDict")

    for sessInfo in sessInfoDictList:
        sess = sessInfo["sess"]
        step = sessInfo["step"]
        saver = tf.train.Saver(max_to_keep=4) 

        saver.save(
            sess, 
            os.path.join(checkpointPath,checkpointModelName), 
            global_step=step
        )

