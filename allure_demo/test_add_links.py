import allure


# 格式1：添加一个普通的link 链接
@allure.link('https://ceshiren.com/t/topic/15860')
def test_with_link():
    pass


# 格式1：添加一个普通的link 链接，添加链接名称
@allure.link('https://ceshiren.com/t/topic/15860', name='这是用例链接地址')
def test_with_named_link():
    pass


# 格式2：添加用例管理系统链接
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'


@allure.testcase(TEST_CASE_LINK, '用例管理系统')
def test_with_testcase_link():
    pass


# 格式3：添加bug管理系统链接
# 这个装饰器在展示的时候会带 bug 图标的链接。可以在运行时通过参数 `--allure-link-pattern` 指定一个模板链接，以便将其与提供的问题链接类型链接模板一起使用。执行命令需要指定模板链接：`--allure-link-pattern=issue:https://ceshiren.com/t/topic/{}`
@allure.issue("15860", 'bug管理系统')
def test_with_issue():
    pass
