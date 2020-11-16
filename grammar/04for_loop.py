languages = ["C#","java","python","scala","Go" ]

print("======== 1 ============")
# for循环用法1   跟序列变量
for lang in languages:
    print(lang)

print("======== 2 ============")
#for循环用法2   直接跟序列
for i in [1,2,3,4,5]:
    print(i)

print("======== 3 ============")
#for循环用法3   根据索引遍历序列
# range(5) => [0,1,2,3,4]  下面是根据序列长度生产索引序列
#range(1,5) = [1,2,3,4]
for i in range(len(languages)):
    print(i,languages[i])

print("======== 4 ============")
#如果两个序列长度相同，需要一起打印，可以借助range
names = ["Alice","Steven","John","Jim","Anna"]
grade = [98,76,82,62,89]
for i in range(len(names)):
    print(names[i], grade[i])

print("======== 5 ============")
#咬合操作 zip()
for names,grade in zip(names,grade):
    print(names,grade)

print("======== 6 ============")
#枚举方法   会自动列举出索引和索引位置元素
for index,item in enumerate(languages):
    print(index,item)
print("======== 7 ============")
namess = {'a':1,'b':2}
for index,item in namess.items():
    print(index,item)