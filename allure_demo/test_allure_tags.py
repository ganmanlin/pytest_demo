import pytest


# 当用例通过时标注为 xfail
@pytest.mark.xfail(condition=lambda: True, reason='这是一个预期失败的用例')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


# 当用例通过时标注为 xpass
@pytest.mark.xfail
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True


# 跳过用例
@pytest.mark.skipif('2 + 2 != 5', reason='当条件触发时这个用例被跳过 @pytest.mark.skipif')
def test_skip_by_triggered_condition():
    pass
