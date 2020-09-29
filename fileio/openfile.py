# r 读取
# w 写入
# a 追加

a = open("tmp.txt","w")
a.write("just do test!")
a.close()

c = open("tmp.txt","a")
c.write("\nit is appending context!")
c.close()

b = open("tmp.txt","r")
print(b.read(20))
print("再次读取："+b.read(20))
b.seek(0)                       #游标归0，重新读取
print("第三次读取："+b.read(20))
b.close()