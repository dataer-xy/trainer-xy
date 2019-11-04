
import sys
sys.path.append('/home/syy/projects/AnalysisCEESystem') # 添加路径要在引用之前

from sanic import Sanic
from sanic_cors import CORS
from sanic import Blueprint

from AnalysisCEESystem.config.globalConfig import DEBUG
from AnalysisCEESystem.config.globalConfig import LOG_DIR
from AnalysisCEESystem.config import globalConfig

from AnalysisCEESystem.webserver.app.index.view import bpIndex
from AnalysisCEESystem.webserver.app.notimesearch.view import bpNoTime
from AnalysisCEESystem.webserver.app.timesearch.view import bpTime

import os


# TODO: log OK
import logging

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.INFO
)
logger = logging.getLogger()
handler = logging.FileHandler(os.path.join(LOG_DIR,"webserver.log.txt"))
handler.setLevel(logging.INFO)

logger.addHandler(handler)


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


# TODO: 
# app.static('/static', './static') # while in docker files from static will be served by ngnix（ , host='www.example.com'）
# app.url_for('static', filename='file.txt') == '/static/file.txt'
# app.url_for('static', name='static', filename='file.txt') == '/static/file.txt'


# TODO: 蓝图 OK
bpApi = Blueprint.group(bpIndex, bpNoTime, bpTime, url_prefix='/python') # url 缓冲区
app.blueprint(bpApi)



# TODO: config OK
app.config.from_object(globalConfig) # Objects are usually either modules or classes -- 可以在后面的文件中，通过request.app.config[key] 来引用配置

# TODO: 虚拟主机




# TODO: 
if __name__ =="__main__":
    app.run(host='127.0.0.1', port=8000, debug=DEBUG) #  debug模式 网页上会有堆栈，第二个重要的调试模式下的功能，就是重载器，可以在源文件被修改时自动重启应用





