
from ....core.msmg import MessageManager


def interface_get_all_trainer():
    """ 获取所有 trainer 名称 
    TODO：bug
    
    """

    msMg = MessageManager()

    queueNameList = msMg.list_queues()

    projectNameList = [] # --> list(str)
    
    for queueName in queueNameList:
        tempProjectName = queueName.split("_")[0] # TODO 需要判断是否是日期数字，因为可能有其他队列存在
        if tempProjectName not in projectNameList:
            projectNameList.append(tempProjectName)
    
    return projectNameList