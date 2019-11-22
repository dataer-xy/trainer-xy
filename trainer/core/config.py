
import os
import platform
from abc import ABCMeta
# import getpass

#-------------------------------------------------------------

# debug
DEBUG = False

# 文件编码方式
ENCODING = "utf-8"

# 
PORT = "8075"

ProxyPort = "8076"

#-------------------------------------------------------------

class ConfigBase(metaclass=ABCMeta):
    """config 抽象类/基类"""


class TrainerConfig(ConfigBase):
    """ 实现类 (模仿struct)

    """

    def __init__(self):
        self.isLog = True
        self.superTheta1 = 0.7
        self.superThetaMaxTry = 10
        self.isUseRepair = True

        # 
        sysstr = platform.system() # Windows/Linux
        # userName = getpass.getuser() # 获取当前用户名
        if sysstr == "Windows":
            self.Trainer_APP_DIR = r"D:\.trainer\app"
            
        else:
            self.Trainer_APP_DIR = r"~/.trainer\app"

        # 日志目录 
        self.Trainer_LOG_DIR = os.path.join(self.Trainer_APP_DIR,r"trainer-log") # 统一路径

        #
        self.port = PORT # 后端app始终都是这个
        self.proxyPort = ProxyPort # 这个是前端和nginx代理的端口
        
        

# 静态配置量
trainerConfig = TrainerConfig()


