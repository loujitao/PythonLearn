#coding=utf-8
#============习题1：
    # 列表
# a = [11,22,24,29,30,32]

    # 1 把28插入到列表的末端
# a.append(28)

    # 2 在元素29后面插入元素57
# a.insert(a.index(29)+1,57)

    # 3 把元素11修改成6
# a[a.index(11)]=6

    # 3 删除元素32
# a.remove(32)

    # 4 对列表从小到大排序
# a.sort()
# a.sort(reverse=True)

# print(a)

#==============习题2：
   # 列表
# b = [1,2,3,4,5]

    # 1 用2种方法输出下面的结果：
    # [1,2,3,4,5,6,7,8]

# b.append(6)
# b.append(7)
# b.append(8)
# print(b)

# b.extend([6,7,8])
# print(b)

    # 2 用列表的2种方法返回结果：[5,4]
# print(b[-1:-3:-1])

    # 3 判断2是否在列表里
# print( 2 in b)

##================习题3：
# b = [23,45,22,44,25,66,78]
    # 用列表解析完成下面习题：
#           列表推导式:   [ 含变量1表达式  for  变量1  in  列表1 （if  判断表达式 ） ]

    # 1 生成所有奇数组成的列表
# print([x for x in b if x%2==1 ])

    # 2 输出结果: ['the content 23','the content 45']
# print(["the content %d" % x for x in b[:2] ])

    # 3 输出结果: [25, 47, 24, 46, 27, 68, 80]
# print([ x+2 for x in b ])

##=================习题4：
    # 用range方法和列表推导的方法生成列表：   [11,22,33]
# print([x*11 for x in range(1,4) ])

###===============习题5：
    # 已知元组:
# a = (1,4,5,6,7)

    # 1 判断元素4是否在元组里
# print(4 in a)

    # 2 把元素5修改成8    #元组是不可变的，利用list互换
# l=list(a)
# l[2]=8
# print(tuple(l))

###=================习题6：
   # 已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：
# setinfo = set('acbdfem')
# finfo = set('sabcdef')
# print(setinfo)
# print(finfo)
    # 1 添加字符串对象'abc'到集合setinfo
# setinfo.add('abc')
# print(setinfo)

    # 2 删除集合setinfo里面的成员m
# setinfo.remove('m')
# print(setinfo)

    # 3 求2个集合的交集和并集
# print(setinfo & finfo)      #交集
# print(setinfo | finfo)      #并集
# print(setinfo - finfo)      #差集
# print(finfo  -  setinfo)


###==================习题7：
    # 用字典的方式完成下面一个小型的学生管理系统。

    # 1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。 比如定义2个同学：
    ##
    # 姓名：李明，年龄25，考试分数：语文80，数学75，英语85
    # 姓名：张强，年龄23，考试分数：语文75，数学82，英语78
studentinfo={'liming':{'name':'李明','age':25,'grade':{'chinese':80,'math':75,'english':85}}}
# print(studentinfo)
studentinfo['zhangqiang']= {'name':'张强','age':23,'grade':{'chinese':75,'math':82,'english':78}}
print(studentinfo)

    # 2 给学生添加一门python课程成绩，李明60分，张强：80分
# studentinfo['liming']['grade']['python'] = 60
# studentinfo['zhangqiang']['grade']['python'] = 80
# print(studentinfo)

    # 3 把张强的数学成绩由82分改成89分
# studentinfo['zhangqiang']['grade']['math'] = 89
# print(studentinfo['zhangqiang'])

    # 4 删除李明的年龄数据
# del studentinfo['liming']['age']
# print(studentinfo['liming'])

    # 5 对张强同学的课程分数按照从低到高排序输出。
# score = studentinfo['zhangqiang']['grade']
# print(sorted( score.values()))

    # 6 外部删除学生所在的城市属性，不存在返回字符串 beijing
print( studentinfo.pop('city','beijing'))
print(studentinfo)