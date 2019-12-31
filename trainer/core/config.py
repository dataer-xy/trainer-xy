
import os
import platform
from abc import ABCMeta

#-------------------------------------------------------------

# debug
DEBUG = False

# 文件编码方式
ENCODING = "utf-8"

# web
PORT = "8075"
ProxyPort = "8076"

# sql
MYSqlHost = '127.0.0.1'
MYSqlUser = 'root'
MYSqlPassword = "" # TODO
MYSqlPort = 3306

# mq
RbtMQhost = "localhost"
RbtMQport = 5672
RbtMQvirtualHost = "testhost"
RbtMQuser = "admin" # 测试用
RbtMQpassword = "admin"


#-------------------------------------------------------------

class ConfigBase(metaclass=ABCMeta):
    """config 抽象类/基类"""


class TrainerConfig(ConfigBase):
    """ 实现类 (模仿struct)

    """

    def __init__(self):
        self.isLog = True

        # 
        sysstr = platform.system() # Windows/Linux
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


