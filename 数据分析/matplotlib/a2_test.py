import matplotlib.pyplot as plt
import random

#折线图绘制与显示
#随机生产数据 温度范围15--18度，一个小时内的温度数据
x = range(60)
y = [random.uniform(15, 18) for i in x]

plt.figure()
plt.plot(x, y)
plt.show()


