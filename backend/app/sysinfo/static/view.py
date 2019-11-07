
"""
系统静态信息
sysStaticInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_sys_static_info

bpSysStaticInfo = Blueprint(name="bpSysStaticInfo",url_prefix="bpSysStaticInfo")

@bpSysStaticInfo.route("/request_sys_static_info", methods=['GET','POST'])
def request_sys_static_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    sysStaticInfoDict = interface_sys_static_info(trainName,isGetAll)


    responseData = {
        "mainData":sysStaticInfoDict
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
