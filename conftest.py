import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will execute last")


@pytest.fixture()
def applicationdata():
    print('User Profile data')
    return ['madhu','ch','34']


@pytest.fixture(params=[("chrome", "Madhu", "34"), ("firefox", "Chinnu", "29"), ("IE", "Sathvik", "5"), ("Opera", "Charvik", "1")])
def crossBrowser(request):
    return request.param
