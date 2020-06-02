
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
url="https://www.meitulu.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
file_dir="F:\\pyData\\tupian\\guochan\\"





fenlei=[ "https://www.meitulu.com/xihuan/rihan",
        "https://www.meitulu.com/xihuan/gangtai","https://www.meitulu.com/xihuan/guochan"]


#下拉标签部分url
def  get_tagUrl():
    r = requests.get(url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")
    # 1) 下拉标签部分url
    tag=sp.select("#tag_ul > li > a")
    # 构建一个tuple的集合
    tag_list = []
    for a in tag:
      # 3）获取套图的url
      a_href=a["href"]
      # 4）获取套图的名称
      # a_text=a.get_text()
      # dir_Name = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", a_text)
      # print(a_href +" : "+a_text)
      # tag_list.append((a_href,dir_Name))
      tag_list.append(a_href)
    return tag_list


#第二次遍历  获取总共有多少页              翻页
def get_maxPage(list_url):
    r = requests.get(list_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")

    # 1) 先拿到页脚列表  找出最大页
    page=sp.select("#pages > a")
    max_page=page[-2].getText()
    return  max_page

#第二次遍历  获取单页的列表url集合              翻页
def get_personlist(list_url):
    r = requests.get(list_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")

    #构建一个tuple的集合
    tup_list=[]
    #2) 获取套图标题作为文件目录   body > div.main > div.boxs > ul > li:nth-child(1) > p.p_title > a
    a_list=sp.select("body > div.main > div.boxs > ul > li > p.p_title > a")

    for a in a_list:
      # 3）获取套图的url
      a_href=a["href"]
      # 4）获取套图的名称
      a_text=a.get_text()
      dir_Name = re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", a_text)
      # print(a_href +" : "+a_text)
      tup_list.append((a_href,dir_Name))
    # print(tup_list)
    return tup_list


#获取人物图片最大页数
def get_jpg_pages(jpg_url):
    r = requests.get(jpg_url, headers)
    r.encoding = 'utf-8'
    sp = BeautifulSoup(r.text, "html.parser")

    # 1) 先拿到页脚列表  找出最大页
    page=sp.select("#pages > a")
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
    #获取【 分辨率，模特名，数量】
    # body > div.width > div.c_l > p

    # 【页脚标签】
    # fenxiang > div.fenxiang_l

    # 获取【 标题】
    # title_h1 = imgs.select("body > div.width > div.weizhi > h1")
    # title=title_h1[0].text
    # if title.find("/")>=0:
    #     title=title.replace("/","_")+"-"
    # print(title)
    # 拿到URL，或者下载图片
    img=imgs.select("body > div.content > center > img")

    #将图片url放到列表中
    list1=[]
    for i in img:
        list1.append(i["src"])
    #获取单张图片
    for x in list1:
        jpg=requests.get(x)
        #截取获取图片名
        name=x.split("/")[-1]
        print("图片名为："+name)
        # 打开文件，保存文件
        with open(fileDir+"\\"+name,"wb+") as file:
            file.write(jpg.content)





if __name__ == '__main__':
    print("============  开始下载标签类的套图  ================")
    #获取标签的栏目url
    tag_list= get_tagUrl()
    fenlei= fenlei+tag_list
    # print(fenlei)
    #获取标题栏的四个主栏目
    for index_url in fenlei:
        max_page= get_maxPage(index_url)
        i=1
        tup_list =[]
        while i <= int(max_page):
            if i<=1:
                tup_list = get_personlist(index_url)
            else:
                tup_list=get_personlist(index_url+"/{}.html".format(i))
            i=i+1
            for tup in tup_list:
                (jpg_url ,jpg_name)=tup
                pages=get_jpg_pages(jpg_url)
                j=1
                while j < int(pages):
                    if j <=1:
                        get_jpg(jpg_url, jpg_name)
                    else:
                        str="_{}.html".format(j)
                        get_jpg(jpg_url.replace(".html",str), jpg_name)
                    j=j+1

