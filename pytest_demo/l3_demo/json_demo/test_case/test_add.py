# 读取json文件内容
import json
from time import sleep

import pytest

from pytest_demo.l3_demo.json_demo.func.operator import my_add


def get_json():
    with open('l3_demo/json_demo/data/params.json', 'r') as f:
        data = json.loads(f.read())
        print(list(data.values()))
        return list(data.values())


# test_add.py 文件内容
class TestWithJson:

    @pytest.mark.parametrize('x,y,expected', [[1, 1, 2], [3, 6, 9], [100, 200, 300]])
    def test_add(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)

    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)

