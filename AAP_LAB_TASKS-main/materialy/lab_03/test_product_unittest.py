import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Laptop", 2999.99, 10)

    def test_add_stock_positive(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.add_stock(-2)

    def test_remove_stock_positive(self):
        self.product.remove_stock(3)
        self.assertEqual(self.product.quantity, 7)

    def test_remove_stock_too_much_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(15)

    def test_remove_stock_negative_raises(self):
        with self.assertRaises(ValueError):
            self.product.remove_stock(-2)

    def test_is_available_when_in_stock(self):
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        empty_product = Product("Myszka", 49.99, 0)
        self.assertFalse(empty_product.is_available())

    def test_total_value(self):
        self.assertAlmostEqual(self.product.total_value(), 29999.90, places=2)

    def test_init_invalid_values(self):
        with self.assertRaises(ValueError):
            Product("Zepsuty", -10.0, 5)
        with self.assertRaises(ValueError):
            Product("Zepsuty", 10.0, -5)


if __name__ == "__main__":
    unittest.main()