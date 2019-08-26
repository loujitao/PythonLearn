#python的多态是根据参数类型，来确定执行方法
# 原理是，方法A传入的参数是什么类型，就执行该类型实例下的方法A。不同类的方法A有不同的实现方式
str="sssss"
list=["221","edse","ewew","21345"]
set={1,3,5,8,4}

print(type(str))
print(len(str))
print(type(list))
print(len(list))
print(type(set))
print(len(set))

#自己定义类，重写len方法
class MyLen:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __len__(self):
        return int(self.a+self.b)
l=MyLen(2,4)
print(len(l))  #这次传入自定义对象
