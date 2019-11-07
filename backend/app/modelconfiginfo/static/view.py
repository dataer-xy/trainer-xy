
"""
模型配置的静态信息
modelConfigStaticInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_modelconfig_static_info

bpModelConfigStaticInfo = Blueprint(name="bpModelConfigStaticInfo",url_prefix="bpModelConfigStaticInfo")

@bpModelConfigStaticInfo.route("/request_modelconfig_static_info", methods=['GET','POST'])
def request_modelconfig_static_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    modelconfigStaticInfoDict = interface_modelconfig_static_info(trainName,isGetAll)


    responseData = {
        "mainData":modelconfigStaticInfoDict
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
