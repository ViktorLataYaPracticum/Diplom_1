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

# Тест метода remove_ingredient.
def test_remove_ingredient():
    burger = Burger()
    ingredient = Mock()

    # убедимся что счписок точно пустой
    assert len(burger.ingredients) == 0  

    burger.add_ingredient(ingredient)
    burger.remove_ingredient(0)

    assert len(burger.ingredients) == 0    