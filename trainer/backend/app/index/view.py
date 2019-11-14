
""" 发送 index.html """


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
    
    return response.html()