import pytest

#Fixture : re-usable function
#scope ="function"
#scope ="module"
#scope = "class"
# scope = "session"
#hierarchy
# SESSION
#  ├── PACKAGE
#  │    ├── MODULE
#  │    │     ├── CLASS
#  │    │     │      ├── FUNCTION
#  │    │     │      └── FUNCTION

@pytest.fixture
def setup(scope="module"):
    print("browser setup")


def test_one(setup):
    print("first test")

def test_two(setup):
    print("second test")

