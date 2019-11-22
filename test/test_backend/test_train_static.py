
from trainer.config.globalconfig import port

import requests

# 
def test_train_static():

    bp = "bpTrainStaticInfo"

    url = "http://127.0.0.1:{port}/python/{bp}".format(
        port=port,
        bp=bp
    ) # 接口地址

    # post 的话，服务器需要设置post允许情况
    jsondata = {
        "mainData":{
            "trainName":"20191118152056",
            "isGetAll":True
        }
    }
    r = requests.post(url,data=None,json=jsondata)
    print(r.json())


def __main():
    test_train_static()

if __name__ == "__main__":
    __main()
