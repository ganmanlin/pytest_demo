import pytest


# ids 为用例起别名，ids列表参数的个数要与参数值的个数一致
@pytest.mark.parametrize("test_input,expected", [("3+5", 8),
                                                 ("2+5", 7),
                                                 ("7+5", 12)],
                         ids=['add_3+5=8',
                              'add_2+5=7',
                              'add_3+5=12'])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
