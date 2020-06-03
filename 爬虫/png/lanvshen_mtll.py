#!/usr/local/Cellar/python/3.7.3/bin
# -*- coding: UTF-8 -*-
# https://www.meitulu.com
import sys,requests,time,random,re
from bs4 import BeautifulSoup
sys.path.append("/Python")
import conf.mysql_db as mysqldb
album_count = 1
image_count = 1
#获取套图下的每套图片信息
def get_photo_info(url,layout_tablename):
    global album_count
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    req.encoding = 'utf-8'
    # print(req.text)
    soup = BeautifulSoup(req.text, "lxml")
    db = mysqldb.Database()
    for ul in soup.find_all(class_ = 'img'):
        for li in ul:
            if (str(li).strip()):
                AlbumName = li.img['alt']
                AlbumNums = re.findall(r"\d+\.?\d*", li.p.string)[0]
                AlbumUrl = li.a['href']
                PhotoUrl = li.img['src']
                print('第'+str(album_count)+'套图:'+AlbumName+'　'+AlbumUrl+'　'+PhotoUrl)
                sql = "insert into "+layout_tablename+"(picname,girlname,picpath,imageid,flodername) values('%s','%s','%s','%s')" % (AlbumUrl,AlbumName,PhotoUrl,AlbumNums,AlbumName)
                db.execute(sql)
                album_count = album_count + 1
    db.close()
    return True

#保存每张图片信息
def get_images(image_tablename,image_nums,flodername,image_url,albumID):
    global image_count
    db = mysqldb.Database()
    for i in range(1, int(image_nums)+1):
        image_path = image_url[:-6] + '/' + str(i) + '.jpg'
        sql = "insert into " + image_tablename + "(imageid,flodername,imagepath,id) values('%s','%s','%s','%s')" % (image_count, flodername, image_path, i)
        db.execute(sql)
        print('第'+str(albumID)+'套写真'+str(image_count)+',第'+str(i)+'张图片:'+flodername+'　url:'+image_path)
        image_count = image_count + 1
    db.close()

#判断网页是否存在
def get_html_status(url):
    req = requests.get(url).status_code
    if(req == 200):
        return True
    else:
        return False

def main():
    global album_count
    global image_count
    # image_count = 1391
    url = 'https://www.meitulu.com/t/dingziku/'
    album_name = '丁字裤美女'
    album_tablename = 'pc_dic_'+'dingziku'
    image_tablename = 'po_'+'dingziku'

    #复制表结构
    db = mysqldb.Database()
    try:
        sql = "create table if not exists "+album_tablename+"(LIKE pc_dic_toxic)"
        db.execute(sql)
        print('创建表:'+album_tablename)
        sql = "create table if not exists " + image_tablename + "(LIKE po_toxic)"
        db.execute(sql)
        print('创建表:'+image_tablename)
    except Exception as e:
        print('Error',e)
    db.close()

    #第一步：搜索页面信息截取
    get_photo_info(url,album_tablename)
    for i in range(2,100):
        urls = url +str(i)+'.html'
        # urls = url +str(i)+'.html'
        if(get_html_status(urls)):
            get_photo_info(urls,album_tablename)
            time.sleep(random.randint(1, 3))
        else:
           break

    #第二步：找出图集中的每张图片，插入数据库
    db = mysqldb.Database()
    sql = 'select * from '+album_tablename+' where ID>0'
    results = db.fetch_all(sql)
    for row in results:
        get_images(image_tablename,row['imageid'],row['flodername'],row['picpath'],row['ID'])
    db.close()

    #更新总表
    db = mysqldb.Database()
    try:
        sql = "select max(imageid) as maxcount from "+image_tablename
        results = db.fetch_one(sql)
        sql = "insert into pc_dic_lanvshen(BeautyName,MinID,MaxID,TableName,IndexName,IndexType) values ('%s',%d,%d,'%s'," \
              "'%s',%d)" % (album_name,1,int(results['maxcount']),image_tablename,album_tablename,1)
        db.execute(sql)
        print('数据已更新到总表:'+album_tablename+'　'+image_tablename)
    except Exception as e:
        print('Error',e)
    db.close()


if __name__ == '__main__':
    main()