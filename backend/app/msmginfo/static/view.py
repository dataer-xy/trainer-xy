
"""
消息队列静态信息
msmgInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_msmg_static_info

bpMsmgStaticInfo = Blueprint(name="bpMsmgStaticInfo",url_prefix="bpMsmgStaticInfo")

@bpMsmgStaticInfo.route("/request_msmg_static_info", methods=['GET','POST'])
def request_msmg_static_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    msmgStaticInfoDict = interface_msmg_static_info(trainName,isGetAll)


    responseData = {
        "mainData":msmgStaticInfoDict
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
