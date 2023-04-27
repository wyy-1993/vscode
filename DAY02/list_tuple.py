# 元组定义
from itertools import count


tuple_1 = (1,2,3)
tuple_2 = 1,2,3

print("tuple_1",tuple_1)
print(type(tuple_1))

print("tuple_2",tuple_2)
print(type(tuple_2))


# 元组不可变性
# 元组中包含列表，就可以变

list_1 = [1,2,3]
list_1[0] = "a"
print(list_1)


# tuple_1[0] = "a"  -- 这样修改会报错

tuple_3 = (1,2,list_1)
print(id(tuple_3[2]))
tuple_3[2][1] = "b"

print(tuple_3)
print(id(tuple_3[2]))


# 元组常用的函数

tuple_4= (1,2,3,"a","a")

print(tuple_4.count("a"))

print(tuple_4.index("a")) # 查找最近的元素索引


