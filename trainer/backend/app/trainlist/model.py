
from ....core.msmg import MessageManager
import pandas as pd 

def interface_get_all_trainer():
    """ 获取所有 trainer 名称 
    """

    msMg = MessageManager()

    topic = "trainListStaticInfo"

    trainListStaticInfoDictList = msMg.pull_deplete(topic=topic) # list(dict)
    trainListStaticInfoTable = pd.DataFrame(trainListStaticInfoDictList)

    # output : {trainName:projectName,...}
    projectNameList = trainListStaticInfoTable.to_dict()
    
    return projectNameList