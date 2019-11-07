
from ..basemodel import message_to_mq

def interface_send_batchState_to_mq(trainName,batchState):
    """ batchState 传到消息队列"""
    topic = "batchState"
    message_to_mq(trainName,data=batchState,topic=topic)


