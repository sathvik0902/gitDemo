import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    def test_fixturedemo1(self):
        print("1 after fixture setup execution")

    def test_fixturedemo2(self):
        print("2 after fixture setup execution")

    def test_fixturedemo3(self):
        print("3 after fixture setup execution")

    def test_fixturedemo4(self):
        print("4 after fixture setup execution")
