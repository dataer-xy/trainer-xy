"""路径拼接

linux 和 win 下的路径拼接
"""

import platform

def my_path_join(BASE_DIR,filePathStr):
    """

    TODO:
        可能没有\ OK
        可能不是文件 OK

    INPUT:
        BASE_DIR : r"G:\Project\题目推荐\AnalysisCEESystem"  r"/home/syy/projects/AnalysisCEESystem"
        filePathStr : r"\OutlierDetection\models\myOutlierDetection\modelsrc\client\main_buildmodel.py"
        filePathStr : r"OutlierDetection\models\myOutlierDetection\modelsrc\client\main_buildmodel.py"
    
    """

    sysstr = platform.system()
    if sysstr == "Windows":
        if filePathStr[0] != "\\":
            filePathStr = "\\" + filePathStr
        if BASE_DIR[-1] == "\\":
            BASE_DIR = BASE_DIR[0:-1]
        filePathStr = BASE_DIR + filePathStr

    else:
        if filePathStr[0] != "/":
            filePathStr = "/" + filePathStr
        if BASE_DIR[-1] == "/":
            BASE_DIR = BASE_DIR[0:-1]
        filePathStr = BASE_DIR + filePathStr.replace("\\","/")
    
    return filePathStr

