

import requests
from bs4 import BeautifulSoup
url="https://www.meitulu.com/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
file_dir="D:\\pyData\\tupian\\"


res=requests.get(url,headers)
soup=BeautifulSoup(res.text,"html.parser")

#下拉标签部分url
#     #tag_ul

fenlei=["https://www.meitulu.com/xihuan/","https://www.meitulu.com/xihuan/rihan",
        "https://www.meitulu.com/xihuan/gangtai","https://www.meitulu.com/xihuan/guochan"]


#第一次遍历  国产分类  拿到国产分类下的url列表     翻页




#第二次遍历  人物分类URL下图片              翻页
def get_personlist(url):
     # 1) 先拿到页脚列表
     #     #pages a

    pass

def  get_jpg(url):
    r=requests.get(url,headers)
    r.encoding = 'utf-8'
    # print(r.text)
    imgs=BeautifulSoup(r.text,"html.parser")
    #获取【 分辨率，模特名，数量】
    # body > div.width > div.c_l > p

    # 【页脚标签】
    # fenxiang > div.fenxiang_l

    # 获取【 标题】
    title_h1 = imgs.select("body > div.width > div.weizhi > h1")
    title=title_h1[0].text
    if title.find("/")>=0:
        title=title.replace("/","_")+"-"
    print(title)
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
        with open(file_dir+title+"_"+name,"wb+") as file:
            file.write(jpg.content)





if __name__ == '__main__':
    u="https://www.meitulu.com/item/22106_{}.html"
    i=2
    while i<=10:
        get_jpg(u.format(i))
        i=i+1
    pass
