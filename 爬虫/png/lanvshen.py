#!/usr/local/Cellar/python/3.7.3/bin
# -*- coding: UTF-8 -*-
# https://www.lanvshen.com
import sys,requests,re,time,random
from bs4 import BeautifulSoup
sys.path.append("/Python")
import conf.mysql_db as mysqldb
layout_count = 1
image_count = 1
#查找每套图集信息
def get_layout(url,layout_tablename):
    global layout_count
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
    try:
        for ul1 in soup.find_all(class_='hezi'):
            for ul2 in ul1:
                if(str(ul2).strip()):
                    for li in ul2:
                        if (str(li).strip()):
                            layout_url = li.a['href']
                            cover_url = li.img['src']
                            layout_nums = re.findall('(\d+)', li.span.string)[0]
                            layout_name = li.find_all("p", class_="biaoti")[0].a.string
                            print('第'+str(layout_count)+'套写真:'+layout_name+"　url:"+layout_url)
                            # print('写真集:'+layout_name+'　图片数:'+str(layout_nums)+'　链接:'+cover_url)
                            sql = "insert into "+layout_tablename+"(ID,picname,girlname,picpath,imageid,flodername) values (" +\
                                  str(layout_count)+ ",'" + layout_url + "','" + layout_name + "','"+cover_url+"',"+str(layout_nums)+",'" + layout_name + "')"
                            db.execute(sql)
                            layout_count=layout_count+1
    except Exception as e:
        print('Error',e)
    db.close()

#查找套图内的每张图片信息
def get_images(image_tablename,pic_nums,pic_title,url):
    global image_count
    global layout_count
    url_num = re.findall('(\d+)', url)[0]
    db = mysqldb.Database()
    for i in range(1, int(pic_nums)):
        pic_url = 'https://img.hywly.com/a/1/' + url_num + '/' + str(i) + '.jpg'
        sql = "insert into "+image_tablename+"(id,imageid,flodername,imagepath) " \
              "values (" + str(i) + ","+str(image_count)+",'" + pic_title + "','" + pic_url + "')"
        db.execute(sql)
        print('第'+str(layout_count)+'套写真,第'+str(i)+'张图片:'+pic_title+'　url:'+pic_url)
        image_count = image_count + 1
    db.close()

#判断网页是否存在
def get_html_status(url):
    req = requests.get(url).status_code
    if(req == 200):
        return True
    else:
        return False

def  main():
    global layout_count
    url='https://www.lanvshen.com/s/16/'
    layoyt_name = '蕾丝美女'
    layout_tablename = 'pc_dic_'+'leisi'
    image_tablename = 'po_'+'leisi'

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

    #找出写真集的每套图集信息，插入数据库
    get_layout(url,layout_tablename)
    for i in range(1,100):
        urls = url + 'index_'+str(i)+'.html'
        # urls = url +str(i)+'.html'
        if(get_html_status(urls)):
            get_layout(urls,layout_tablename)
            time.sleep(random.randint(1, 3))
        else:
           break

    #找出图集中的每张图片，插入数据库
    layout_count = 1
    db = mysqldb.Database()
    sql = 'select * from '+layout_tablename+' order by ID'
    results = db.fetch_all(sql)
    for row in results:
        get_images(image_tablename,row['imageid'],row['flodername'],row['picname'])
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