'''
    循环中的需要做跳出本次循环或者本轮循环
'''

languages = ["C#","java","python","scala","Go" ]
java = "java"
print("======== 1 ============")
# 跳出并结束循环 break
for lang in languages:
    if lang == java:
        break
    print(lang)

print("======== 2 ============")
# 跳出本轮循环 continue
for lang in languages:
    if lang == java:
        continue   
    print(lang)