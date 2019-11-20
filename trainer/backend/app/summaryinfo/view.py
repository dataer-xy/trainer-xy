
"""
summary 动态信息
summaryInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_summary_dynamic_info

bpSummaryDynamicInfo = Blueprint(name="bpSummaryDynamicInfo",url_prefix="/bpSummaryDynamicInfo")

@bpSummaryDynamicInfo.route("/", methods=['GET','POST'])
def request_summary_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = False

    interface_summary_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":None
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)
