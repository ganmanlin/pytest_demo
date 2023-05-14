# fixture的作用域,尽量避免以test_开头
import pytest

"""
@pytest.fixture
def fixture_name():
    set_up 操作
    yield 返回值
    teardown 操作
"""
@pytest.fixture()
def login():
    print("\n登录操作")
    token = 'adjfoqwueoriqwe'
    username = "Tom"
    yield token, username  # 相当于return
    # teardown 操作
    print("登出")


def test_cart(login):
    print(f"token:{login}")
    print("购物车")


def test_order(login):
    print("下单")


class TestDemo:
    def test_case_demo1(self, login):
        print("case1")

    def test_case_demo2(self, login):
        print("case2")
