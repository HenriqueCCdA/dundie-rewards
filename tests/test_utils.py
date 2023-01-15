import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["bruno@rocha.com", "joe@doe.com", "a@b.pt"]
)
def test_positive_check_valid_email(address):
    """ensure email is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize("address", ["bruno@.com", "@doe.com", "a@b.p"])
def test_negative_check_valid_email(address):
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generation of roandom simple passwords
    TODO: Generate hashed comples passwords, encrypit it
    """
    passwords = [generate_simple_password(8) for _ in range(100)]

    assert len(set(passwords)) == 100
