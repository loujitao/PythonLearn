from itertools import  count

# count(2,2)从2开始，步长为2.  无限生成所有的偶数   用break跳出
for i in count(2,2):
    if i > 20:
        break
    print(i)