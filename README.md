python学习大纲

    1）python安装包与开发工具（3.6.5  pycharm）
         pip install selenium  -i https://pypi.tuna.tsinghua.edu.cn/simple  （清华的）
					              http://pypi.douban.com/simple/ (豆瓣的)

    2）数据结构与流程控制 （grammar）

        数据结构：int,boolean,decimal,string,tuple,list,set,dictionary
        流程控制：if语句，while循环，for循环，break,continue

    3）函数相关（function）

        定义函数；pass关键字；函数参数和返回值；lambda；递归函数；函数中的作用域

    4）面向对象（oop）

        定义类和实例；属性；类中的方法；类的继承；组合has-a有一个；python的多态

    5）异常处理（exception）

        异常处理的简单结构；捕获多种异常；异常处理中的else；finally关键字；raise关键字；with结构

    6)爬虫框架scrapy常用命令：
            创建项目： scrapy startproject pyimgs
            创建一个爬虫：scrapy genspider example example.com
                          scrapy genspider -t crawl  example example.com
            执行：  scrapy crawl smtmm
