from time import sleep

import pytest
import yaml

from pytest_demo.l3_demo.yaml_demo.func.operator import my_add


def get_data():
    # 如果yaml文件中有中文，必须要加上encoding="utf-8"
    with open("l3_demo/yaml_demo/data/data.yaml", encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return data


def test_get_data():
    print(get_data())


class TestWithYAML:
    # 普通参数
    @pytest.mark.parametrize('x,y,expected', [[1, 1, 2], [3, 6, 9], [100, 200, 300]])
    def test_add(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)

    # Pytest 数据驱动结合 csv 文件
    @pytest.mark.parametrize('x,y,expected', get_data())
    def test_add_case2(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)
