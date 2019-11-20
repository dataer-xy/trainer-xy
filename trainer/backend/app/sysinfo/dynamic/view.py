
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

bpSysDynamicInfo = Blueprint(name="bpSysDynamicInfo",url_prefix="/bpSysDynamicInfo")

@bpSysDynamicInfo.route("/", methods=['GET','POST'])
def request_sys_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    sysDynamicInfoDict = interface_sys_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":{
            "partTitle": "机器动态信息",
            "sysDynamicInfoDict":sysDynamicInfoDict # --> {col1:[],col2:[],col3:[]}
        }
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)
