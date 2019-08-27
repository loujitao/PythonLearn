# try...except语句如果没有抛出异常，就执行else语句。如果有异常就不走else语句
try:
    x = 100
    y= int(input("请输入除数："))
    z = x/y
except ValueError as e:
    print("输入的不是数字！")
except ZeroDivisionError as e :
    print("除数为0")
else:
    print("程序正常结束！")