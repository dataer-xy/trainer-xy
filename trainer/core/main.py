#---------------------------------------------------------------------------------
# config配置 
from image2latex.models.myim2latex.config.modelconfig import modelConfig



#---------------------------------------------------------------------------------
# 模型
from image2latex.models.myim2latex.modeleasysrc.model import Im2latexModel

im2latexModel = Im2latexModel()


#---------------------------------------------------------------------------------
# 创建数据集

from image2latex.datahelper.loadDataSet.datagenerator import build_im2latex_dataset

dataset = build_im2latex_dataset() # --> DataSet
dataset.batchSize = modelConfig.batchSize

trainDataSet, validDataSet, testDataSet = dataset.split_dataset(modelConfig.frac,strategyValidate=2) # 创建训练集、验证集和测试集



#---------------------------------------------------------------------------------
# 训练部分
im2latexModel.train(trainDataSet, validDataSet)
