
from trainer.config.globalconfig import port

import requests

# OK
def test_request_test():

    url = "http://127.0.0.1:{port}/python/bpRequestTest".format(port=port)  # 接口地址

    # 需要包括协议方案：
    # 'http://192.168.1.61:8080/api/call'
    # 没有http://部分，requests不知道如何连接到远程服务器。

    # 消息头数据 -- 没有也可以
    # headers = {
    #     'Connection': 'keep-alive',
    #     'Content-Length': '123',
    #     'Cache-Control': 'max-age=0',
    #     'Origin':'https://passport.csdn.net',
    #     'Upgrade-Insecure-Requests':'1',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Cookie': '省略',
    # }
    # 在url 中传递参数
    # payload = {
    #     'username':'**',
    #     'password':'**',
    #     'lt':'**',
    #     'execution':'e1s1',
    #     '_eventId':'submit',
    # }
    # verify = False 忽略SSH 验证 

    # r = requests.get(url) # , json=payload,headers=headers,verify=False,data = {'key':'value'}

    # post 的话，服务器需要设置post允许情况
    jsondata = {"hello":"python"}
    r = requests.post(url,data=None,json=jsondata)
    print(r.json())


def __main():
    test_request_test()

if __name__ == "__main__":
    __main()
