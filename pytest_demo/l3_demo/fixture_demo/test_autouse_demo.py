# fixture的作用域,尽量避免以test_开头
import pytest


@pytest.fixture(autouse=True)
def login():
    print("\n登录操作")


def test_search():
    print("搜索")


def test_cart():
    print("购物车")


def test_order():
    print("下单")


class TestDemo:
    def test_case_demo1(self, ):
        print("case1")

    def test_case_demo2(self, ):
        print("case2")

    def test_case_demo3(self, ):
        print("case3")
