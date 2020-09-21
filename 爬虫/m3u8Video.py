import requests
import re
import os
import shutil
import math
from multiprocessing.dummy import Pool

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}

def dowload_data(data_url):
    data = requests.get(data_url)
    name = data_url[-9:]
    with open('.\\bak\\' + name, 'wb') as code:
        code.write(data.content)
    per = math.floor(abs(int(name[:-3])) * 100 / int(len(dow_list)))
    print('已经下载： '+str(per) + '%')

def merge_movie(name, movie_name):
    name = name[-9:]
    with open('.\\bak\\' + name, 'rb') as code:
        data = code.read()
    with open(movie_name + '.ts', 'ab') as code:
        code.write(data)
        data = None

if __name__ == '__main__':
    dow_list = []
    target = input('输入地址： ')
    movie_name = input('输入电影名称： ')
    os.makedirs('bak') if os.path.exists('bak') == False else None
    index_req = requests.get(url=target, headers=headers)
    index_url = target[:-10] + index_req.text.split()[2]
    file_req = requests.get(url=index_url, headers=headers)
    file_name_list = re.findall(',([\W\w]*?).ts', file_req.text)
    for i in file_name_list:
        file_name = str(i).replace('\n', '') + '.ts'
        dowload_url = index_url[:-10] + file_name
        dow_list.append(dowload_url)
    pool = Pool(44)
    pool.imap(dowload_data, dow_list)
    pool.close()
    pool.join()
    print('电影合并中...请等待...')
    for i in dow_list:
        merge_movie(i, movie_name)
    shutil.rmtree('bak')
    print('电影下载完成...')

