import requests
import json
import hashlib
import execjs
import os
os.environ["NODE_PATH"] = os.getcwd()+"/node_modules"

# base_url = 'http://bmfw.www.gov.cn/yqfxdjcx/index.html'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'http://bmfw.www.gov.cn/yqfxdjcx/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'x-wif-signature': 'CF5F215FBE55BB7A6C51E3EA0D33D4808AD8856948A182D856FF286B77514735',
    'x-wif-timestamp': '1594208193'
    }

json_url = 'http://bmfw.www.gov.cn/bjww/interface/interfaceJson'
#获取北京市所有区
def get_area():
   aa = get_params(flag=1, param=None)
   print(aa)
   # resp = requests.post(json_url, json=json.dumps(params), headers=headers)
   # print(resp)


def get_params(flag, param):
    f = open("D:\\pyproject\\PythonLearn\\爬虫\\gov\\a.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    ctx = execjs.compile(htmlstr)  # 加载JS文件
    jsdata = ""
    if flag ==1:
        jsdata = ctx.call('ajaxGetCity')
    if flag ==2:
        jsdata = ctx.call('ajaxGetCityBlocks', param)
    if flag ==3:
        jsdata = ctx.call('ajaxGetCityIllLevel', param)
    return jsdata


if __name__ == '__main__':
    get_area()