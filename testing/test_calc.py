# -*- coding: utf-8 -*-
# @Time : 2023/4/26 21:52
# @Author : 简凡
# @Email : 18826478943@163.com
# @File : test_calc.py
# @Project : 12Testing

import  unittest
from python.calc import cal

class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.cal = cal()
        result = self.cal.add(1,2)
        self.assertEqual(3,result)
        print(result)

    def test_minus(self,a,b):
        self.cal =cal()

