# 参数化：多参数情况
# 数据放在元组中
import pytest


@pytest.mark.parametrize("username,password", [['right_username', 'right_pwd'],
                                               ['wrong_user', 'wrong_pwd'],
                                               ['', 'right_pwd']])
def test_login(username, password):
    print(f"登陆的用户名:{username},密码: {password}")


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7+5", 12)])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected


# 数据放在列表中
@pytest.mark.parametrize("test_input,expected", [["3+5", 8], ["2+5", 7], ["7+5", 12]])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
