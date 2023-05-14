import pytest


@pytest.mark.parametrize("b", ["a", "b", "c"])
@pytest.mark.parametrize("a", [1, 2, 3])
def test_param1(a, b):
    print(f"笛卡积形式的参数化中 a={a} , b={b}")
