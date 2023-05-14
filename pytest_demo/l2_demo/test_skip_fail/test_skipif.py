import sys

import pytest


@pytest.mark.skipif(sys.platform == "darwin", reason="does not run on mac")
def test_case4():
    print("test_case4")
    assert True


@pytest.mark.skipif(sys.platform == "win", reason="does not run on window")
def test_case5():
    print("test_case5")
    assert True


@pytest.mark.skipif(sys.version_info < (3, 6), reason="require python 3.6 or higher")
def test_case6():
    print("test_case6")
    print(sys.version_info)
    assert True
