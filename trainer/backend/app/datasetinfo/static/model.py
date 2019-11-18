
from ...basemodel import mq_to_sql

# 训练数据集信息
def interface_traindataset_static_info(trainName,isGetAll):
    """ 训练数据集信息

    """
    topic = "tdsStaticInfoDict"
    tablename = "tdsStaticInfoTable"
    tdsStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)
    return tdsStaticInfoDict


# 测试数据集信息
def interface_validdataset_static_info(trainName,isGetAll):
    """ 测试数据集信息
    """
    topic = "vdsStaticInfoDict"
    tablename = "vdsStaticInfoTable"  
    vdsStaticInfoDict = mq_to_sql(topic,tablename,trainName,isGetAll)

    return vdsStaticInfoDict



def interface_dataset_static_info(trainName,isGetAll):
    tdsStaticInfoDict = interface_traindataset_static_info(trainName,isGetAll)
    vdsStaticInfoDict = interface_validdataset_static_info(trainName,isGetAll)

    dsStaticInfoDict = {
        "tdsStaticInfoDict":tdsStaticInfoDict,
        "vdsStaticInfoDict":vdsStaticInfoDict
    }

    return dsStaticInfoDict
