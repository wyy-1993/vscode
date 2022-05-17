# 定义

dict_1 = {"a":1,"b":2}

dict_2 = dict(a=1,b=2)

print("dict_1",dict_1)
print(type(dict_1))

print("dict_2",dict_2)
print(type(dict_2))


print(dict_1.keys())
print(dict_1.values())

# 返回删除的健值对
print(dict_1.popitem())

# 返回剩余的健值对
print(dict_1)


a = {}
b = a.fromkeys([1,2,3])
print(b)

b = a.fromkeys((1,2,3,4),"test")
print(b)


"""
推导式
"""

print({ i:i*j  for i in range(1,4) for j in range(1,4)})

test = {}
for i in range(1,4):
    for j in range(1,4):
        test[i] = i*j

print(test)

test2={}
for j in range(1,4):
    for i in range(1,4):
        test2[i] = i*j
        # print(test2)
print(test2)




