import matplotlib.pyplot as plt
import random

#折线图绘制与显示
#随机生产数据 温度范围15--18度，一个小时内的温度数据
x = range(60)
y_shanghai = [random.uniform(15, 18) for i in x]
y_beijing = [random.uniform(9, 11) for i in x]

# plt.figure()
'''    多个子图
matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, 
                squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
nrows：默认为 1，设置图表的行数。
ncols：默认为 1，设置图表的列数。
sharex、sharey：设置 x、y 轴是否共享属性，默认为 false，可设置为 'none'、'all'、'row' 或 'col'。
        False 或 none 每个子图的 x 轴或 y 轴都是独立的，True 或 'all'：所有子图共享 x 轴或 y 轴，
        'row' 设置每个子图行共享一个 x 轴或 y 轴，'col'：设置每个子图列共享一个 x 轴或 y 轴。
squeeze：布尔值，默认为 True，表示额外的维度从返回的 Axes(轴)对象中挤出，对于 N*1 或 1*N 个子图，
        返回一个 1 维数组，对于 N*M，N>1 和 M>1 返回一个 2 维数组。如果设置为 False，
        则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1。
subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
**fig_kw：把详细的关键字参数传给 figure() 函数                
'''
figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(20,8), dpi=80)

#绘制图像
axes[0].plot(x, y_shanghai, label="shanghai")
axes[1].plot(x, y_beijing, label="beijing")

axes[0].legend()
axes[1].legend()

plt.show()


