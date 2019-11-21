import os
import sys
from sanic import Sanic
from sanic_cors import CORS
from sanic import Blueprint

from .loger import build_trainerapp_log

from .app.index.view import bpIndex
from .app.trainlist.view import bpTrainList
from .app.batchstate.view import bpBatchState
from .app.datasetinfo.static.view import bpDsStaticInfo
from .app.datasetinfo.dynamic.view import bpDsDynamicInfo
from .app.epochstate.view import bpEpochState
from .app.modelconfiginfo.static.view import bpModelConfigStaticInfo
from .app.msmginfo.static.view import bpMsmgStaticInfo
from .app.sessinfo.view import bpSessDynamicInfo
from .app.summaryinfo.view import bpSummaryDynamicInfo
from .app.sysinfo.static.view import bpSysStaticInfo
from .app.sysinfo.dynamic.view import bpSysDynamicInfo
from .app.traininfo.dynamic.view import bpTrainDynamicInfo
from .app.traininfo.static.view import bpTrainStaticInfo

from .app.test import bpRequestTest



# log OK

logger = build_trainerapp_log()

# OK
app = Sanic()
CORS(app,automatic_options=True) # resolve pre-flight request problem (https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request)


# TODO: 中间件
# @app.middleware('response')
# async def custom_banner(request, response):
#     response.headers["content-type"] = "application/json"


# TODO: 请求的url中多了一个python,需有？/？+url 的缓冲方式
# @app.middleware('request')
# async def add_key(request):
#     # Add a key to request object like dict object
#     request['foo'] = 'bar'


#
app.static('/static', './static')  # while in docker files from static will be served by ngnix（ , host='www.example.com'）
# app.url_for('static', filename='file.txt') == '/static/file.txt'
# app.url_for('static', name='static', filename='file.txt') == '/static/file.txt'


# 蓝图 OK
bpApi = Blueprint.group(
    bpIndex, 
    bpTrainList,
    bpBatchState,
    bpDsStaticInfo,
    bpDsDynamicInfo,
    bpEpochState,
    bpModelConfigStaticInfo,
    bpMsmgStaticInfo,
    bpSessDynamicInfo,
    bpSummaryDynamicInfo,
    bpSysStaticInfo,
    bpSysDynamicInfo,
    bpTrainDynamicInfo,
    bpTrainStaticInfo,
    bpRequestTest,
    url_prefix='/python'
) # url 缓冲区

app.blueprint(bpApi)


# config OK
# app.config.from_object(globalconfig) # Objects are usually either modules or classes -- 可以在后面的文件中，通过request.app.config[key] 来引用配置


# TODO: 虚拟主机

