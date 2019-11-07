
""" epoch 状态回传到消息队列 """

try:
    import ujson as jsonModule
except :
    import json as jsonModule


from sanic import Blueprint
from sanic import response


from .model import interface_send_epochState_to_mq


bpEpochState = Blueprint(name="bpEpochState",url_prefix="bpEpochState")

@bpEpochState.route("/",methods=['GET','POST'])
def request_epoch_state(request):
    
    messageJson = request.json 

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    epochState = mainData["epochState"]

    interface_send_epochState_to_mq(trainName,epochState)

    responseData = {
        "mainData":None
    }

    responseJson = {
        "isSuccessful":1, 
        "errMsg":[],
        "data":responseData
    }

    return response.json(body=responseJson)
