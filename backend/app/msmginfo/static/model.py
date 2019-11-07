

from ...basemodel import mq_to_sql

def interface_msmg_static_info(trainName,isGetAll):
    """ 消息队列静态信息
    """
    topic = "msmgInfoDict"
    tablename = "msmgInfoTable"
    msmgStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return msmgStaticInfoDict