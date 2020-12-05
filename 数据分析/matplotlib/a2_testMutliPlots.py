import matplotlib.pyplot as plt
import random

#折线图绘制与显示
#随机生产数据 温度范围15--18度，一个小时内的温度数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(9, 11) for i in x]

# plt.figure()
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,8), dpi=80)

#绘制图像
axes[0].plot(x, y_shanghai, label="shanghai")
axes[1].plot(x, y_beijing, label="beijing")

axes[0].legend()
axes[1].legend()

plt.show()


