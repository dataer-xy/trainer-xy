.. _api.msmg:


====
MsMg
====

.. currentmodule:: trainer

Constructor
-----------

.. autosummary::
   :toctree: api/

    MessageManager


Attributes
----------

.. autosummary::
    :toctree: api/

    MessageManager.band_trainName
    MessageManager.free_trainName


主题/队列
---------

.. autosummary::
    :toctree : api/

    MessageManager.push
    MessageManager.pull
    MessageManager.pull_deplete
    MessageManager.delete_queue
    MessageManager.list_queues
    MessageManager.show_all_topic


描述
-----

.. autosummary::
    :toctree: api/
    
    MessageManager.describe


========
序列化器
========


创建
-----

.. autosummary::
    :toctree: api/

    Serializer


方法
-----

.. autosummary::
    :toctree: api/

    Serializer.serialize
    Serializer.serialize_inv


==============
消息队列连接器
==============


创建 
-----
.. autosummary::
    :toctree: api/

    MqConn


方法
-----

.. autosummary::
    :toctree: api/

    MqConn.push
    MqConn.pull
    MqConn.close
    MqConn.delete_queue


