import pytest


@pytest.mark.xfail
def test_case_7():
    print("test_case_7 方法执行")
    assert 2 == 2


xfail = pytest.mark.xfail


@xfail(reason="bug 119")
def test_case_8():
    print("*****开始测试****")
    assert 0


def test_xfail():
    print("*****开始测试****")
    pytest.xfail(reason='该功能尚未完成')
    print("****测试过程****")
    assert 1 == 1
