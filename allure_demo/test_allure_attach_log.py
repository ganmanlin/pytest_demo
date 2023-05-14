import allure
from utils.log_util import logger


@allure.epic("EPIC 1")
@allure.feature("Module 1")
class TestEpic:
    @allure.story("Sub-module1")
    @allure.title("Testcase 1")
    def test_case1(self):
        logger.info("This is TestEpic's first case")
        print("Test case 1")

    @allure.story("Sub-module2")
    @allure.title("Testcase 2")
    def test_case2(self):
        logger.debug("This is TestEpic's second case")
        print("Test case 2")

    @allure.story("Sub-module3")
    @allure.title("Testcase 3")
    def test_case3(self):
        logger.warning("This is TestEpic's third case")
        print("Test case 3")

    @allure.story("Sub-module4")
    @allure.title("Testcase 4")
    def test_case4(self):
        logger.error("This is TestEpic's 4th case")
        print("Test case 4")
