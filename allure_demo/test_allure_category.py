import allure


@allure.epic("需求1")
@allure.feature("功能模块1")
class TestEpic:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能2")
    @allure.title("用例2")
    def test_case2(self):
        print("用例2")

    @allure.story("子功能2")
    @allure.title("用例3")
    def test_case3(self):
        print("用例3")

    @allure.story("子功能1")
    @allure.title("用例4")
    def test_case4(self):
        print("用例4")


@allure.epic("需求2")
@allure.feature("功能模块2")
class TestEpic2:
    @allure.story("子功能1")
    @allure.title("用例1")
    def test_case1(self):
        print("用例1")

    @allure.story("子功能2")
    @allure.title("用例2")
    def test_case2(self):
        print("用例2")

    @allure.story("子功能2")
    @allure.title("用例3")
    def test_case3(self):
        print("用例3")

    @allure.story("子功能1")
    @allure.title("用例4")
    def test_case4(self):
        print("用例4")

    @allure.story("子功能3")
    @allure.title("用例5")
    def test_case5(self):
        print("用例5")
