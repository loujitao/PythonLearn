
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print( path + ' 目录已存在')
        return False

import re
import requests
from bs4 import BeautifulSoup
url="https://www.duotoo.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
file_dir="F:\\pyData\\tupian\\duotuwang\\"


#找出所有分类url和分类名称
def  get_tagUrl():
    r = requests.get(url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")
    # 1) 下拉标签部分url
    tag=sp.select("#footer > div > dl > dd > a")
    # 构建一个tuple的集合
    tag_list = []
    for a in tag:
      # 3）获取套图的url
      a_href=a["href"]
      # 4）获取套图的名称
      a_text=a.get_text()
      dir_Name = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", a_text)
      # print(a_href +" : "+a_text)
      tag_list.append((a_href,dir_Name))
    return tag_list

#找出分类下的最大页数
def get_maxPage(list_url):
    r = requests.get(list_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")
    # 1) 先拿到页脚列表  找出最大页
    page=sp.select("#RightArticle > div.pages > ul > a")
    max_page=page[-1]["href"]
    page=re.findall(r'\d+', max_page)
    # print(page)
    return  page[0]

#获取这个分类下的列表url集合
def get_taglist(list_url):
    r = requests.get(list_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")

    #构建一个tuple的集合
    tup_list=[]
    #2) 获取套图标题作为文件目录
    a_list=sp.select("#imgList > ul > li > a")

    for a in a_list:
      # 3）获取套图的url
      a_href=a["href"]
      # 4）获取套图的名称
      a_text=a["title"]
      dir_Name = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", a_text)
      print(a_href +" : "+a_text)
      tup_list.append((a_href,dir_Name))
    # print(tup_list)
    return tup_list


#获取单个套图最大页数
def get_jpg_pages(jpg_url):
    r = requests.get(jpg_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")
    # 1) 先拿到页脚列表  找出最大页
    page=sp.select(".pages > ul > li > a")
    max_page=page[-2].getText()
    return  max_page


#获取人物图片     保存      翻页
def  get_jpg(url,dirName):
    r=requests.get(url,headers)
    r.encoding = 'utf-8'
    # print(r.text)
    imgs=BeautifulSoup(r.text,"html.parser")
    fileDir=file_dir+dirName
    mkdir(fileDir)
    # 拿到URL，或者下载图片
    img=imgs.select("#ArticlePicBox > p > img")

    #图片url
    img_url=img["src"]
    jpg=requests.get(img_url)
    #截取获取图片名
    name=img_url.split("/")[-1]
    print("图片名为："+name)
    # 打开文件，保存文件
    with open(fileDir+"\\"+name,"wb+") as file:
        file.write(jpg.content)





if __name__ == '__main__':
    #获取标签的栏目url
    tag_list= get_tagUrl()
    for t in tag_list:
        index_url=t[0]
        index_dir=t[1]
        file_dir = file_dir + index_dir+"\\"
        mkdir(index_dir)
        #获取分类的总页数url集合
        page=get_maxPage(url+"/weimeitupian/")
        i=1
        while i <= int(page):
            list_url = url + "/weimeitupian/"
            if i>1:
                list_url=url+"/weimeitupian/index_{}.html".format(i)
            print(list_url)
            i=i+1
            #获取单页url中的url_list
            tup_list=get_taglist(list_url)
            for t in tup_list:
                href=t[0]
                name=t[1]
                jpg_url=url+href
                p=get_jpg_pages(jpg_url)
                j=1
                while j<= int(p):
                    if j>1:
                        xurl="_{}.html".format(j)
                        jpg_url=jpg_url.replace(".html",xurl,1)
                        print(jpg_url)
                    get_jpg(jpg_url, name)


