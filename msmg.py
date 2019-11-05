
"""消息管理器"""



class MqConn(object):
    def band(self,projectName):
        pass

    def push(self,a,topic):
        pass
    
    def pull(self,topic):
        pass

    def clear(self,projectName):
        pass


class Serializer(object):
    def serialize(self,a):
        pass
    def serialize_inv(self,b):
        pass



class MessageManager(object):
    
    def __init__(self):
        self.mqConn = None
        self.serializer = None

    def push(self,data,topic):
        pass
    
    def pull(self,topic):
        pass

    def show_all_topic(self):
        pass

    def get_message(self):
        pass






