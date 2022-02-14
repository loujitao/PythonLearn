
# 设置心形矩阵
import os
import random
import numpy as np
from PIL import Image

FRAME = [[0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]]

# 定义相关参数
SIZE = 100  # 每张图片的尺寸，越大越清晰
N = 2  # 每个点位上放置1*1张图片

# 计算相关参数
width = np.shape(FRAME)[1] * N * SIZE  # 照片墙宽度
height = np.shape(FRAME)[0] * N * SIZE  # 照片墙高度
n_img = np.sum(FRAME) * (N ** N)  # 照片墙需要的照片数
print(n_img)
dir = r'D:\wq/'  # 头像存储目录
filenames = random.sample(os.listdir(dir), n_img)  # 随机选取n_img张照片
filenames = [dir + f for f in filenames]

# 绘制爱心墙
img_bg = Image.new('RGB', (width, height))  # 设置照片墙背景
i = 0
for y in range(np.shape(FRAME)[0]):
    for x in range(np.shape(FRAME)[1]):
        if FRAME[y][x] == 1:  # 如果需要填充
            pos_x = x * N * SIZE  # 填充起始X坐标位置
            pos_y = y * N * SIZE  # 填充起始Y坐标位置
            for yy in range(N):
                for xx in range(N):
                    img = Image.open(filenames[i])
                    img = img.resize((SIZE, SIZE), Image.ANTIALIAS)
                    img_bg.paste(img, (pos_x + xx * SIZE, pos_y + yy * SIZE))
                    i += 1
# 保存图片
img_bg.save('d:/love.jpg')
