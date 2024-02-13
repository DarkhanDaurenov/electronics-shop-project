import pytest
from src.phone import Phone

@pytest.fixture
def phone():
    return Phone("Phone", 1000, 10, 2)


def test_phone_initialization(phone):
    assert phone.name == "Phone"
    assert phone.price == 1000
    assert phone.quantity == 10
    assert phone.number_of_sim == 2


def test_number_of_sim_setter_valid(phone):
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_number_of_sim_setter_invalid(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1

def test_repr(phone):
    assert repr(phone) == "Phone('Phone', 1000, 10, 2)"

