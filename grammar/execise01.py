#coding=utf-8
    # 一.已经字符串 s = "i,am,lilei", 请用两种办法取出之间的“am”字符。
# s = "i,am,lilei"
# '''
#     切片方法；
#     split方法;
# '''
# print(s[2:4])
# print(s.split(",")[1])

    # 二.在python中，如何修改字符串？
    # 字符串是不可变序列，重新赋值，更改引用对象。

    # 三.bool("2012" == 2012) 的结果是什么。 False

    # 四.已知一个文件test.txt，内容如下：
    # ____________
    # 2012来了。
    # 2012不是世界末日。
    # 2012欢乐多。
    # _____________

    # 1.请输出其内容。 中文编码问题
# f = open("test.txt","r",encoding="UTF-8")
# content= f.read()
# print(content)

    # 2. 请计算该文本的原始长度。
# print(len(content))

    # 3. 请去除该文本的换行。
# d=  content.replace("\n","")
# print(d)
# print(len(d))

    # 4. 请替换其中的字符  "2012" 为 "2013"。
# rstr= content.replace("2012","2013")
# print(rstr)

    # 5. 请取出最中间的长度为5的子串。 切片法[中间索引:中间索引+5]
# length= len(content)
# print(content[int(length/2):int(length/2 + 5)])

    # 6. 请取出最后2个字符。
# print(content[-2:])
    # 7. 请从字符串的最初开始，截断该字符串，使其长度为11.
# print(content[:12])
    # 8. 请将 {4} 中的字符串保存为test1.py文本.
# w = open("test1.py","w",encoding="UTF-8")
# w .write(rstr)
# w.close()
#
# f.close()
    # 五.请用代码的形式描述python的引用机制。
# import sys
#
# cinfo = '1234'
# print(  id(cinfo))
# print( sys.getrefcount('1234') )
#
# binfo = '1234'  #引用计数加1
# print( id(binfo))
# print( sys.getrefcount('1234'))

    # 六.已知如下代码
    # ________
    #
# a = "中文编程"
# b = a
# c = a
# a = "python编程"
# b = u'%s' % a
# d = "中文编程"
# e = a
# c = b
# b2 = a.replace("中", "中")
    # ________
    #
    # 1. 请给出str对象 "中文编程" 的引用计数
# import sys
# print( sys.getrefcount("中文编程") )

    # 2. 请给出str对象 "python编程" 的引用计数
# print(sys.getrefcount("python编程"))

    # 七.已知如下变量
    # ________
# a = "字符串拼接1"
# b = "字符串拼接2"
    # ________
    #
    # 1. 请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
# c= a +b
# print(c)

# c= '%s%s' % (a,b)         #元组
# print(c)

# c= '%(a)s%(b)s' % {'a':a,'b':b}     #字典
# print(c)

# c= '{a}{b}'.format(a=a,b=b)
# print(c)

# c= "".join([a,b])           #分隔符，list集合
# print(c)

    # 2. 请将a与b拼接成字符串c，并用逗号分隔。
# c= ",".join([a,b])
# print(c)

    # 3. 请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
# print(len(c))
# print(c[6])
    #
    # 八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。
# import  string
# print(help(string))

    # 1. 包含0 - 9 的数字。
# print(string.digits)

    # 2. 所有小写字母。
# print(string.ascii_lowercase)

    # 3. 所有标点符号。
# print(string.punctuation)

    # 4. 所有大写字母和小写字母。
# print(string.ascii_letters)

    # 5. 请使用你认为最好的办法将 {1} - {4} 点中的字符串拼接成一个字符串。
# strlist= []
# strlist.append(string.digits)
# strlist.append(string.ascii_lowercase)
# strlist.append(string.punctuation)
# strlist.append(string.ascii_letters)
# print("".join(strlist))

    # 九.已知字符串
    # ________
    #
# a = "i,am,a,boy,in,china"
    # ________
    #
    # 1. 假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
# a = "i,am,a,{person},in,{address}"
# b= a.format(person='gay',address='USA')
# print(b)

    # 2. 请使用2种办法取出其间的字符 "boy" 和 "china"。
# c= a.split(",")
# print(c[3])
# print(c[5])
#
# print(a[7:10])
# print(a[-5:])

    # 3. 请找出第一个 "i" 出现的位置。 find(sub, start=None, end=None)
# print(a.find("i"))

    # 4. 请找出 "china" 中的 "i" 字符在字符串a中的位置。
# print(a.find("i",a.find("china")))

    # 5. 请计算该字符串一共有几个逗号。
# print(a.count(","))
    #
    # 十.请将模块string的帮助文档保存为一个文件。
# import sys
# import string
#
# f = open('test.log','w')
# sys.stdout = f
# help(string)
# f.close()
