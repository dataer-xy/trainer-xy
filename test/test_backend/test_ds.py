
from trainer.core.buildds import build_dataset

from trainer.core.msmg import MessageManager
import pandas as pd 

from myutils.pandasUtils import _my_dataframe_to_sql
from myutils.linksqlUtils import link_mysql_ifnotexit_creat
from myutils.linksqlUtils import create_engine_mysql

def test_funcion_name():
    pass

def test_build_ds():
    

    ds = build_dataset()
    ds.convertFunDict = {
        "xds" : test_funcion_name
    }

    d,s = ds.describe()

    print("json")
    print(d)
    print("str")
    print(s)
    print("end")


def test_msmg_push():
    msMg = MessageManager()
    msMg.band_trainName("20191120152801")

    ds = build_dataset()
    ds.convertFunDict = {
        "xds" : test_funcion_name
    }

    trainDataSet,validDataSet,_ = ds.split_dataset(strategyValidate=2)

    tdsStaticInfoDict,_ = trainDataSet.describe()
    vdsStaticInfoDict,_ = validDataSet.describe()
    print(tdsStaticInfoDict)
    print(vdsStaticInfoDict)

    msMg.push(tdsStaticInfoDict,"tdsStaticInfoDict")
    msMg.push(vdsStaticInfoDict,"vdsStaticInfoDict")

def test_msmg_pull_to_sql():

    trainName="20191120152801"
    msMg = MessageManager()
    msMg.band_trainName(trainName)

    tdsStaticInfoDictList = msMg.pull_deplete("tdsStaticInfoDict")
    print("------------------")
    print(tdsStaticInfoDictList)
    tdsStaticInfoTable = pd.DataFrame(tdsStaticInfoDictList)
    print("table")
    print(tdsStaticInfoTable)

    con = link_mysql_ifnotexit_creat(trainName)
    engine = create_engine_mysql(trainName)

    tablename = "tdsStaticInfoTable"
    _my_dataframe_to_sql(tdsStaticInfoTable,tablename,con=con,engine=engine,if_exists="append")



def __main():
    # test_build_ds()
    # test_msmg_push()
    test_msmg_pull_to_sql()


if __name__ == "__main__":
    __main()
