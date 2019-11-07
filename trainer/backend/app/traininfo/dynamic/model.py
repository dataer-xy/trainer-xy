

from ...basemodel import mq_to_sql


def interface_train_dynamic_info(trainName,isGetAll):
    """ 训练的动态信息 """
    topic = "trainIterInfoDict"
    tablename = "trainIterInfoTable"

    trainDynamicInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return trainDynamicInfoDict
