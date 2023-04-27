#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
类和对象
类变量
类方法
普通函数（类方法比普通函数需要多一个self 参数）


"""

# 定义一个类
class Person():
    # 类的属性
    name = "lily"
    # 类的方法
    def get_name(self):
        return self.name

print(Person.name)

# 实例化一个对象
p = Person()
print(p.name)
print(p.get_name())

# 修改已经实例化对象的名字，类的名字不会变
p.name = "Lilei"

print(p.name)
print(p.get_name())
print(Person.name)

# 只修改类中属性的名字，不修改实例化对象的名字，实例化对象的名字会一起改变
# 实例化一个新的对象
p1 = Person()
Person.name = "Jerry"
print(p1.name)
print(Person.name)

# 如果类和实例化对象均修改，以实例化对象的为准

p2 = Person()
p2.name = "Tom"
Person.name = "Jerry"
print(p2.name)
print(Person.name)




