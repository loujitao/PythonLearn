import numpy

# Ndarray 对象
'''
N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
ndarray 对象是用于存放同类型元素的多维数组
'''

'''
一、构建对象，参数含义
    object	数组或嵌套的数列
    dtype	数组元素的数据类型，可选
    copy	对象是否需要复制，可选
    order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）, k
    subok	默认返回一个与基类类型一致的数组
    ndmin	指定生成数组的最小维度
n_arr = numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)    
'''
a = numpy.array([1,2,3],dtype=int,copy = False, order = 'C', ndmin = 1)
print (a)
a = numpy.array([1,2,3],dtype=int, order = 'C', ndmin = 2)
print (a)
a = numpy.array([1,2,3],dtype=complex, order = 'F', ndmin = 1)
print (a)