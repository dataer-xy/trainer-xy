import pandas as pd 

from .msmg import MessageManager


def interface_dataset_static_info(isGetAll):
    """
    
    Step
        读取 mq
        io mysql
        如果 isGetAll
            读取 mysql 所有数据
        返回数据
    
    """
    
    msMg = MessageManager()

    tdsStaticInfoDict = msMg.pull(topic="tdsStaticInfoDict") # list(dict) / None

    if tdsStaticInfoDict is not None:
        tdsStaticInfoTable = pd.DataFrame(tdsStaticInfoDict)
    
        engine = None
        tablename = "tdsStaticInfoTable"
        tdsStaticInfoTable.to_sql(tablename,con=engine)

    if isGetAll:
        querySql = "select * from {tablename}".format(tablename=tablename)
        tdsStaticInfoTable = pd.read_sql(querySql,con=engine)

        tdsStaticInfoDict = tdsStaticInfoTable.to_dict()

    return tdsStaticInfoDict