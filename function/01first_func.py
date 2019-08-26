# 无参无返回值函数， 默认返回值为None
def echo():
    print("test")

# 一个参数一个返回值函数
def my_sum(n):
    s = 0
    i = 1
    while i <= n:
        s += i
        i += 1
    return s

# 两个参数，两个返回值参数  返回值为tuple类型
def my_chu(a , b):
    shang = a // b
    yu = a % b
    return  (shang, yu)

print(my_sum(100))
print(my_chu(23,5))