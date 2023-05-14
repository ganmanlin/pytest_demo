import pytest


@pytest.mark.skip()
def test_case_1():
    print("代码没有开发完")
    assert True


@pytest.mark.skip(reason="代码未开发完")
def test_case_2():
    assert False


def check_login():
    return True


def test_case_3():
    print("start")

    if not check_login():
        pytest.skip("unsupported configuration")

    print("end")