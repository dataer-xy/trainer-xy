

import numpy as np 
import pandas as pd

from dataset import DataSet

def build_dataset():
    
    # 
    nSample = 5000 # 样本数量
    xData = np.random.rand(2, nSample)
    wTrue = [0.100, 0.200]
    bTrue = 0.300
    
    pdf = pd.DataFrame()
    pdf["yTrue"] = np.dot(wTrue, xData) + bTrue
    pdf["x"] = xData.T.tolist()

    # 
    ds = DataSet(pdf)

    # 设置
    ds.batchSize = 64 # 批次大小

  

    return ds


def __test1():
    ds = build_dataset()
    # tab = ds.show()

    for outputDict in ds.iter():
        x = outputDict["x"]
        print(x)
        
    print("end")



def __main():
    __test1()



if __name__ == "__main__":
    __main()