from ...basemodel import mq_to_sql

def interface_dataset_dynamic_info(trainName,isGetAll):
    """ 获取数据集的动态信息 
    
    只需要训练集的即可

    Step
        读取 mq
        io mysql
        如果 isGetAll
            读取 mysql 所有数据
        返回数据
    """
    topic = "dsIterInfoDict"
    tablename = "dsIterInfoTable"
    isOnlyOne=False
    dsDynamicInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll,isOnlyOne)

    return dsDynamicInfoDict

