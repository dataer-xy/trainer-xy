
""""""

import pika

from .config import RbtMQhost
from .config import RbtMQport
from .config import RbtMQvirtualHost
from .config import RbtMQuser
from .config import RbtMQpassword

from ..utils.systemTypeUtils import use_platform
systype = use_platform()
if systype == "Windows":
    encoding = "gbk"
else:
    encoding = "utf-8"


class MqConn(object):
    """ 消息队列工具 工厂
    
    可以是继承模式，或者聚合模式
    """

    host = RbtMQhost
    port =RbtMQport
    virtualHost = RbtMQvirtualHost
    user = RbtMQuser
    password = RbtMQpassword

    def __init__(self,connType="rabbitmq",**kargs):
        """ 构建工厂 构建不同的 conn"""

        if connType == "rabbitmq":
            credentials = pika.PlainCredentials(self.user, self.password) # 链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）

            self.conn = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.host,
                    port=self.port,
                    virtual_host=self.virtualHost,
                    credentials=credentials
                )
            )

            self.channel = self.conn.channel()

        self.connType = connType

    def push(self,data,topic):
        """ 发送
        
        
        Parameters
        ----------
        topic : str
            主题即队列 : topic = "test"
        data : bytes
            数据即消息 : dill.dumps({"a":[1,2,3],"b":np.array([1,2,3])})

        """
        self.channel.queue_declare(queue=topic, durable=True) # 创建队列。有就不管，没有就自动创建。durable 指定持久化
        self.channel.basic_publish(
            exchange="",
            routing_key=topic,
            body=data, # 需要 b"str" , json,pickle
            properties=pika.BasicProperties(
                delivery_mode = 2, # 使消息或任务也持久化存储
            )
        )

    def pull(self,topic):
        """ 拉取
        一次一条数据
        
        Parameters
        ----------
        topic : str
            主题即队列 : topic = "test"
        
        Returns
        -------
        method : spec.Basic.GetOk|None
            方法 <Basic.GetOk(['delivery_tag=2', 'exchange=', 'message_count=0', 'redelivered=False', 'routing_key=test2'])>
        properties :  spec.BasicProperties|None
            <BasicProperties(["delivery_mode=2])>
        body : bytes|None
            消息即数据 
        """

        self.channel.queue_declare(queue=topic, durable=True) # 

        method, properties, body = self.channel.basic_get(
            queue=topic, 
            auto_ack=True
        ) # auto_ack=True（默认为False，即必须有确认标识）,在回调函数consumer_callback中，未收到确认标识，那么，RabbitMQ会重新将该任务添加到队列中。

        return method, properties, body

    def close(self):
        self.channel.close()
        self.conn.close()

    def delete_queue(self,topic, if_unused=False, if_empty=False):
        """ 删除队列 
        
        :param str queue: The queue to delete
        :param bool if_unused: only delete if it's unused
        :param bool if_empty: only delete if the queue is empty
        :returns: Method frame from the Queue.Delete-ok response
        :rtype: `pika.frame.Method` having `method` attribute of type
            `spec.Queue.DeleteOk`
        """
        self.channel.queue_delete(topic,if_unused,if_empty)


class Serializer(object):
    """序列化工具 工厂
    
    可以是继承模式，或者聚合模式
    """

    def __init__(self,serializeType="dill"):
        if serializeType == "dill":
            import dill 

            self.serializeTool = dill 
        elif serializeType == "json":
            try:
                import ujson as jsonModule
            except:
                import json as jsonModule
            self.serializeTool = jsonModule
        
        elif serializeType == "pickle":
            import pickle

            self.serializeTool = pickle

        else:
            raise Exception("没有实现其他序列化工具")

        self.serializeType = serializeType


    def serialize(self,a):
        """序列化"""
        return self.serializeTool.dumps(a)


    def serialize_inv(self,b):
        """反序列化"""
        if b is not None:
            return self.serializeTool.loads(b)
        else:
            return b


