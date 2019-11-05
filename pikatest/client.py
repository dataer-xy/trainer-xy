
"""
rabbitmq-plugins enable rabbitmq_management
http://127.0.0.1:15672/

https://www.cnblogs.com/pangguoping/p/5720134.html

"""
import pika

# 连接服务器

credentials = pika.PlainCredentials('admin', 'admin') # 链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672,virtual_host='testhost',credentials=credentials))

channel = conn.channel()

# rabbitmq消费端仍然使用此方法创建队列。这样做的意思是：若是没有就创建。和发送端道理道理。目的是为了保证队列一定会有

channel.queue_declare(queue='test1') # ,durable=True

# 收到消息后的回调

def callback(ch, method, properties, body):

    print(" [x] Received %r" % body)

channel.basic_consume(
    queue='test1', 
    on_message_callback=callback,
    auto_ack=False
) # auto_ack=True（默认为False，即必须有确认标识）,在回调函数consumer_callback中，未收到确认标识，那么，RabbitMQ会重新将该任务添加到队列中。

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming() # # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。

