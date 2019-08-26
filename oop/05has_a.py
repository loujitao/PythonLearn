class Engine:
    pass

class Liangqu(Engine):
    def __init__(self):
        print("两驱引擎")

class Siqu(Engine):
    def __init__(self):
        print("四驱引擎")
#===================
class Car:
    car_eng= Engine    # 车有一个引擎

class  LiangCar(Car):
     car_eng = Liangqu  # 两驱车有一个两驱引擎
     def __init__(self):
         self.power= self.car_eng() #找类属性的car_eng，实例化对应的Engine对象

class SiCar(Car):
    car_eng = Siqu      # 四驱车有一个四驱引擎
    def __init__(self):
        self.power = self.car_eng()

l= LiangCar()
s= SiCar()

print(type(l.power))
print(type(s.power))
