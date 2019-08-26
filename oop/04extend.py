#python里面有单继承和多继承
class Person:
    p = 11111
    def __init__(self, name):
        self.name = name
        print("Person初始化方法")

class Childen:
    p = 22222
    def __init__(self, sex):
        self.sex = sex
        print("Childen初始化方法")

#单继承的学生类
class  Student(Person):

    def __init__(self,name, id ,age):
        super().__init__(name)  #这里是super()而不是super。
        self.id = id
        self.age = age
        print("Student初始化方法")

#多继承的类
class Son(Person,Childen):

    def __init__(self,name,sex, hobbit):
        Person.__init__(self,name)
        Childen.__init__(self,sex)
        self.hobbit =   hobbit
        print("Son初始化方法")

s= Student("Tom","10010",14)
print(s.name)
print(s.id)
print(s.age)
print("==============")

z= Son("Tim","男","play")
print(z.name)
print(z.sex)
print(z.hobbit)
print(z.p) #两个父类中都有p这个属性，先加载第一个