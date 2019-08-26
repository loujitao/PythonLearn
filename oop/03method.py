class User:
    @staticmethod       #定义静态方法
    def say_hello():
        print("hello!")

    def play(self,sprot):  #定义实例对象方法
        print(sprot)

    # 初始化方法，并不是构造方法，进行变量初始化操作      最好用可变参数的方式*args，只能有一个
    def __init__(self,name='steve',age=0,sex='男'):
        self.name =name
        self.age  =age
        self.sex  =sex
        print("实例构造完后，调用了初始化方法！")

    @classmethod            #类方法
    def getinstance(cls,**args):
        name = args.get("name","007")
        age = args.get("age",32)
        sex = args.get("sex","男")
        return cls(name,age,sex)

u= User()
print("====== 静态方法调用方式 ======")
u.say_hello()
User.say_hello()
print("====== 实例对象方法调用方式 ======")
u.play("pingpangbar")
print("====== 类方法调用方式 ======")
u2= User.getinstance(name="Tom",age=6,sex="男")


