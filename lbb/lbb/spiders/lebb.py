# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from copy import deepcopy

class LebbSpider(scrapy.Spider):
    name = 'lebb'
    allowed_domains = ['www.lebanban.com']
    start_urls = ['https://www.lebanban.com/course/search?categoryId=70777&courseType=1']
    # https: // www.lebanban.com / course / play.json?traceId = 58654858722
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'gr_user_id=2f7803aa-f705-46d1-a630-b921ab41d1cb; grwng_uid=b7f1fe7e-4dce-46ac-a01d-b67a0ca97301; 9d87731c1dfe530f_gr_last_sent_cs1=f4ca91a77f69ba39; _fecdn_=1; UniqueKey=3a24e8598df455bc; lebanban_auth=dct3%2FBYC6PYKBMSFiuyXvRaPkoiQudcPEYmuCXkBu4c9nzx0QILggMIOga6P7tpNq6xsr8XlstvZCeykVJsuQXKxnFG1uu9BW2zYoU7dLsQoFvgOsiPZcXoOUI%2FaFc1NjEoJ; fb_auth=a0b979f81ae8ba3700eb4d7edadfa0a73355f91057c096ea45d297b2fa78447da33f7f3b54c052e27fb4844bc4d6381076b7cd130a7f9766; 9d87731c1dfe530f_gr_session_id=9f507a04-e184-4adb-90aa-a042aee2a808; 9d87731c1dfe530f_gr_last_sent_sid_with_cs1=9f507a04-e184-4adb-90aa-a042aee2a808; 9d87731c1dfe530f_gr_session_id_9f507a04-e184-4adb-90aa-a042aee2a808=true; 9d87731c1dfe530f_gr_cs1=f4ca91a77f69ba39; JSESSIONID=2CF3F07A6AE5DDB4F74D2AFCB7612AB7',
        'Host': 'www.lebanban.com',
        'Referer': 'https://www.lebanban.com/course/search?categoryId=70777&courseType=1',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    def start_requests(self):
        cookies = "gr_user_id=2f7803aa-f705-46d1-a630-b921ab41d1cb; grwng_uid=b7f1fe7e-4dce-46ac-a01d-b67a0ca97301; 9d87731c1dfe530f_gr_last_sent_cs1=f4ca91a77f69ba39; _fecdn_=1; 9d87731c1dfe530f_gr_session_id=5ac63583-e0b3-4946-8fa5-0c53d83f2831; 9d87731c1dfe530f_gr_last_sent_sid_with_cs1=5ac63583-e0b3-4946-8fa5-0c53d83f2831; 9d87731c1dfe530f_gr_session_id_5ac63583-e0b3-4946-8fa5-0c53d83f2831=true; UniqueKey=3a24e8598df455bc; lebanban_auth=dct3%2FBYC6PYKBMSFiuyXvRaPkoiQudcPEYmuCXkBu4c9nzx0QILggMIOga6P7tpNq6xsr8XlstvZCeykVJsuQXKxnFG1uu9BW2zYoU7dLsQoFvgOsiPZcXoOUI%2FaFc1NjEoJ; fb_auth=a0b979f81ae8ba3700eb4d7edadfa0a73355f91057c096ea45d297b2fa78447da33f7f3b54c052e27fb4844bc4d6381076b7cd130a7f9766; 9d87731c1dfe530f_gr_cs1=f4ca91a77f69ba39; JSESSIONID=3B87E9541B1E0EE47C22339A02226886"
        cookies = { i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback = self.parse,
            cookies = cookies
        )

#获取列表页数据
    def parse(self, response):
        list_tmp = 'https://www.lebanban.com/course/search.json?categoryId=70777&pageSize=20&curPage={}&courseType=1&traceId=67144343733'
        for i in range(1,6):
            list_url = list_tmp.format(i)
            html = requests.get(list_url, headers=self.headers)
            data = json.loads(html.text)
            # print(len(data['data']['dataList']))
            list = data['data']['dataList']
            for a in list:
                item = {}
                item['teacher'] = a['lecturerTag']
                url = a['url']
                yield scrapy.Request(
                    url,
                    callback=self.detail_parse,
                    meta={"item": deepcopy(item)}
                )

    def detail_parse(self, response):
        item = response.meta["item"]
        print(item)