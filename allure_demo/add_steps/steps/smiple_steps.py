import allure


@allure.step
def simple_step1(step_param1, step_param2=None):
    '''定义一个测试步骤'''
    print(f"首先：连接数据库，准备数据")
    print(f"步骤1：打开页面，参数1: {step_param1}, 参数2：{step_param2}")


@allure.step
def simple_step2(step_param):
    '''定义一个测试步骤'''
    print(f"步骤2：完成搜索 {step_param} 功能")
