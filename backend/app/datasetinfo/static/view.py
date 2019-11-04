"""

路由
请求
请求参数
请求数据
json 请求
响应json

NOTE   
    sanic 依赖于 uvloop 和 ujson
    uvloop 不支持win
    cors 一个是修改头，另一个是用sanic-cors包

"""
try:
    import ujson as jsonModule # 要更快
except :
    import json as jsonModule


from sanic import Blueprint
from sanic import response

# from AnalysisCEESystem.config.globalConfig import DEBUG

from .model import interface_dataset_static_info

dsStaticInfo = Blueprint("dsStaticInfo",url_prefix="/dsStaticInfo")

@dsStaticInfo.route("/dataset-static-info", methods=['GET','POST']) # @cross_origin(app)
def request_dataset_static_info(request):
    """ 查找分组，不带时间

    STEP:
        从request中获取请求参数
        将参数输入到模型中
        返回结果
    
    请求：

    响应：


    EXAMPLE:
        URL (函数)
            /searchgroup

        输入参数(json):
            NOTE: 所有参数都要在request.json中
            {
                "mainData":{
                    "gpby":["area","papertype"], #  分组字段
                    "searchgroup":{"area":"武汉", "papertype":"高考"}, # 查询的组
                    "isSendCorrcoef":1,
                    "isSendFig":1
                }
            }

        输出参数(json):
            {
                "isSuccessful":1, 
                "errMsg":[],
                "data":{
                    "knowCount":{"a":1,"b":2}, # 知识点词频
                    "knowTfidf":{"a":12.2,"b":12},# tfidf字典
                    "corrcoef":{'row1': {'col1': 1, 'col2': 0.5}, 'row2': {'col1': 2, 'col2': 0.75}}, # 相关矩阵
                    "corrfig":"safdafdfdfffff", # 相关系数矩阵图片位置
                    "barfig":"safdafdfdfffff", # bar 图片位置
                    "wcfig":"safdafdfdfffff" # wc 图片位置
                }
            }
    """
    

    if DEBUG:
        print("进入函数。。。")
        print(request)
        print(dir(request))
        
        # OPTION 的时候，body是空，post 的时候，body 是 b"[object Object]""

        # print(request.body) # --> b"[object Object]""
        # print(jsonModule.loads(request.body.decode())) # NOTE: 会出错
        # python 自己请求是好的，而js请求失败，那就是js 请求有错误
        # bytes.decode()
        # on Python 3.5 json.loads only supports str not bytes
        
        # OK 解析输入参数
        messageJson = request.json # --> dict json格式的字符串,并自动调用json解析为dict
        print(messageJson)
        print(type(messageJson)) # dict

        # OK 取出主要的数据
        mainData = messageJson["mainData"]
        print(mainData)
        print(mainData.keys())

        # OK 从主要数据中取出输入参数
        gpby = mainData["gpby"] # --> 
        searchgroup = mainData["searchgroup"]
        isSendCorrcoef = bool(mainData["isSendCorrcoef"])
        isSendFig = bool(mainData["isSendFig"])
        print(gpby),print(searchgroup),print(isSendCorrcoef),print(isSendFig)

        # OK 构建响应数据，测试返回效果
        gpKnowledgeCountDict = {"我":"32","你":"64","tta":"64"}
        gpKnowledgeTfidfDict = {"我":"32","你":"64","tta":"64"}
        import pandas as pd
        vsmVecCorrcoef = pd.DataFrame([[1,2,3],[4,5,5]],columns=["a","b","c"])
        corrfigStr = "AnalysisCEESystem/webserver/notimesearch"
        barfigStr = "AnalysisCEESystem/webserver/notimesearch"
        wcfigStr = "AnalysisCEESystem/webserver/notimesearch"

        responseData = {"knowCount":gpKnowledgeCountDict,
                        "knowTfidf":gpKnowledgeTfidfDict,
                        "corrcoef":vsmVecCorrcoef.to_dict("index"),
                        "corrfig":corrfigStr,
                        "barfig":barfigStr,
                        "wcfig":wcfigStr}

        responseJson = {"isSuccessful":1, "errMsg":[],"data":responseData}
        return response.json(body=responseJson) 


    # TODO: OK 从request中获取数据
    messageJson = request.json # json格式的字符串 -- 是一个章节对象
    # request.args # url 中的参数

    mainData = messageJson["mainData"] # --> dict

    isGetAll= mainData["isGetAll"]

    tdsStaticInfoDict = interface_dataset_static_info(isGetAll)

    responseData = {
        "mainData":tdsStaticInfoDict
    }

    responseJson = {"isSuccessful":1, "errMsg":[],"data":responseData}

    return response.json(body=responseJson)




@bpNoTime.route("/request_test",methods=["GET","POST"])
def request_test(request):
    import time
    time.sleep(10)
    responseJson = {"isSuccessful":1, "errMsg":[],"data":{"长时间延迟也可行"}}
    return response.json(responseJson)
    


if __name__ == "__main__":

    from sanic import Sanic
    from sanic_cors import CORS, cross_origin

    app = Sanic(__name__)
    CORS(app) # 全部跨域

    app.blueprint(bpNoTime)

    app.run(host="127.0.0.1",port=8000) # ,debug=True


