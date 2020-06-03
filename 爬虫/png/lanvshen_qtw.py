#!/usr/local/Cellar/python/3.7.3/bin
# -*- coding: UTF-8 -*-
# http://www.quantuwang.co
import sys,requests
from bs4 import BeautifulSoup
sys.path.append("/Python")
import conf.mysql_db as mysqldb

image_count = 1
#获取套图下的每套图片信息
def get_photo_info(url,layout_tablename):
    global PhotoNames
    html = get_html(url)
    # html = fread('ttb.html')
    soup = BeautifulSoup(html, "lxml")
    db = mysqldb.Database()
    icount = 1
    for ul in soup.find_all(class_ = 'ul960c'):
        for li in ul:
            if (str(li).strip()):
                PhotoName = li.span.string
                PhotoUrl = li.img['src']
                imageUrl = 'http://www.quantuwang.co'+li.a['href']
                print('第'+str(icount)+'套图:'+PhotoName+'　'+PhotoUrl+'　'+imageUrl)
                sql = "insert into "+layout_tablename+"(picname,girlname,picpath,flodername) values('%s','%s'," \
                      "'%s','%s')" % (imageUrl,PhotoName,PhotoUrl,PhotoName)
                db.execute(sql)
                icount = icount + 1
    db.close()
    return True

#查找套图内的每张图片信息并保存
def get_images(image_tablename,pic_nums,pic_title,url,layout_count):
    global image_count
    db = mysqldb.Database()
    try:
        for i in range(1, int(pic_nums)):
            pic_url = url[:-5] + str(i) + '.jpg'
            sql = "insert into "+image_tablename+"(id,imageid,flodername,imagepath) " \
                  "values (" + str(i) + ","+str(image_count)+",'" + pic_title + "','" + pic_url + "')"
            db.execute(sql)
            print('第'+str(layout_count)+'套写真'+str(image_count)+',第'+str(i)+'张图片:'+pic_title+'　url:'+pic_url)
            image_count = image_count + 1
    except Exception as e:
        print('Error',e)
    db.close()

#获取首页图片信息中的每页链接
def get_image_pages(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")
    # print(html)
    image_pages = []
    image_pages.append(url)
    try:
        for ul in soup.find_all(class_='c_page'):
            for li in ul.find_all('a'):
                image_pages.append('http://www.quantuwang.co/'+li.get('href'))
    except Exception as e:
        print('Error',e)
    return len(image_pages)

#获取网页信息，得到的html就是网页的源代码，传url，返回html
def get_html(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept - Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    }
    resp = requests.get(url,headers=headers)
    resp.encoding='utf-8'
    html = resp.text
    # fwrite(html)
    return html

#处理url
def handle_url(i,url):
    if i == 1:
        return url
    else:
        url = url[:-5] + "_" + format(i) + ".html"
        return url

def main():
    global image_count
    # image_count = 1391
    url = 'http://www.quantuwang.co/t/f4543e3a7d545391.html'
    layoyt_name = '糯美子Mini'
    layout_tablename = 'pc_dic_'+'nuomeizi'
    image_tablename = 'po_'+'nuomeizi'

    #复制表结构
    db = mysqldb.Database()
    try:
        sql = "create table if not exists "+layout_tablename+"(LIKE pc_dic_toxic)"
        db.execute(sql)
        print('创建表:'+layout_tablename)
        sql = "create table if not exists " + image_tablename + "(LIKE po_toxic)"
        db.execute(sql)
        print('创建表:'+image_tablename)
    except Exception as e:
        print('Error',e)
    db.close()

    #第一步：搜索页面信息截取
    get_photo_info(url,layout_tablename)

    #第二步：找出图集中的每张图片，插入数据库
    layout_count = 1
    db = mysqldb.Database()
    sql = 'select * from '+layout_tablename+' where ID>0'
    results = db.fetch_all(sql)
    for row in results:
        # 找出套图信息：图片数量
        imgage_nums = get_image_pages(row['picname']) + 1
        get_images(image_tablename,imgage_nums,row['flodername'],row['picpath'],layout_count)
        layout_count = layout_count + 1
    db.close()

    #更新总表
    db = mysqldb.Database()
    try:
        sql = "select max(imageid) as maxcount from "+image_tablename
        results = db.fetch_one(sql)
        sql = "insert into pc_dic_lanvshen(BeautyName,MinID,MaxID,TableName,IndexName,IndexType) values ('%s',%d,%d,'%s'," \
              "'%s',%d)" % (layoyt_name,1,int(results['maxcount']),image_tablename,layout_tablename,1)
        db.execute(sql)
        print('数据已更新到总表:'+layout_tablename+'　'+image_tablename)
    except Exception as e:
        print('Error',e)
    db.close()


if __name__ == '__main__':
    main()