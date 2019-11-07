
import os
import platform

# debug
DEBUG = False

# 文件编码方式
ENCODING = "utf-8"

# 项目的根目录
sysstr = platform.system()
if sysstr == "Windows":
    BASE_DIR = r"G:\Project\Trainer"
else:
    BASE_DIR = r"/home/syy/projects/Trainer"

# 日志目录 
LOG_DIR = os.path.join(BASE_DIR,"log")

# 前端开发的位置
FRONTFACE_DIR = os.path.join(BASE_DIR,r"frontface\app\build")

# 
port = "8075" # 后端app始终都是这个
proxyPort = "8076" # 这个是前端和nginx代理的端口


# # # # 
# 图片

# DATABASE = "" # 一个 trainName 一个数据库

