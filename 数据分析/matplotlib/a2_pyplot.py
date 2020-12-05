import matplotlib.pyplot as plt

#折线图绘制与显示
#1、创建画布  参数：figsize: 图片的长宽， kpi：清晰度
plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 7, 7, 9, 12, 14, 9]
y2 = [3, 6, 11, 14, 15, 12, 9]
#2、绘制图像
plt.plot(x, y, color='r', linestyle="-.", label="shanghai")

#（可选）双图像直接添加plot
plt.plot(x, y2)
#显示图例  双图像时使用  参数可以指定显示位置（默认右上角）
plt.legend()


# 修改刻度值 根据数据的值范围自己制定步长
# 第一个参数是数值取值， 第二个参数是对应描述
# 中文字体解决： 安装字体、 删除matplotlib缓存文件、配置文件
x_label = ["周一", "周三", "周五", "周日"]
plt.xticks(x[::2], x_label)
plt.yticks(range(0, 30, 5))
plt.title("xxx一周数据指标折线图")

#添加网格
plt.grid(linestyle="--", alpha=0.5)

#（可选）图片保存路径，不能放在show()方法之后
#plt.savefig("test.png")

#3、显示图像  会释放数据资源
plt.show()


