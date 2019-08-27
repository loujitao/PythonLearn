#1） try except后面跟多个except语句
try:
    x = 100
    y= int(input("请输入除数："))
    z = x/y
except ValueError as e:
    print("输入的不是数字！")
except ZeroDivisionError as e :
    print("除数为0")


# 2） try except后面跟多个error值(tuple结构)
print("========  第二个异常处理结构  =======")
import sys
try:
    a = 100
    b = int(input("请输入除数："))
    c = a / b
except (ValueError,ZeroDivisionError):
    print(sys.exc_info())

