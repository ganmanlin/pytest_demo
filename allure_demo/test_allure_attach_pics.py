from venv import logger

import allure


class TestWithAttach:
    def test_pic(self):
        logger.info("这是通过allure.attach.file添加的截图")
        allure.attach.file("./data/image.png",
                           name="这是一个图片",
                           attachment_type=allure.attachment_type.PNG,
                           extension="png")

    def test_pic2(self):
        logger.info("这是通过allure.attach添加的截图")
        with open("./data/image.png", mode="rb") as f:
            file = f.read()
            allure.attach(file, "页面截图", allure.attachment_type.PNG)
