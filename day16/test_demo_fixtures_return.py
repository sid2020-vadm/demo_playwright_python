import pytest

#Fixture : re-usable function
@pytest.fixture
def setup():
    return "chrome"


def test_one(setup):
    print(f"browser is {setup}")
    print("first test")

def test_two(setup):
    print(f"browser is {setup}")
    print("second test")

