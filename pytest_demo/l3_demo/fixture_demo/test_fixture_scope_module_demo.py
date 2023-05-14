# fixture的作用域,尽量避免以test_开头
import pytest


@pytest.fixture(scope='module')
def login():
    print("\n登录操作")


def test_search():
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单")


class TestDemo:
    def test_case_demo1(self, login):
        print("case1")

    def test_case_demo2(self, login):
        print("case2")
