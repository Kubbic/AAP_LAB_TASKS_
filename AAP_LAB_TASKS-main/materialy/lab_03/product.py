class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError()
        if quantity < 0:
            raise ValueError()
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError()
        self.quantity += amount

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError()
        if amount > self.quantity:
            raise ValueError()
        self.quantity -= amount

    def is_available(self) -> bool:
        return self.quantity > 0

    def total_value(self) -> float:
        return self.price * self.quantity

    def apply_discount(self, percent: float):
        """Obniza cene o podany procent (0-100)."""
        if not (0 <= percent <= 100):
            raise ValueError()
        self.price = self.price * (1 - percent / 100.0)