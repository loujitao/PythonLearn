from selenium  import webdriver
from selenium.webdriver.chrome.options import Options
import time
import  logging     #日志模块
logger=logging.getLogger("__name__")

#驱动版本要跟谷歌浏览器版本对应，没有对应的选择相近版本的也行  可以配置到环境的path中，那样就不需要指定了
# driver_dir="D:\pyproject\PythonLearn\driver\chromedriver.exe"
#加载浏览器的驱动
# driver = webdriver.Chrome(driver_dir)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 不打开浏览器执行
driver = webdriver.Chrome(chrome_options=chrome_options)
#目录页url
index_url = 'https://www.biqukan.com/1_1496/'
#用作拼接章节页时，补充的前置域名
base_url = 'https://www.biqukan.com/'

#获取目录页的 a标签： 带了href的url和txt章节名
def get_urls(url):
    #让浏览器访问目录页
     html= driver.get(url)
    #爬取目录页的所有A标签
     links=driver.find_elements_by_css_selector('.listmain dd a')
     return links

def get_txtcontent(url):
    #让页面刷新到章节页
     html= driver.get(url)
    #获取章节的标题做文件名
     link=driver.find_elements_by_css_selector('.content h1')
     title=link[0].get_attribute("textContent")
    #获取章节的内容文本
     txts=driver.find_elements_by_css_selector('.showtxt')
     word=txts[0].get_attribute("textContent")
    #保存文件
     with open("D:\\pyData\\xiaoshuo\\%s.txt" % title, "w", encoding="utf-8") as f:
         word.replace('\xa0'*8,u'')
         f.write(word)  # 写入
         f.write('\n')

if __name__ == '__main__':
    try:
        allurl= get_urls(index_url)
        #拿到目录页的href放到list集合中
        arr=list()
        for link in allurl:
            url=link.get_attribute("href")
            arr.append(url)
        #便利集合，去爬取每个章节页，并保存到本地文本TXT
        for u in arr:
            get_txtcontent(u)
            #休息3S，防止页面没刷新完全，或者访问频繁被网站拦截IP
            time.sleep(3)
    except:
        logger.error("========")



