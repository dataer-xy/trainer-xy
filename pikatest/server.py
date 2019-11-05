

import pika 


credentials = pika.PlainCredentials('admin', 'admin')
# 链接rabbit服务器（localhost是本机，如果是其他服务器请修改为ip地址）
conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672,virtual_host='testhost',credentials=credentials))

# conn = pika.BlockingConnection()



for i in range(10):
    print(i)
    channel = conn.channel()
    channel.queue_declare(queue='test', durable=True) # 创建队列。有就不管，没有就自动创建。durable 指定持久化

    channel.basic_publish(
        exchange="test",
        routing_key="test",
        body=b"Test message.",
        properties=pika.BasicProperties(
            delivery_mode = 2, # 使消息或任务也持久化存储
        )
    )


conn.close()


#  注意：如果仅仅是设置了队列的持久化，仅队列本身可以在rabbit-server宕机后保留，队列中的信息依然会丢失，如果想让队列中的信息或者任务保留，还需要做以下设置：
# 消息队列持久化包括3个部分：
#     　　（1）exchange持久化，在声明时指定durable => 1
#     　　（2）queue持久化，在声明时指定durable => 1
#     　　（3）消息持久化，在投递时指定delivery_mode=> 2（1是非持久化）

#     如果exchange和queue都是持久化的，那么它们之间的binding也是持久化的。如果exchange和queue两者之间有一个持久化，一个非持久化，就不允许建立绑定。



