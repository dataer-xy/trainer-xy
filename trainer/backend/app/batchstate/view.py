
""" batch 状态回传到消息队列 """

try:
    import ujson as jsonModule
except :
    import json as jsonModule


from sanic import Blueprint
from sanic import response


from .model import interface_send_batchState_to_mq


bpBatchState = Blueprint(name="bpBatchState",url_prefix="/bpBatchState")

@bpBatchState.route("/",methods=['GET','POST'])
def request_batch_state(request):
    
    messageJson = request.json 

    mainData = messageJson["mainData"]

    trainName = mainData["trainName"]
    batchState = mainData["state"]

    interface_send_batchState_to_mq(trainName,batchState)

    responseData = {
        "mainData":None
    }

    # responseJson = {
    #     "isSuccessful":1, 
    #     "errMsg":[],
    #     "data":responseData
    # }

    return response.json(body=responseData)
