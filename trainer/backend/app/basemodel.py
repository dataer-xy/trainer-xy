
import pandas as pd 

from ...core.msmg import MessageManager
from myutils.linksqlUtils import link_mysql_ifnotexit_creat
from myutils.linksqlUtils import create_engine_mysql
from myutils.pandasUtils import _my_dataframe_to_sql


def mq_to_sql(topic,tablename,trainName,isGetAll):
    """
    
    Step
        读取 mq
        io mysql
        如果 isGetAll
            读取 mysql 所有数据
        返回数据
    
    """

    msMg = MessageManager()
    msMg.band_trainName(trainName)

    tdsStaticInfoDictList = msMg.pull_deplete(topic=topic) # list(dict)
    tdsStaticInfoTable = pd.DataFrame(tdsStaticInfoDictList)

    if len(tdsStaticInfoDictList) > 0:
        con = link_mysql_ifnotexit_creat(trainName)
        engine = create_engine_mysql(trainName)
        _my_dataframe_to_sql(tdsStaticInfoTable,tablename,con=con,engine=engine,if_exists="append")


    if isGetAll:
        querySql = "select * from {tablename}".format(tablename=tablename)
        tdsStaticInfoTable = pd.read_sql(querySql,con=engine)

    tdsStaticInfoDict = tdsStaticInfoTable.to_dict() # TODO if none return none

    return tdsStaticInfoDict



def message_to_mq(trainName,data,topic):
    """ 消息发送到消息队列 """

    msMg = MessageManager()
    msMg.band_trainName(trainName)

    msMg.push(data,topic)



def get_modelconfig_from_sql(trainName):
    """ 从 sql 中获取模型配置信息 """
    tablename = "modelConfigStaticInfoTable"
    querySql = "select * from {tablename}".format(tablename=tablename)
    modelconfigStaticInfoTable = pd.read_sql(querySql,con=engine)

    modelconfigStaticInfoDict = modelconfigStaticInfoTable.to_dict()
    return modelconfigStaticInfoDict