class MessageManager(object):
    """消息管理器 
    
    聚合了一个消息队列连接器和一个序列化器
    """
    
    def __init__(self):
        self.connType = "rabbitmq"
        self.serializeType = "dill"
        self.mqConn = MqConn(connType=self.connType)
        self.serializer = Serializer(serializeType=self.serializeType)

        self.trainName = None # NOTE: 声明，为绑定留位置。并不是属性，而是依赖，绑定是为了防止调用时未声明的情况
    
    def band_trainName(self,trainName):
        """绑定到某个项目/trainName 上
        
        Notes
        -----
        1、一旦绑定之后，推送/拉取的消息队列（topic）名称都会
        被修改为 trainName_topic。这有助于识别/区分每个队列是哪个
        trainName 下的。
        2、可以统一删除某个 trainName 下的所有队列。

        """
        self.trainName = trainName

    def free_trainName(self):
        """ 释放 trainName

        解除 trainName 的绑定，是 band_trainName 方法的逆变换。
        
        """
        self.trainName = None

    def _rename_topic(self,topic):
        if self.trainName:
            topic = "{proj}_{topic}".format(
                proj=self.trainName,
                topic=topic
            )
        return topic


    def push(self,data,topic):
        """ 推送消息/数据到主题/队列中

        Parameters
        ----------
        data : py data (任何可序列化的 py 对象)
            消息即数据
        topic : str
            队列即主题

        Notes
        -----
        1、如果已经绑定到了某个 trainName 下，消息队列（topic）名称都会
        被修改为 trainName_topic。
        2、数据会在该方法中被序列化，拉取的时候也会自动的反序列化，这个
        过程对用户是不可见的。
        
        """

        # 管理主题
        topic = self._rename_topic(topic)

        # 序列化
        if not isinstance(data,bytes):
            dataBytes = self.serializer.serialize(data)
        else:
            dataBytes = data

        # 发送
        self.mqConn.push(dataBytes,topic)

    
    def pull(self,topic):
        """ 拉取 -- 一次一条数据

        Parameters
        ----------
        topic : str
            队列即主题
        
        Notes
        -----
        1、拉取的数据会被自动反序列化。
        """

        # 管理主题
        topic = self._rename_topic(topic)

        # 拉取 
        _,_,dataBytes = self.mqConn.pull(topic)

        # 反序列化
        data = self.serializer.serialize_inv(dataBytes)

        return data
    

    def pull_deplete(self,topic):
        """ 拉取 -- 取尽队列 

        Parameters
        ----------
        topic : str
            队列即主题
        
        Notes
        -----
        1、拉取的数据会被自动反序列化。        
        """
        dataList = []

        while True:
            data = self.pull(topic)
            if data is not None:
                dataList.append(data)
            else:
                break
        
        return dataList


    def show_all_topic(self):
        print(self.list_queues())


    def list_queues(self):
        """ 列出某虚拟机下所有队列 
        
        Notes
        ------
        1、仅针对 rabbitmq。
        2、对于其他的队列，需要修改这个地方。
        """
        hostName = self.mqConn.virtualHost

        if hostName is not None:
            import subprocess
            cmd = "rabbitmqctl list_queues -p {hostName}".format(hostName=hostName)
            ret = subprocess.run(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if ret.returncode != 0: 
                print("公式正则化子程序错误！\n {err}".format(err=ret.stderr.decode(encoding)))
                queueNameList = []
            else:
                returnStr = ret.stdout.decode(encoding)

                tempList1 = returnStr.splitlines()[3:]

                queueNameList = [itemStr.split()[0] for itemStr in tempList1] # --> list[str]

            return queueNameList


    def delete_queue(self,topic):
        """删除某个主题/队列
        
        Parameters
        ----------
        topic : str
            队列即主题
        
        Notes
        -----
        1、如果已经绑定到了某个 trainName 下，消息队列（topic）名称都会
        被修改为 trainName_topic。
        """
        # 管理主题
        topic = self._rename_topic(topic)

        # 删除
        self.mqConn.delete_queue(topic=topic)


    def clear_trainName(self,trainName=None):
        """ 清除某 train 下的所有队列 
        
        如果某次训练不理想，可以统一删除该训练下的所有队列

        Parameters
        ----------
        trainName : str / None
            项目名称，用于过滤
        """

        if trainName is None:
            trainName = self.trainName
        
        queueNameList = self.list_queues()

        # 循环删除队列
        for queueName in queueNameList:
            if queueName.split("_")[0] == trainName:
                self.mqConn.delete_queue(topic=queueName) 


    def describe(self):
        """ MSMG 的信息 
        
        用于将 msmg 的信息发送到可视化部分
        """

        msmgInfoDict = {
            "connType":self.connType,
            "serializeType":self.serializeType,
            "host":self.mqConn.host,
            "port":self.mqConn.port,
            "virtualHost":self.mqConn.virtualHost,
            "user":self.mqConn.user,
            # "password":self.mqConn.password,
        }

        return msmgInfoDict



def __test1():
    
    msMg = MessageManager()
    msMg.clear_trainName("a")

    print("end")

def __main():
    __test1()


if __name__ == "__main__":
    __main()

