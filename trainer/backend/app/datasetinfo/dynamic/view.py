
"""
数据集动态信息
dsIterInfoDict

"""

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_dataset_dynamic_info

bpDsDynamicInfo = Blueprint(name="bpDsDynamicInfo",url_prefix="/bpDsDynamicInfo")

@bpDsDynamicInfo.route("/", methods=['GET','POST'])
def request_dataset_dynamic_info(request):

    messageJson = request.json

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    isGetAll = mainData["isGetAll"]

    dsDynamicInfoDict = interface_dataset_dynamic_info(trainName,isGetAll)


    responseData = {
        "mainData":{
            "partTitle": "数据集动态信息",
            "dsDynamicInfoDict":dsDynamicInfoDict # --> {col1:[],col2:[],col3:[]}
        }
        
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)
