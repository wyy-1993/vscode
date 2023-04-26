# -*- coding: utf-8 -*-
# @Time : 2023/4/26 22:04
# @Author : 简凡
# @Email : 18826478943@163.com
# @File : test_pytest.py
# @Project : 12Testing
# json\yaml\selenium\appium\request
from python.calc import cal

class TestCalc:
    def setup(self):
        self.cal = cal()
    def test_a(self):
     #   self.cal=cal()
        result = self.cal.add(2,3)
        print(result)
        assert 5 == result


# 补充测试用例 ，根据等价类划分，参数化
