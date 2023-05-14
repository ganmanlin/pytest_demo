import csv
from time import sleep

import pytest
from pytest_demo.l3_demo.csv_demo.func.operator import my_add


def get_csv():
    """
    获取csv数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('l3_demo/csv_demo/data/params.csv', 'r') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    return data


data = get_csv()


# test_add.py 文件内容
class TestWithCSV:

    @pytest.mark.parametrize('x,y,expected', [[1, 1, 2], [3, 6, 9], [100, 200, 300]])
    def test_add(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)

    @pytest.mark.parametrize('x,y,expected', data)
    def test_add(self, x, y, expected):
        sleep(1)
        assert my_add(int(x), int(y)) == int(expected)
