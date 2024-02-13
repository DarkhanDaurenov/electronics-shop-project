"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

def test_calculate_total_price():
    item = Item("Тестовый товар", 10.0, 5)
    assert item.calculate_total_price() == 50.0


def test_apply_discount():
    item = Item("Тестовый товар", 10.0, 5)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) > 0


def test_name_setter():
    item = Item('Ноутбук', 100, 5)
    item.name = 'Ноутбук'
    assert item.name == 'Ноутбук'


def test_name_setter_long_name():
    item = Item('Тестовый товар', 100, 5)
    item.name = 'ОченьДлинноеНаименование'
    assert item.name == 'ОченьДлинн'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Смартфон"


@pytest.fixture
def item_1():
    return Item("Телефон", 10000, 20)

@pytest.fixture
def item_2():
    return Item("Будка",2000, 50)


def test_add_(item_1, item_2):
    assert item_1 + item_2 == 70


def test_add_mistake(item_1):
    with pytest.raises(TypeError):
        assert item_1 + 30