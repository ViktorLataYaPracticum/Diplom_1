import pytest
from unittest.mock import Mock

from praktikum.burger import Burger

# Тест метода set_buns. 
def test_set_buns():
    burger = Burger()
    bun = Mock()
    burger.set_buns(bun)

    assert burger.bun == bun

# Тест метода add_ingredient. 
def test_add_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert ingredient in burger.ingredients