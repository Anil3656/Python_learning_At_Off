from Items import Item
import json
import os

class User:
    def __init__(self, username):
        self.username = username
        self.filename = f"{username}_cart.json"

    def save_cart(self, items):
        data = [
            {"name": item.name, "price": item.price, "quantity": item.quantity}
            for item in items
        ]
        with open(self.filename, "w") as f:
            json.dump(data, f)
        print("💾 Cart saved!")

    def load_cart(self):
        items = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                for d in data:
                    items.append(Item(d["name"], d["price"], d["quantity"]))
        return items