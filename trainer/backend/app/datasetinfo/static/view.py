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


from .model import interface_dataset_static_info

bpDsStaticInfo = Blueprint("bpDsStaticInfo",url_prefix="/bpDsStaticInfo")

@bpDsStaticInfo.route("/", methods=['GET','POST']) # @cross_origin(app)
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
    
    messageJson = request.json # json格式的字符串 -- 是一个章节对象

    mainData = messageJson["mainData"] # --> dict

    trainName = mainData["trainName"]
    isGetAll= mainData["isGetAll"]

    dsStaticInfoDict = interface_dataset_static_info(trainName,isGetAll)

    responseData = {
        "mainData":{
            "partTitle":"数据集静态信息",
            "dsStaticInfoDict":dsStaticInfoDict # --> dict 完全
        }
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)


