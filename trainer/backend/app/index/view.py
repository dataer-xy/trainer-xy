
""" 发送 index.html

NOTE: 静态文件由 nginx 发送

"""

import os 

try:
    import ujson as jsonModule
except:
    import json as jsonModule

from sanic import Blueprint
from sanic import response


bpIndex = Blueprint(name="bpIndex",url_prefix="bpIndex")

@bpIndex.route("/",methods=["GET","POST"])
def index(request):
    """"""
    # TODO
    messageJson = request.json

    mainData = messageJson["mainData"]

    indexFile = os.path.join( os.path.abspath( os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir,os.pardir)),"static","html")
    
    return response.file()