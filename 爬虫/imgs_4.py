
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
url = "https://www.aitaotu.com/tag/miaotangyinghua.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }

png_headers = {
    'accept': 'image/jpeg,image/*,*/*;q=0.8',
    "Cache-Control": "max-age=86400",
    "Referer": "",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
file_dir = "D:\\pyData\\tupian\\mmshe\\"


#获取人物图片     保存      翻页
def  get_jpg( url ):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    etree = html.etree
    imgs = etree.HTML(r.text)
    dirname = imgs.xpath("//div[@id='photos']/h1/text()")
    dirname = re.sub("[\.\!\/_,:$%^*()+\"\']+|[+——！，：。？、~@#￥%……&*（）]+", "", dirname[0])
    # print(dirname)
    fileDir = file_dir+dirname
    mkdir(fileDir)
    # # 拿到URL，或者下载图片
    img_list = imgs.xpath("//div[@id='big-pic']/p/a/img/@src")[0]
    # print(img_list)
    png_headers["Referer"]=url
    jpg=requests.get(img_list, headers=png_headers, verify=False)
    #截取获取图片名
    name = img_list.split("/")[-1]
    name = re.sub("[\!\/_,:$%^*(+\"\']+|[+——！，：。？、~@#￥%……&*（）]+", "", name)
    # 打开文件，保存文件
    try:
        with open(fileDir+"\\"+name, "wb+") as file:
            file.write(jpg.content)
    except:
        print("========================")
    next_page = imgs.xpath("//div[@class='pages']/ul/li[@class='thisclass']/following-sibling::li[1]/a/@href")
    if (next_page is not None) and (len(next_page) > 0):
        get_jpg("https://www.aitaotu.com" + next_page[0])



def  get_url_List(url):
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    # print(r.text)
    etree = html.etree
    imgs = etree.HTML(r.text)
    m_list = imgs.xpath("//div[@id='mainbody']/ul/li")
    # print(len(m_list))
    for img in m_list:
        page_href  ="https://www.aitaotu.com" +img.xpath("./a[@class='Pli-litpic']/@href")[0]
        # page_title = img.xpath("./a[@class='Pli-litpic']/@title")[0]
        # print(page_title + ":" +page_href )
        get_jpg(page_href)

    next_page = imgs.xpath("//div[@id='pageNum']/span/a[@class='thisclass']/following-sibling::a[1]/@href")
    if (next_page is not None) and (len(next_page) > 0):
            get_url_List("https://www.aitaotu.com" + next_page[0])

if __name__ == '__main__':
    get_url_List(url)



