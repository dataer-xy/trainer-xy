import os

from ..utils.pathJoinUtils import my_path_join
from ..utils.dirFileUtils import mkdir_my

#--------------------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir)) # 父级目录

OUTPUT_BASE = my_path_join(BASE_DIR,r"outputs")

checkpointPath = my_path_join(OUTPUT_BASE,r"checkpointPath")
mkdir_my(checkpointPath)

tensorboardLogPath = my_path_join(OUTPUT_BASE,r"tensorboardLogPath")
mkdir_my(tensorboardLogPath)

exportPath = my_path_join(OUTPUT_BASE,r"exportPath") # NOTE: 不能存在
# mkdir_my(exportPath)

historyPath = my_path_join(OUTPUT_BASE,r"historyPath")
mkdir_my(historyPath)



class ModelConfig(object):
    
    def __init__(self):
        self.learnRate = 0.5 # 学习率
        self.deno = 1000 # 分母

        # 训练部分
        self.batchSize = 64 # OK

        self.epochs = 500 # epoch 次数 step = epochs*批次数 NOTE: 10 epoch 需要 1/4 天

        self.validFrequency = 2 # ? 个 epoch 验证 1 次

        self.runMetaDataFrequency = None # 多少尺度运行一次 runmetadata

        #---------------------------------------------------
        # 存储

        self.printStep = 20 # OK

        self.summaryStepSave = 20 # 每 20 step 保存一次 summary
        
        self.modelStepSave = 1000 # 每 1000 step 保存一次 model

        self.hiddenLayerStepSave = 50 # 每 50 step 保存一次 history

        self.checkpointPath = checkpointPath # NOTE: 需要是一个空文件夹。存储保存路径，保存了graph和网络参数值

        self.checkpointModelName = "linemodel"

        self.tensorboardLogPath = tensorboardLogPath # 可视化的保存路径，按epoch记录 # OK

        self.exportPath = exportPath # save_model 保存模型 # OK

        self.historyPath = historyPath # OK
    
    def to_dict(self):
        """类属性转化为字典"""
        outDict = {}
        attrList = dir(self)
        for attrStr in attrList:
            attr = getattr(self, attrStr)
            if not attrStr.endswith("__") and not callable(attr):
                outDict[attrStr] = attr

        return outDict


modelConfig = ModelConfig()
