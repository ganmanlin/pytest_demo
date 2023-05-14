import pytest


@pytest.fixture()
def func(request):
    # 前置动作 -- 相当于setup
    print("这是一个fixture方法")

    # 前置动作 -- 相当于tearup
    # 定义一个终结器，teardown动作放在终结器中
    def over():
        print("session级别终结器")

    request.addfinalizer(over)


@pytest.fixture()
def func1(request):
    # 前置动作 -- 相当于setup
    print("这是func1的前置动作")

    yield
    print("这是func1的后置动作")


class TestClass(object):
    def test_with_scoped_finalizers(self, func, func1):
        print("测试用例")
