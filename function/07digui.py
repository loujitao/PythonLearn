'''
    求n个数的阶乘
   1!=  1* 0! =1
   2!=  2* 1! =2*1
   3!=  3* 2! =3*2*1
   n!=  n*(n-1)!
'''

def  fun(n):
    if n ==1 :
        return 1
    else:
        return n * fun(n-1)

print(fun(10))
print(fun(5))