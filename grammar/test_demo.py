'''
    写一个判断是否是素数的代码
    （素数：只能被1和它本身整除的数）
'''

#键盘录入一个数字
number = int(input("请输入一个数字："))

for i in range(2,number):
    if number % i == 0:
        print(str(number)+"不是素数")
        break
else:
    print(str(number)+"是素数")