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

# Тест метода move_ingredient.
def test_move_ingredient():
    burger = Burger()

    ing1 = Mock()
    ing2 = Mock()
    ing3 = Mock()

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)

    burger.move_ingredient(0, 2)

    assert burger.ingredients == [ing2, ing3, ing1]

# Тест метода get_price.
def test_get_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ing1 = Mock()
    ing1.get_price.return_value = 50

    ing2 = Mock()
    ing2.get_price.return_value = 150

    burger.set_buns(bun)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    assert burger.get_price() == 300
