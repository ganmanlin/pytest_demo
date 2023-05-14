import logging
from time import sleep


class CheckDemo:
    def check_demo1(self):
        sleep(1)
        logging.info("This is check_demo1")
        print("check_demo1")

    def check_demo2(self):
        sleep(1)
        print("check_demo2")
