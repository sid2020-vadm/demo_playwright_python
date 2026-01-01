import pytest

@pytest.mark.skip
def test_login_email():
    print("login by email")
    assert 1 == 1

@pytest.mark.skip
def test_login_facebook():
    print("login by facebook")
    assert 1 == 1

@pytest.mark.skip
def test_login_phone():
    print("login by phone")
    assert 1 == 1


def test_signup_email():
    print("signup by email test")
    assert True == True


def test_signup_facebook():
    print("signup by facebook test")
    assert True == True


def test_signup_phone():
    print("signup by phone test")
    assert True == True
