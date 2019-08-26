def my_echo(**params):
    print(type(params))
    print(params.get("id",1))
    print(params.get("name","stevetao"))
#使用默认值
my_echo()

#直接指定参数
print("============")
my_echo(id=10,name="john")

#已存在的dictionary传参
print("============")
args={"id":2,"name":"Tom"}
my_echo(**args)

