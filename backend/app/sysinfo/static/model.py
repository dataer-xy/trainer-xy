
from ...basemodel import mq_to_sql

def interface_sys_static_info(trainName,isGetAll):
    """ 系统静态信息"""
    topic = "sysStaticInfoDict"
    tablename = "sysStaticInfoTable"
    sysStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return sysStaticInfoDict

