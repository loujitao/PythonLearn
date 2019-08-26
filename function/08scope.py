i= 1
j= 1

def fun1():
    i= 2
    global j  #全局作用域修饰词  这里的j是引用外部的j
    j= 2        #赋值会覆盖外部j的值
    def fun2():
        nonlocal i  #临近作用域修饰词  这里的i是引用fun1里的i
        i= 3     #赋值会覆盖fun1中i的值
        j= 3
        print("fun2中的i,j: "+str(i)+","+str(j))
    print("fun1中的i,j: " + str(i) + "," + str(j))
    fun2()
    print("执行fun2方法后，fun1中的i,j: " + str(i) + "," + str(j))

print("全局的i,j: " + str(i) + "," + str(j))
fun1()
print("执行fun1方法后，全局的i,j: " + str(i) + "," + str(j))

