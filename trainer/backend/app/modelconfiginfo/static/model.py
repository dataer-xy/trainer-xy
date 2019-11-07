
from ...basemodel import mq_to_sql

def interface_modelconfig_static_info(trainName,isGetAll):
    """模型配置静态信息"""
    topic = "modelConfigStaticInfoDict"
    tablename = "modelConfigStaticInfoTable"
    modelconfigStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)
    return modelconfigStaticInfoDict
