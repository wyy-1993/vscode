# -*- coding: utf-8 -*-
# @Time : 2023/4/26 22:04
# @Author : 简凡
# @Email : 18826478943@163.com
# @File : test_pytest.py
# @Project : 12Testing
# json\yaml\selenium\appium\request
from python.calc import cal
import pytest
import yaml

class TestCalc:
    def setup(self):
        self.cal = cal()

    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('./testdata.yml')))
    def test_add(self,a,b):
     #   self.cal=cal()
        result = self.cal.add(a,b)
        print(result)
        # assert 5 == result
    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('./testdata.yml')))
    def test_minus(self,a,b):
        result = self.cal.minus(a,b)
        print(result)
    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('./testdata.yml')))
    def test_div(self,a,b):
        if b == 0:
            print("is not 0")
            with pytest.raises(ZeroDivisionError):
                result = self.cal.div(a,b)
                # result = 0
                print("is not 0")
        else:
            result = self.cal.div(a,b)
            print(result)
    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open('./testdata.yml')))
    def test_mul(self,a,b):
        result = self.cal.mul(a,b)
        print(result)


