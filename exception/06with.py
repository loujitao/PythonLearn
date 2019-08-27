#with关键字是一个替你管理实现上下文协议对象的东西,适用于对资源进行访问的场合，
# 确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，
# 比如文件使用后自动关闭、线程中锁的自动获取和释放等
import sys
try:
    with open("a.txt") as f :
        x =int(f.readline())
        y = 100
        z = y/x
except:
    print(sys.exc_info())
#不用考虑流文件、数据库连接池等资源的关闭了，简化了try块的多层嵌套