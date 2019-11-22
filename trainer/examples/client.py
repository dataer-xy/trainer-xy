"""客户流程"""


from trainer import MessageManager
msMg = MessageManager()

from .modelconfig import modelConfig 

from .buildds import build_dataset

ds = build_dataset()
ds.batchSize = modelConfig.batchSize

trainDataSet,validDataSet,testDataSet = ds.split_dataset(strategyValidate=2)

from .model import LineModel
lineModel = LineModel()

from .trains import train

def test_train():
    
    print("begin")

    projectName = "testProj"
    train(lineModel,trainDataSet,validDataSet,msMg,projectName)

    print("end")

