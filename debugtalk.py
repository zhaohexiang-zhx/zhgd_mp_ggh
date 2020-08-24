import time
import requests


def sleep(n_secs):
    time.sleep(n_secs)

# 11位
def get_timestamp():
    return str(int(time.time() * 10))
# 10位
def get_timestamp1():
    return str(time.time()).replace(".", " ")[5:10]

# 登录三级用户并获取token
def debug_token(username="runner_admin", password="72732414d750775c1eb0b5b915b3561b"):
    url = "http://10.23.190.107/zhgd_mms/user/login"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; VOG-AL00 Build/HUAWEIVOG-AL00;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120MQQBrowser/6.2 TBS/045227 Mobile Safari/537.36 MMWEBID/3549 MicroMessenger/7.0.17.1720(0x27001139)Process/tools WeChat/arm64 NetType/WIFI Language/zh_CN ABI/arm64",
        "X-Requested-With": "com.tencent.mm"
    }
    body = {
        "_sign": '9f66ca82115e8ed69b67b09c1ac77c97',
        "_timestamp": '1597904422000',
        "loginName": username,
        "password": password,
        "terminal": 'wechat',
        "token": '',
        "v": ''
    }
    r = requests.post(url, headers=headers, data=body)
    try:
        return_token = r.json()["results"]["data"]["token"]
    except:
        print("没取到token \n %s" % r.text)
        return_token = ''
    return return_token
if __name__ == "__main__":
    return_token = debug_token()
    print(return_token)


# 登录一级用户并获取token
# def get_token(username="zhaohexiang1", password="72732414d750775c1eb0b5b915b3561b"):
#     url = "http://10.23.190.107/zhgd_mms/user/login"
#     headers = {
#         "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
#         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
#     }
#     body = {
#         "_sign": 'bd49d5b78c71d2268c181e9c70ba9233',
#         "_timestamp": '1596009876000',
#         "loginName": username,
#         "password": password,
#         "terminal":'pc',
#         "token": '',
#         "v": ''
#     }
#     r = requests.post(url, headers=headers, data=body)
#     try:
#         # 获取token的方法：["一级"]["二级"]["..."]
#         return_token = r.json()["results"]["data"]["token"]
#     except:
#         print("没取到token \n %s" % r.text)
#         return_token = ''
#     return return_token

# if __name__ == "__main__":
#     return_token = get_token()
    # print(return_token)