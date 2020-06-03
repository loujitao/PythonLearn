#!/usr/local/Cellar/python/3.7.1/bin
# -*- coding: UTF-8 -*-
import mysql.connector
import logging

# 加入日志
# 获取logger实例
logger = logging.getLogger("dbSql")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s%(levelname)-8s:%(message)s')

#数据库操作类
class Database:
    # 构造函数
    def __init__(self):
        self._dbhost = '113.125.177.146'  # 数据库主机地址
        self._dbuser = 'lanvshen'       # 数据库用户名
        self._dbpassword = 'sMDkix3J32GRykjC'   # 数据库密码
        self._dbname = 'lanvshen'         # 数据库名称
        self._dbcharset = 'utf8'    # 数据库编码
        self._conn = self.connectMysql()
        if (self._conn):
            self._cursor = self._conn.cursor()

    # 数据库连接
    def connectMysql(self):
        conn =False
        try:
            # self._conn = mysql.connector.connect(
            conn = mysql.connector.connect(
                        host=self._dbhost,
                        user=self._dbuser,
                        passwd=self._dbpassword,
                        database=self._dbname,
                        charset=self._dbcharset,
                        )
        except Exception:
            # self._logger.error("connect database failed, %s" % data)
            logger.error("connect database failed!")
            conn =False
        # self._cursor = self._conn.cursor()
        return conn

    # 直接执行SQL语句
    def execute(self, sql):
        flag = False
        if (self._conn):
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception:
                flag = False
                logger.warning("update database exception SQL=" + sql)
        return flag


    # 查询所有数据，带字段名
    def fetch_all(self, sql):
        result = ''
        if (self._conn):
            try:
                self._cursor = self._conn.cursor(dictionary=True)
                self._cursor.execute(sql)
                result = self._cursor.fetchall()
            except Exception:
                result = False
                logger.warning("query database exception SQL=" + sql)
        return result

    # 查询所有数据，不带字段名
    def fetchall(self, sql):
        result = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                result = self._cursor.fetchall()
            except Exception:
                result = False
                logger.warning("query database exception SQL=" + sql)
        return result

    # 查询一条数据，带字段名
    def fetch_one(self, sql):
        result = ''
        if (self._conn):
            try:
                self._cursor = self._conn.cursor(dictionary=True)
                self._cursor.execute(sql)
                result = self._cursor.fetchone()
            except Exception:
                result = False
                logger.warning("query database exception SQL=" + sql)
        return result

    # 查询一条数据，不带字段名
    def fetchone(self, sql):
        result = ''
        if (self._conn):
            try:
                self._cursor.execute(sql)
                result = self._cursor.fetchone()
            except Exception:
                result = False
                logger.warning("query database exception SQL=" + sql)
        return result

    # 关闭数据库连接
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if (self._conn):
            try:
                if (type(self._cursor) == 'object'):
                    self._cursor.close()
                if (type(self._conn) == 'object'):
                    self._conn.close()
            except Exception:
                # self._logger.warn("close database exception, %s,%s,%s" % (data, type(self._cursor), type(self._conn)))
                logger.warning("close database exception,%s,%s" % ( type(self._cursor), type(self._conn)))
        return True
'''
if __name__ == '__main__':
    db = database()
    # sql = 'update bd_ttj set flag=1  where id=6'
    # sql = 'insert into bd_ttj(url,pwd,flag) values(\'3333\',\'sss\',0)'
    sql ='select * from bd_ttj where flag=0 and ID<45'
    result = db.fetch_one(sql)
    print(result)
    db.close()
    # print('aa')
'''