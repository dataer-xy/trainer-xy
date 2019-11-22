import numpy as np 
import pandas as pd 
import ujson as json

def my_pandas_to_dict(df,isOnlyOne=True):
    """"""
    outputDict = {}

    columns = df.columns
    if not isOnlyOne:
        for columnsName in columns:
            outputDict[columnsName] = df[columnsName].tolist() # np.stack(df[columnsName]) 
    else:
        for columnsName in columns:
            outputDict[columnsName] = df[columnsName].tolist()[0]
    return outputDict


def dump_t(dsDynamicInfoDict):
    responseData = {
        "mainData":{
            "partTitle": "数据集动态信息",
            "dsDynamicInfoDict":dsDynamicInfoDict # --> {col1:[],col2:[],col3:[]}
        }
        
    }

    return json.dumps(responseData)


def test_df1():
    pdf = pd.DataFrame([[1,2,3]],columns=list("abc"))
    print(pdf)
    d = my_pandas_to_dict(pdf)
    print(d)



def test_df_json():
    pdf = pd.DataFrame([[1,2,3]],columns=list("abc"))
    print(pdf)
    d = my_pandas_to_dict(pdf)
    print(d)
    b = dump_t(d)
    print(b)

def __main():
    # test_df1()
    test_df_json()

if __name__ == "__main__":
    __main()

