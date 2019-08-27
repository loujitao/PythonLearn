
while True:
    try:
        x = int(input("请输入一个数字："))
        break
    except ValueError as e:
        print(type(e))
        print(e.args)