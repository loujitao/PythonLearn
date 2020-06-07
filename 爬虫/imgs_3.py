
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
from lxml import html
url="https://smtmm.win"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
file_dir="D:\\pyData\\tupian\\smtmm\\"


#获取人物图片     保存      翻页
def  get_jpg(url):
    r=requests.get(url,headers=headers)
    r.encoding = 'utf-8'
    # print(r.text)
    etree=html.etree
    imgs=etree.HTML(r.text)
    title=imgs.xpath("//div[@class='container']/h1[@class='focusbox-title']/text()")
    dirname = re.sub("[\.\!\/_,:$%^*()+\"\']+|[+——！，：。？、~@#￥%……&*（）]+", "", title[0])
    print(dirname)
    fileDir=file_dir+dirname
    mkdir(fileDir)
    # # 拿到URL，或者下载图片
    img_list=imgs.xpath("//article[@class='article-content']/p/img[1]")
    # print(img_list)

    for img in img_list:
        # print(img.attrib.get("data-original"))
        img_url=img.attrib.get("data-original")
        jpg=requests.get("https://smtmm.win"+img_url,headers=headers,verify=False)
        #截取获取图片名
        name=img_url.split("/")[-1]
        name = re.sub("[\!\/_,:$%^*(+\"\']+|[+——！，：。？、~@#￥%……&*（）]+", "", name)
        print("图片名为："+name)
        # 打开文件，保存文件
        try:
            with open(fileDir+"\\"+name,"wb+") as file:
                file.write(jpg.content)
        except:
            print("========================")




if __name__ == '__main__':
    # https://smtmm.win/article/{52652- 52384}/
    jpg_url="https://smtmm.win/article/{}/"
    j=52616
    while j >=52384:
    # while j >=52652:
        xurl=jpg_url.format(j)
        print(xurl)
        j=j-1
        print(j)
        get_jpg(xurl)



