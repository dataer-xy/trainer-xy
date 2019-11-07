
"""
系统动态信息
sysIterInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_sys_dynamic_info

bpSysDynamicInfo = Blueprint(name="bpSysDynamicInfo",url_prefix="bpSysDynamicInfo")

@bpSysDynamicInfo.route("/request_sys_dynamic_info", methods=['GET','POST'])
def request_sys_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    sysDynamicInfoDict = interface_sys_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":sysDynamicInfoDict
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
