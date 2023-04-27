#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
import sys,time
from turtle import rt

print(sys.argv)
print(time.localtime())

print("exit")

import numpy

"""


"""

f = open('jane/DAY02/testfile','rt+')

# print(f.read()) # 读取文件所有内容，不适合大容量的文件
print("this is a cutline")

# 每次读取一行，包括换行符
print(f.readline())

# 读取所有的内容，放到列表中：['day02\n', 'day03\n', 'day04,day05\n']
print(f.readlines())

f.close()




with open('jane/DAY02/testfile','rt+') as f:
    # print(f.read())
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break

f.close()

"""

import json

info = [{

            "name":"Tom",
            "gender":"male",
            "age":"12"
        },{
            "name":"Jeery",
            "gender":"male",
            "age":"12"
        }]

# dumps:将python中的字典转换为字符串

# print(type(info))
# data = json.dumps(info,sort_keys=True,indent=4)
# print(data)
# print(type(data))

print("读取并保存到json文件")
json.dump(info, open('jane/DAY02/test_json.json',"w+"))
print("读取到json文件结束！")

