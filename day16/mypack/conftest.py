import pytest

@pytest.fixture(scope="session")
def setup():
    print("setup env")
    yield
    print("tear down...")