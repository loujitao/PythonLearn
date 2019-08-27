import sys
try:
   raise ValueError("输入的不是数字！")  #手动抛出数值错误异常
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])


print("=========  抛出自定义异常  ============")
# 继承Exception异常类
class MyError(Exception):
    def __init__(self, errormsg):
        self.value = errormsg
    def __str__(self):
        return self.value

try:
   raise MyError("这是自定义的异常！")  #手动抛出自定义异常
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
