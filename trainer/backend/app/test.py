
from sanic import Blueprint
from sanic import response



bpRequestTest = Blueprint("bpRequestTest",url_prefix="/bpRequestTest")

@bpRequestTest.route("/",methods=["GET","POST"])
def request_test(request):

    messageJson = request.json 

    print(messageJson)

    import time
    time.sleep(10) 
    responseJson = {"isSuccessful":1, "errMsg":[],"data":{"长时间延迟也可行"}}
    return response.json(responseJson)
    


if __name__ == "__main__":

    from sanic import Sanic
    from sanic_cors import CORS, cross_origin

    app = Sanic(__name__)
    CORS(app) # 全部跨域

    app.blueprint(bpRequestTest)

    app.run(host="127.0.0.1",port=8000) # ,debug=True



