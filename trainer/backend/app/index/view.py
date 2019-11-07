
""" 获取所有 projectName/trainName 信息 """


try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response

from .model import interface_get_all_trainer

bpIndex = Blueprint(name="bpIndex",url_prefix="bpIndex")

@bpIndex.route("/",methods=["GET","POST"])
def index(request):
    """"""

    messageJson = request.json

    mainData = messageJson["mainData"]
    
    projectNameList = interface_get_all_trainer()

    responseData = {
        "mainData":projectNameList
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)