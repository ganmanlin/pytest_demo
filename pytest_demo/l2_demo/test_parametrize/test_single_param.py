import pytest

search_list = ['appium', 'selenium', 'pytest']


def test_search_case1():
    assert 'appium' in search_list


def test_search_case2():
    assert 'selenium' in search_list


def test_search_case3():
    assert 'pytest' in search_list


def test_search_case4():
    assert 'abc' in search_list


def test_search_case5():
    assert 'requests' in search_list


# 参数化：单参数情况，每一条测试数据都会生成一个case
@pytest.mark.parametrize('name', ['appium', 'selenium', 'pytest', 'abc', 'requests'])
def test_search(name):
    assert name in search_list
