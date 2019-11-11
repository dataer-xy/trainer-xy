
from ....core.msmg import MessageManager


def interface_get_all_trainer():
    """ 获取所有 trainer 名称 
    TODO：bug
    
    """

    msMg = MessageManager()

    queueNameList = msMg.list_queues()

    projectNameList = [] # --> list(str)
    
    for queueName in queueNameList:
        tempProjectName = queueName.split("_")[0]
        if tempProjectName not in projectNameList:
            projectNameList.append(tempProjectName)
    
    return projectNameList