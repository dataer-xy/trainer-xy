
"""
sess 动态信息
sessInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_sess_dynamic_info

bpSessDynamicInfo = Blueprint(name="bpSessDynamicInfo",url_prefix="/bpSessDynamicInfo")

@bpSessDynamicInfo.route("/", methods=['GET','POST'])
def request_sess_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = False

    interface_sess_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":None
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)
