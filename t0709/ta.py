import requests
import json
import time
import hashlib

base_url = 'http://bmfw.www.gov.cn/bjww/interface/interfaceJson'

headers ={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '247',
'Content-Type': 'application/json; charset=UTF-8',
'Referer': 'http://bmfw.www.gov.cn/yqfxdjcx/index.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'x-wif-nonce': 'QkjjtiLM2dCratiA',
'x-wif-paasid': 'smt-application',
'x-wif-signature': '',
'x-wif-timestamp': ''
}
#
# params = {
#     'paasHeader': 'zdww',
#     'timestampHeader': '',
#     'nonceHeader': 'nonce',
#     'appId': 'NcApplication',
#     'signatureHeader':'',
#     'key':''
# }

def get_provience():
    timestamp = round(int(time.time()))
    p={ 'key': 'cd4faa2f4c0bdeb4cfd6093769f36482',
        'flag': '11'
    }
    timestamp = str(timestamp)
    headers['x-wif-timestamp'] = timestamp
    headers['x-wif-signature'] = get_sha256(timestamp + 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvC' + 'QkjjtiLM2dCratiA' + timestamp)
    # print(headers)
    data = param_toJsonStr(p,timestamp)
    # print(data)
    resp = requests.post(base_url,data=data,headers=headers)
    print(resp.text)


def get_city(city_code):
    timestamp = round(int(time.time()))
    p = {'key': '8bdd05700ef165746baeca0ae1ef13fc',
         'city_codes': [city_code]
         }
    timestamp = str(timestamp)
    headers['x-wif-timestamp'] = timestamp
    headers['x-wif-signature'] = get_sha256(timestamp + 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvC' + 'QkjjtiLM2dCratiA' + timestamp)
    # print(headers)
    data = param_toJsonStr(p, timestamp)
    # print(data)
    resp = requests.post(base_url, data=data, headers=headers)
    print(resp.text)


def get_area(area_code ):
    timestamp = round(int(time.time()))
    p = {'key': '17487fec8650a09761f93810819abe86',
         'area_code': area_code
         }
    timestamp = str(timestamp)
    headers['x-wif-timestamp'] = timestamp
    headers['x-wif-signature'] = get_sha256(timestamp + 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvC' + 'QkjjtiLM2dCratiA' + timestamp)
    # print(headers)
    data = param_toJsonStr(p, timestamp)
    # print(data)
    resp = requests.post(base_url, data=data, headers=headers)
    print(resp.text)

def param_toJsonStr(p,timestamp):
    token = '23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA'
    nonce = '123456789abcdefg'
    signa = get_sha256(timestamp + token + nonce + timestamp)
    data ={
        'paasHeader': 'zdww',
        'timestampHeader': timestamp,
        'nonceHeader': nonce,
        'appId': 'NcApplication',
        'signatureHeader': signa,
        'key':''
    }
    return json.dumps(dict(data, **p))


def get_sha256(string):
    hsobj = hashlib.sha256()
    hsobj.update(string.encode("utf-8"))
    return hsobj.hexdigest().upper()

if __name__ == '__main__':
    # get_provience()
    get_area("110101")
