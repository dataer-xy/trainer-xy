"""
数据集静态信息
--------------------------------
路由
请求
请求参数
请求数据
json 请求
响应json

NOTE   
    sanic 依赖于 uvloop 和 ujson
    uvloop 不支持win
    cors 一个是修改头，另一个是用sanic-cors包

"""
try:
    import ujson as jsonModule # 要更快
except :
    import json as jsonModule


from sanic import Blueprint
from sanic import response

# from AnalysisCEESystem.config.globalConfig import DEBUG

from .model import interface_dataset_static_info

bpDsStaticInfo = Blueprint("bpDsStaticInfo",url_prefix="/bpDsStaticInfo")

@bpDsStaticInfo.route("/request_dataset_static_info", methods=['GET','POST']) # @cross_origin(app)
def request_dataset_static_info(request):
    """ 查找分组，不带时间

    STEP:
        从request中获取请求参数
        将参数输入到模型中
        返回结果
    
    请求：

    响应：

    EXAMPLE:
        URL (函数)
            /searchgroup

        输入参数(json):
            NOTE: 所有参数都要在request.json中
            {
                "mainData":{

                }
            }

        输出参数(json):
            {
                "isSuccessful":1, 
                "errMsg":[],
                "data":{

                }
            }
    """
    

    if DEBUG:
        print("进入函数。。。")
        print(request)
        print(dir(request))
        
        # OPTION 的时候，body是空，post 的时候，body 是 b"[object Object]""

        # print(request.body) # --> b"[object Object]""
        # print(jsonModule.loads(request.body.decode())) # NOTE: 会出错
        # python 自己请求是好的，而js请求失败，那就是js 请求有错误
        # bytes.decode()
        # on Python 3.5 json.loads only supports str not bytes
        
        # OK 解析输入参数
        messageJson = request.json # --> dict json格式的字符串,并自动调用json解析为dict
        print(messageJson)
        print(type(messageJson)) # dict

        # OK 取出主要的数据
        mainData = messageJson["mainData"]
        print(mainData)
        print(mainData.keys())

        # OK 从主要数据中取出输入参数
        gpby = mainData["gpby"] # --> 
        searchgroup = mainData["searchgroup"]
        isSendCorrcoef = bool(mainData["isSendCorrcoef"])
        isSendFig = bool(mainData["isSendFig"])
        print(gpby),print(searchgroup),print(isSendCorrcoef),print(isSendFig)

        # OK 构建响应数据，测试返回效果
        gpKnowledgeCountDict = {"我":"32","你":"64","tta":"64"}
        gpKnowledgeTfidfDict = {"我":"32","你":"64","tta":"64"}
        import pandas as pd
        vsmVecCorrcoef = pd.DataFrame([[1,2,3],[4,5,5]],columns=["a","b","c"])
        corrfigStr = "AnalysisCEESystem/webserver/notimesearch"
        barfigStr = "AnalysisCEESystem/webserver/notimesearch"
        wcfigStr = "AnalysisCEESystem/webserver/notimesearch"

        responseData = {"knowCount":gpKnowledgeCountDict,
                        "knowTfidf":gpKnowledgeTfidfDict,
                        "corrcoef":vsmVecCorrcoef.to_dict("index"),
                        "corrfig":corrfigStr,
                        "barfig":barfigStr,
                        "wcfig":wcfigStr}

        responseJson = {"isSuccessful":1, "errMsg":[],"data":responseData}
        return response.json(body=responseJson) 


    # TODO: OK 从request中获取数据
    messageJson = request.json # json格式的字符串 -- 是一个章节对象
    # request.args # url 中的参数

    mainData = messageJson["mainData"] # --> dict

    trainName = mainData["trainName"]
    isGetAll= mainData["isGetAll"]

    dsStaticInfoDict = interface_dataset_static_info(trainName,isGetAll)

    responseData = {
        "mainData":dsStaticInfoDict
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)


