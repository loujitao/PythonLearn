
def my_print(a ,b ,c):
    print("参数a是：" + a)
    print("参数b是：" + b)
    print("参数c是：" + c)

 #位置参数，按照位置传参
my_print("A","B","C")

print("==================")
#关键字参数，按照名称传参
my_print(c="CC",b="BB",a="AA")


#定义一个带默认值的函数
def my_sum(a, b=10):
    return a+b

print(my_sum(1))
print(my_sum(1,2))