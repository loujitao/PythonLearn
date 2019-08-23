'''
    在python的循环中，如果遍历执行完了，可以执行else语句。
    常用的场景为，一个序列找了一遍，没有发现要找的元素，在else里面给出处理或者提示信息
'''

languages = ["C#","java","python","scala","Go" ]
java = "C++"
print("======== 1 ============")
# 跳出并结束循环 break
for lang in languages:
    if lang == java:
        break
    print(lang)
else:
    print("没有找到结果")

result = "java"
print("======== 2 ============")
# 跳出并结束循环 break
for lang in languages:
    if lang == result:
        break
    print(lang)
else:
    print("没有找到结果")