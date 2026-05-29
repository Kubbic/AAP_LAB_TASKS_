import pytest
from product import Product


@pytest.fixture
def product():
    return Product("Laptop", 2999.99, 10)


def test_is_available(product):
    assert product.is_available() is True


@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (20, 30),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-2)


def test_remove_stock_too_much_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(15)


def test_remove_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(-5)


def test_is_not_available_when_empty():
    empty_p = Product("Myszka", 49.99, 0)
    assert empty_p.is_available() is False


def test_total_value(product):
    assert product.total_value() == pytest.approx(29999.90, 0.01)


@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount(product, percent, expected_price):
    product.price = 100.0
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("invalid_percent", [-10, 150])
def test_apply_discount_invalid_raises(product, invalid_percent):
    with pytest.raises(ValueError):
        product.apply_discount(invalid_percent)