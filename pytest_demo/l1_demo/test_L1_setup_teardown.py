# 模块级别,只被调用1次
def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源释放：teardown module")


def test_case1():
    print("case1")


def test_case2():
    print("case2")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源准备：teardown function")


class TestDemo:
    def setup_class(self):
        print("TestDemo setup class")

    def teardown_class(self):
        print("TestDemo teardown class")

    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")

    def test_case3(self):
        print("case3")

    def test_case4(self):
        print("case4")
