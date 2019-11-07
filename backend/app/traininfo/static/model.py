
from ...basemodel import mq_to_sql

def interface_train_static_info(trainName,isGetAll):
    """训练的静态信息"""

    topic = "trainStaticInfoDict"
    tablename = "trainStaticInfoTable"

    trainStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return trainStaticInfoDict
