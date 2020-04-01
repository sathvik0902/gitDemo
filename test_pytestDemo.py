import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_A():
    print("first file A method")
    print("gitDemo project wit gitB")
    print("gitDemo project wit gitB second time")
    print("gitDemo project wit gitStuff")

@pytest.mark.xfail
def test_B():
    print("first file B method")