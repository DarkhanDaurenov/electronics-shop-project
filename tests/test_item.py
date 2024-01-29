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
