class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} x{self.quantity} - ₹{self.price:.2f} each"