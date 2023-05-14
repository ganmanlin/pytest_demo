import sys


def test_1():
    assert True


def test_2():
    a = 1
    b = 3
    exec = 5
    assert a + b == exec, f"{a}+{b}=={exec}, 结果为False"


def test_3():
    assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"
