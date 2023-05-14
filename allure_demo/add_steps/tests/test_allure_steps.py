import pytest

from allure_demo.add_steps.steps.smiple_steps import *


@pytest.mark.parametrize('param1', ["pytest", "allure"], ids=['search pytest', 'search allure'])
def test_parameterize_with_id(param1):
    simple_step2(param1)


@pytest.mark.parametrize('param1', [True, False])
@pytest.mark.parametrize('param2', ['value 1', 'value 2'])
def test_parametrize_with_two_parameters(param1, param2):
    simple_step1(param1, param2)


@pytest.mark.parametrize('param2', ['pytest', 'unittest'])
@pytest.mark.parametrize('param1,param3', [[1, 2]])
def test_parameterize_with_uneven_value_sets(param1, param2, param3):
    simple_step1(param1, param3)
    simple_step2(param2)


# 方法二：使用 `with allure.step()` 添加测试步骤
@allure.title("搜索用例:{searchkey}")
@pytest.mark.parametrize('searchkey', ['pytest', 'unittest'])
def test_step_in_method(searchkey):
    with allure.step("测试步骤一：打开页面"):
        print("操作 a")
        print("操作 b")

    with allure.step("测试步骤二：搜索"):
        print("搜索操作 ")

    with allure.step("测试步骤三：断言"):
        assert False
