import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'Host': 'www.3btjia.com',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
}
#爬取新上映电影第三方资源bt
txt = "http://www.3btjia.com/attach-download-fid-9-aid-14288.htm"

if __name__ == '__main__':
    # html = requests.get(txt, headers=headers)
    response = requests.get(txt, headers=headers, allow_redirects=False)
    print(response.headers['Location'])  # 打印响应的状态码
