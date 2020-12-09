import numpy
import matplotlib.pyplot as plt

# 数据为两列逗号分隔的多行小数
p = numpy.genfromtxt('data.csv', delimiter=',')
#  查看所有数据
p[0,0]

# 提取每列的数字
# 第一列
x = p[:, 0]
# 第二列
y = p[:, 1]

#用plt画出散点图
# plt.scatter(x,y)
# plt.show()

# 2）定义损失函数
def compute_cost(w,b,p):
    total = 0
    M = len(p)
    #逐点计算平方误差，然后求平均数
    for i in range(M):
        x = p[i, 0]
        y = p[i, 1]
        total += (y -w * x -b) ** 2
    return  total/M

# 3)定义拟合函数
def average(data):
    sum = 0
    num = len(data)
    for i in range(num):
        sum += data[i]
    return sum/num

#4) 定义核心拟合函数
def fit(p):
    M = len(p)
    x_bar = average(p[:, 0])

    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0

    for i in range(M):
        x = p[:, 0]
        y = p[:, 1]
        sum_yx += y * (x - x_bar )
        sum_x2 += x **2
    w = sum_yx / ( sum_x2 - M * (x_bar ** 2) )

    for i in range(M):
        x = p[:, 0]
        y = p[:, 1]
        sum_delta += (y - w * x)
    b = sum_delta / M
    return  w, b

# 测试
w , b =fit(p)
print("w = ", w)
print("b = ", b)

cost = compute_cost(w,b, p)
print("cost =", cost)

# 画出拟合曲线
plt.scatter(x,y)
k = w * x + b
plt.plot(x, k, c='r')
plt.show()