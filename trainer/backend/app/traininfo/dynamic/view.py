
"""
训练动态信息
trainIterInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_train_dynamic_info

bpTrainDynamicInfo = Blueprint(name="bpTrainDynamicInfo",url_prefix="/bpTrainDynamicInfo")

@bpTrainDynamicInfo.route("/", methods=['GET','POST'])
def request_train_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    trainDynamicInfoDict = interface_train_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":{
            "partTitle":"训练动态信息",
            "trainDynamicInfoDict":trainDynamicInfoDict
        }
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
