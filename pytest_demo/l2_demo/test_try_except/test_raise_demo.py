import pytest


def test_raise_demo():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError("value must be 0 or None")


def test_raise_demo2():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 42")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 42"


def test_raise_demo3():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        a = 10
        b = 0
        c = a / b
        print(f"你输入的两个数相除的结果是: {c}")
        raise ZeroDivisionError("division by zero")
