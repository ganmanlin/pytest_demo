import logging
from time import sleep


class TestDemo:
    def test_demo1(self):
        sleep(1)
        logging.info("This is test_demo1")
        print("test_demo1")

    def test_demo2(self):
        sleep(1)
        logging.info("This is test_demo2")
        print("test_demo2")


def test_demo3():
    sleep(1)
    logging.info("This is test_demo3")
