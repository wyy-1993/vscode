
"""
list.append(x):在末尾添加元素 a[len(a):]=[x]
list.insert(i,x):在给定位置i输入元素x
list.remove(x):移除元素x
list.pop(i):在给定位置删除，如果没有位置，删除最后一个元素
list.sort(key, reverse=False):对列表进行排序
list.reverse():反转数据

"""

"""

list_jane = [1,2,3]
list_jane.append(0)

list_jane.insert(2,12)

list_jane.remove(1)


list_jane.append(0)

list_jane.insert(1,0)


list_new = list_jane.pop(0)

print(list_jane)

print(list_new)

list_jane.reverse()
print(list_jane)
"""


"""
使用for 循环，写平方列表[1,4,9...]
"""
list_dup=[]
for i in range(1,10):
    list_dup.append(i**2)
    i=i+1

print(list_dup)

"""
使用列表推到式
"""
list_dup2 = [i*i for i in range(1,10)]
print (list_dup2)


list_dup3 = []

for i in range(1,10):
    if i!=1:
        list_dup3.append(i**2)
print(list_dup3)


list_dup4 = [i**2 for i in range(1,10) if i!=1]

print(list_dup4)


"""
嵌套循环
"""
list_dup5 = []
for i in range(1,4):
    for j in range(1,4):
        list_dup5.append(i*j)
print(list_dup5)

"""
使用列表推到式写嵌套循环
"""

list_dup6 = [i*j for i in range(1,4) for j in range(1,4)]

print(list_dup6)



