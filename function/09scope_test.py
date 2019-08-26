n= 1
print(n)

if True:
    n=2
print(n)

while True:
    n=3
    break
print(n)
#判断语句和循环语句没有产生新的作用域，都是全局的n
