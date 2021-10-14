import matplotlib.pyplot as plt
import matplotlib

#折线图绘制与显示
#1、创建画布  参数：figsize: 图片的长宽， kpi：清晰度
plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 7, 7, 9, 12, 14, 9]
y2 = [3, 6, 11, 14, 15, 12, 9]

#2、绘制图像
'''
颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。
            多条曲线不指定颜色时，会自动选择不同颜色。
线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等
'''
plt.plot(x, y, color='r', linestyle="-.", label="shanghai")

#（可选）双图像直接添加plot
plt.plot(x, y2)
#显示图例  双图像时使用  参数可以指定显示位置（默认右上角）
plt.legend()

'''
Matplotlib 默认情况不支持中文;我们使用思源黑体
GitHub 地址：https://github.com/adobe-fonts/source-han-sans/tree/release/OTF/SimplifiedChinese
可以下载个 OTF 字体，比如 SourceHanSansSC-Bold.otf，
'''
# fname 为 你下载的字体库路径，注意 SourceHanSansSC-Bold.otf 字体的路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

'''
我们可以使用 xlabel() 和 ylabel() 方法来设置 x 轴和 y 轴的标签;
使用 title() 方法来设置标题;
'''
plt.xlabel("x - label")
plt.ylabel("y - label")

# 修改刻度值 根据数据的值范围自己制定步长
# 第一个参数是数值取值， 第二个参数是对应描述
# 中文字体解决： 安装字体、 删除matplotlib缓存文件、配置文件
plt.rcParams['font.sans-serif'] = ['SimHei'] #黑体
x_label = ["周一", "周三", "周五", "周日"]
plt.xticks(x[::2], x_label)
plt.yticks(range(0, 30, 5))

# fontdict 可以使用 css 来设置字体样式
font1 = {'color': 'blue', 'size': 20}
plt.title("xxx一周数据指标折线图", fontproperties=zhfont1, fontdict=font1)

'''
添加网格
b：可选，默认为 None，可以设置布尔值，true 为显示网格线，false 为不显示，
        如果设置 **kwargs 参数，则值为 true。
which：可选，可选值有 'major'、'minor' 和 'both'，默认为 'major'，表示应用更改的网格线。
axis：可选，设置显示哪个方向的网格线，可以是取 'both'（默认），
        'x' 或 'y'，分别表示两个方向，x 轴方向或 y 轴方向。
**kwargs：可选，设置网格样式，可以是 color='r', linestyle='-' 和 linewidth=2，
            分别表示网格线的颜色，样式和宽度。
color：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，
        'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。
linestyle：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
linewidth：设置线的宽度，可以设置一个数字            
'''
plt.grid(linestyle="--", alpha=0.5)

#（可选）图片保存路径，不能放在show()方法之后
#plt.savefig("test.png")

#3、显示图像  会释放数据资源
plt.show()


