def my_echo(*params):
    print(type(params))
    if params:
        for i in range(len(params)):
            print("参数"+str(i)+"为："+str(params[i]))
    else:
        print("没有任何参数")


my_echo()
print("===================")
my_echo("AA","BB","CC","DD")

print("===================")
args=("a","b","c","d","e")
my_echo(*args) # tuple unpacking