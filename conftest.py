from typing import Optional

import pytest


# conftest.py 名字是固定的，不能改变
@pytest.fixture()
def login():
    print("\n登录操作")
    token = 'adjfoqwueoriqwe'
    username = "Tom"
    yield token, username  # 相当于return
    # teardown 操作
    print("登出")


@pytest.fixture()
def connect_db():
    print("连接数据库")
    yield
    print("断开数据库")


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')


# def pytest_runtest_setup(item: "Item") -> None:
#     print("hook:setup")
#
#
# def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
#     print("hook:teardown")
#     print("hook:teardown")
