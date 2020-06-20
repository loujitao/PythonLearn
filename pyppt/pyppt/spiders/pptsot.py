# -*- coding: utf-8 -*-
import scrapy
import execjs
import json
import requests

class PptsotSpider(scrapy.Spider):
    name = 'pptsot'
    allowed_domains = ['ppt.sotary.com']
    # start_urls = ['http://ppt.sotary.com/web/wxapp/index.html']
    start_urls = ['http://ppt.sotary.com/opi/v1/search.ashx?fid=1111111111&size=48&keyword=']
    ctx = None

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "Referer": "http://ppt.sotary.com/web/wxapp/index.html"
        }

    def __init__(self, name=None, **kwargs):
        jsstr = self.get_js()
        self.ctx = execjs.compile(jsstr)  # 加载JS文件

    def parse(self, response):
        txt = response.text
        jsdata = self.ctx.call('Codage2025.decode', txt)
        # jsdata = self.get_des_psswd(txt)
        jsRes = json.loads(jsdata)
        rows = jsRes.get("rows")
        # print(rows)
        for element in rows:
            item = {}
            item['name'] = element.get("name")
            item['filepath'] = [element.get("filepath")]
            yield item
        if len(rows) != 0:
            id = rows[len(rows) - 1].get("id")
            print("=========fid:" + str(id))
            nexturl = 'http://ppt.sotary.com/opi/v1/search.ashx?fid={}&size=48&keyword='.format(id)
            yield scrapy.Request(
                nexturl,
                callback=self.parse
            )

    def get_des_psswd(self, data):
        jsstr = self.get_js()
        ctx = execjs.compile(jsstr) #加载JS文件
        return (ctx.call('Codage2025.decode', data))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数

    def get_js(self):
        f = open("D:/pyproject/PythonLearn/pyppt/pyppt/spiders/a.js", 'r', encoding='utf-8') # 打开JS文件
        line = f.readline()
        htmlstr = ''
        while line:
            htmlstr = htmlstr+line
            line = f.readline()
        return htmlstr

