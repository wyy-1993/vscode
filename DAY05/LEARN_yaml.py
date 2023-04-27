# -*- coding: utf-8 -*-
# @Time : 2022/7/17 10:17
# @Author : 简凡
# @Email : 18826478943@163.com
# @File : LEARN_yaml.py
# @Project : vscode
import pytest
import yaml

class TestData:
    print("test")
    @pytest.mark.parametrize(("a","b","c"),yaml.safe_load(open("./test.yaml")))
    def test_case(self,a,b,c):
        print(a+b+c)




