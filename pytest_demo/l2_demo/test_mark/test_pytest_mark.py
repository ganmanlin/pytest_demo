import pytest


def double(a):
    return a * 2


@pytest.mark.P0
def test_double_int():
    print("test double int")
    assert 2 == double(1)


@pytest.mark.minus
def test_double_minus():
    print("test double minus")
    assert -2 == double(-1)


@pytest.mark.minus
def test_double_minus2():
    print("test double minus")
    assert -2 == double(-2)


@pytest.mark.float
def test_double_float():
    assert 0.2 == double(0.1)


@pytest.mark.float
def test_double_float2():
    assert -0.2 == double(-0.1)


@pytest.mark.str
def test_double_str():
    assert 'abc' == double(-0.1)
