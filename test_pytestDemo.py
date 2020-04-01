import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_A():
    print("first file A method")

@pytest.mark.xfail
def test_B():
    print("first file B method")