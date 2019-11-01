

import numpy as np 
import pandas as pd

from dataset import DataSet

def build_dataset():
    
    pdf = pd.DataFrame()
    x_data = np.random.rand(2, 100)
    pdf["yTrue"] = np.dot([0.100, 0.200], x_data) + 0.300
    pdf["x"] = x_data

    ds = DataSet(pdf)


    return ds
