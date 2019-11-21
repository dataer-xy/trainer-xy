
import numpy as np 
import pandas as pd 

from ...core.msmg import MessageManager
from ...utils.linksqlUtils import link_mysql_ifnotexit_creat
from ...utils.linksqlUtils import create_engine_mysql
from ...utils.pandasUtils import _my_dataframe_to_sql


def my_pandas_to_dict(df,isOnlyOne=True):
    """对大小是1的表是否好用？ 可以，不知道json 的时候会不会有问题？OK"""

    outputDict = {}
    columns = df.columns
    
    if not isOnlyOne:
        for columnsName in columns:
            colList = df[columnsName].tolist()
            outputDict[columnsName] = [None if x!=x else x for x in colList] # np.stack(df[columnsName]) 
    else:
        for columnsName in columns:
            outputDict[columnsName] = df[columnsName].tolist()[0]


    return outputDict




def mq_to_sql(topic,tablename,trainName,isGetAll,isOnlyOne=True):
    """
    isOnlyOne=True 静态的纯字典，否则，动态的字典k-v(str:list)

    Step
        读取 mq
        io mysql
        如果 isGetAll
            读取 mysql 所有数据
        返回数据
    
    """
    if trainName is not None:
        msMg = MessageManager()
        msMg.band_trainName(trainName)

        tdsStaticInfoDictList = msMg.pull_deplete(topic=topic) # list(dict)
        tdsStaticInfoTable = pd.DataFrame(tdsStaticInfoDictList)

        con = link_mysql_ifnotexit_creat(trainName)
        engine = create_engine_mysql(trainName)

        if len(tdsStaticInfoDictList) > 0:
            _my_dataframe_to_sql(tdsStaticInfoTable,tablename,con=con,engine=engine,if_exists="append")


        if isGetAll:
            print("正在加载全部数据！")
            querySql = "select * from {tablename}".format(tablename=tablename)
            tdsStaticInfoTable = pd.read_sql(querySql,con=engine)

        tdsStaticInfoDict = my_pandas_to_dict(tdsStaticInfoTable,isOnlyOne)

        return tdsStaticInfoDict
    else:
        raise Exception("trainName is None")



def message_to_mq(trainName,data,topic):
    """ 消息发送到消息队列 """
    if trainName is not None:
        msMg = MessageManager()
        msMg.band_trainName(trainName)

        msMg.push(data,topic)
    else:
        raise Exception("trainName is None")



def get_modelconfig_from_sql(trainName):
    """ 从 sql 中获取模型配置信息 """
    if trainName is not None:
        tablename = "modelConfigStaticInfoTable"
        querySql = "select * from {tablename}".format(tablename=tablename)
        engine = create_engine_mysql(trainName)
        modelconfigStaticInfoTable = pd.read_sql(querySql,con=engine)

        modelconfigStaticInfoDict = my_pandas_to_dict(modelconfigStaticInfoTable,isOnlyOne=True)
        return modelconfigStaticInfoDict
    else:
        raise Exception("trainName is None")

