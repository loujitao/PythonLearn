#在a.txt中分别输入数字、字母、0测试
import  sys

try:
    f =  open("a.txt")
    x = 100
    y = int(f.readline())
    z = x/y
except :
    print(sys.exc_info()[1])  #打印异常的信息
else:
    print("打印出z："+str(z))  #如果没有出异常，打印z的结果
finally:
    print("最后执行了finally语句")
    f.close()                #关闭文件读取流