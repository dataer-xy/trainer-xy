import os

from ._errors import UtilsException


class MakeDirException(UtilsException):
    """创建文件夹错误"""

# 创建文件夹
def mkdir_my(filepath):
    '''
        创建路径/文件夹
    '''
    try:
        filepath = filepath.strip()  # 去除首位空格
        filepath = filepath.rstrip("\\")  # 去除尾部 \ 符号
        isExists = os.path.exists(filepath)  # 判断路径是否存在
        # 如果不存在则创建目录
        if not isExists:
            try:
                os.mkdir(filepath)
            except:
                os.makedirs(filepath)
    except:
        raise MakeDirException("创建文件夹错误！")