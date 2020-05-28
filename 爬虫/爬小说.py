from selenium  import webdriver
import time

driver_dir="D:\pyproject\PythonLearn\driver\chromedriver.exe"
driver = webdriver.Chrome(driver_dir)
index_url = 'https://www.biqukan.com/3_3037/'
base_url = 'https://www.biqukan.com/'

def get_urls(url):
     html= driver.get(url)
     links=driver.find_elements_by_css_selector('.listmain dd a')
     return links

def get_txtcontent(url):
     html= driver.get(url)
     link=driver.find_elements_by_css_selector('.content h1')
     title=link[0].get_attribute("textContent")
     txts=driver.find_elements_by_css_selector('.showtxt')
     word=txts[0].get_attribute("textContent")
     with open("D:\\pyData\\xiaoshuo\\%s.txt" % title, "w", encoding="utf-8") as f:  # 格式化字符串还能这么用！
         word.replace('\xa0'*8,u'')
         f.write(word)  # 写入
         f.write('\n')


if __name__ == '__main__':
    try:
        allurl= get_urls(index_url)
        arr=list()
        for link in allurl:
            url=link.get_attribute("href")
            arr.append(url)

        for u in arr:
            get_txtcontent(u)
            time.sleep(3)
    except:
        print("error")



