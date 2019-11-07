

from ...basemodel import mq_to_sql

def interface_sys_dynamic_info(trainName,isGetAll):
    """系统动态信息"""

    topic = "sysIterInfoDict"
    tablename = "sysIterInfoTable"

    sysDynamicInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return sysDynamicInfoDict

