import requests
import json

url="https://www.lebanban.com/course/play.json" #action属性
params={
    "videoId":'907839', #input标签下的name
    # "videoId":'1264559', #input标签下的name
    "browserType":'4' #input标签下的name
}
headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Connection': 'keep-alive',
'Content-Length': '29',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'gr_user_id=2f7803aa-f705-46d1-a630-b921ab41d1cb; grwng_uid=b7f1fe7e-4dce-46ac-a01d-b67a0ca97301; 9d87731c1dfe530f_gr_last_sent_cs1=f4ca91a77f69ba39; _fecdn_=1; 9d87731c1dfe530f_gr_session_id=3db9b42c-0174-405e-92b2-792c1b4de13d; 9d87731c1dfe530f_gr_last_sent_sid_with_cs1=3db9b42c-0174-405e-92b2-792c1b4de13d; 9d87731c1dfe530f_gr_session_id_3db9b42c-0174-405e-92b2-792c1b4de13d=true; UniqueKey=3a24e8598df455bc; lebanban_auth=IpR8%2FRYC6PYKBMSFiuyXvRaPkoiQudcPEYmuCXkBu4c9nzx0QILggMIOga6P7tlN961sr8XlstjUBeelVZoqQnKxnFG1uu9BW2zYokfSLsQoFvgOsiPZcXoOUI%2FaFc1NjEoJ; fb_auth=a0b979f81ae8ba3700eb4d7edadfa0a73355f91057c096ea45d297b2fa78447da33f7f3b54c052e2199e87f10fa55f710079e9a87f8a49ee; JSESSIONID=9399D16E194AB4F945D6976947332C18; 9d87731c1dfe530f_gr_cs1=f4ca91a77f69ba39',
'Referer': 'https://www.lebanban.com',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'X-Requested-With': 'XMLHttpRequest'
}

if __name__ == '__main__':
    html=requests.post(url,data=params,headers=headers)
    data = html.text
    print(data)
    djson = json.loads(data)
    print(djson['data']['url'])