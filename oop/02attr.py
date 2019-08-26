class User:
    age= 0 #类属性

u1 = User()
u2 = User()

u1.name = 'steve'
u1.age =   27
u2.sex = '男'
u2.name= 'Tim'

print(u1.age)
print(u1.name)
print(u2.age)   # u2没有定义age属性，会使用类属性0
print(u2.sex)
print(u2.name)