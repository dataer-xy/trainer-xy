import tensorflow as tf 
import os
from .msmg import MessageManager

checkpointPath = None
checkpointModelName = None

def save_sess():
    
   
    msMg = MessageManager()

    sessInfo = msMg.pull("sessInfo")

    if sessInfo is not None:
        sess = sessInfo["sess"]
        step = sessInfo["step"]
        saver = tf.train.Saver(max_to_keep=4) 

        saver.save(
            sess, 
            os.path.join(checkpointPath,checkpointModelName), 
            global_step=step
        )

