import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun2():
    assert False
