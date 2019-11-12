
"""
训练静态信息
trainStaticInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_train_static_info

bpTrainStaticInfo = Blueprint(name="bpTrainStaticInfo",url_prefix="bpTrainStaticInfo")

@bpTrainStaticInfo.route("/", methods=['GET','POST'])
def request_train_static_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    trainStaticInfoDict = interface_train_static_info(trainName,isGetAll)


    responseData = {
        "mainData":{
            "partTitle":"训练静态信息",
            "trainStaticInfoDict":trainStaticInfoDict
        }
        
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
