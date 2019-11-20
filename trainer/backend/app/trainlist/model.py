
import pandas as pd 
from ....core.msmg import MessageManager
from ....utils.linksqlUtils import link_mysql_ifnotexit_creat
from ....utils.linksqlUtils import create_engine_mysql
from ....utils.pandasUtils import _my_dataframe_to_sql

# 私有的函数
def _df_to_dict(trainListStaticInfoTable):
    trainListStaticInfoTable.index = trainListStaticInfoTable["trainName"]
    return trainListStaticInfoTable["projectName"].to_dict()


def interface_get_all_trainer():
    """ 获取所有 trainer 名称 
    """

    msMg = MessageManager()

    topic = "trainListStaticInfo"

    trainListStaticInfoDictList = msMg.pull_deplete(topic=topic) # list(dict)
    trainListStaticInfoTable = pd.DataFrame(trainListStaticInfoDictList) # projectName trainName

    database = "trainmeta"
    tablename = "trainListStaticInfoTable"
    con = link_mysql_ifnotexit_creat(database)
    engine = create_engine_mysql(database)
    

    if len(trainListStaticInfoTable) > 0:
        _my_dataframe_to_sql(trainListStaticInfoTable,tablename,con=con,engine=engine,if_exists="append")

    querySql = "select * from {tablename}".format(tablename=tablename)
    trainListStaticInfoTable = pd.read_sql(querySql,con=engine)


    # output : {trainName:projectName,...}
    projectNameList = _df_to_dict(trainListStaticInfoTable)
    
    return projectNameList


