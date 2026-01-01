import pytest

#Fixture : re-usable function
@pytest.fixture
def setup():
    print("setup browser")
    yield
    print("close browser")


def test_one(setup):
    print("first test")

def test_two(setup):
    print("second test")

