import pytest


@pytest.fixture(params=[['Tom', 'Tom123'],['Harry', 'Harry123']])
def login(request):
    print(f"用户名:{request.param}")
    temp = request.param
    yield temp


def test_demo1(login):
    tmp = login
    print(f"demo1 case,数据为：{tmp}")
