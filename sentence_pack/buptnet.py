# ubuntu实现自动启动此脚本
# root权限修改/etc/rc.local文件在exit 0上一行加上 python3 xiaoyuanwang.py
# 即可实现开机启动此脚本

# python 2.7 python 3.5均可用
# 脚本外部依赖requests库，请在运行脚本前pip3或者pip安装requests

# python 2.7运行时务必加上下面一行代码，指定编码为utf8，python3可以忽略。
# coding: utf-8
import requests


url = 'http://10.3.8.211/login'


def login():
    postdata = {'user': '13410008',
                'pass': 'jinziooo',
                }
    headers = {'Accept': '*/*',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Content-Length': '27',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Cookie': 'SessionId=a09229def63b0b38',
               'Host': '10.3.8.211',
               'Origin': 'http://10.3.8.211',
               'Referer': 'http://10.3.8.211/index',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    requests.post(url, data=postdata)


def is_connect_edu():
    status_code = requests.get(url).status_code
    if status_code == 200:
        return True
    else:
        return False


def is_connect_web():
    r = requests.get("http://www.baidu.com").text
    if r.find('网络认证登录') != -1:
        return False
    else:
        return True


while True:
    if is_connect_edu():  # 是否连接上校园网
        if not is_connect_web():  # 是否连接上外网
            login()
            if requests.get('http://www.baidu.com').status_code == 200:
                print('Already connected Internet')
            else:
                print('Not connected Internet')
        break
