#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
错误与异常
错误一般指系统错误、内存溢出等现象
异常一般指程序异常，比如参数错误、代码逻辑错误等

"""
while True:
    try:
        a = int(input("please input a number"))
        b = int(input("please inpit another number"))

        print(a/b)
    except:
        print("请输入正整数")
        continue


    else:
        print("输入数字正常")
        break

    finally:
        print("end！")
    

"""
自定义异常，raise
"""

c = int(input("please input a number"))
if c>10:
    raise Exception("this is a exception")
else:
    print(c)

class MyException(Exception):
    def __init__(self, value1,value2) :
        self.value1 = value1
        self.value2 = value2
raise MyException("value1","value2")









