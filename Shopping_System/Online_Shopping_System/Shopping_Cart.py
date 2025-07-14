from User import User
from Items import Item

class ShoppingCart:
    def __init__(self, user: User):
        self.user = user
        self.items = user.load_cart()

    def add_item(self, item: Item):
        for existing in self.items:
            if existing.name.lower() == item.name.lower():
                existing.quantity += item.quantity
                print(f"🛒 Updated '{item.name}' quantity to {existing.quantity}")
                return
        self.items.append(item)
        print(f"✅ Added '{item.name}' x{item.quantity} to cart")

    def view_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
        else:
            print("\n🛒 Your Cart:")
            total = 0
            for i, item in enumerate(self.items, 1):
                line_total = item.price * item.quantity
                print(f"{i}. {item} | Total: ₹{line_total:.2f}")
                total += line_total
            print(f"\n💰 Grand Total: ₹{total:.2f}")

    def remove_item(self):
        self.view_cart()
        if self.items:
            try:
                index = int(input("Enter item number to remove: ")) - 1
                removed = self.items.pop(index)
                print(f"❌ Removed '{removed.name}' from cart.")
            except (IndexError, ValueError):
                print("⚠️ Invalid item number.")

    def checkout(self):
        total = sum(item.price * item.quantity for item in self.items)
        self.view_cart()
        print(f"🧾 Final Amount: ₹{total:.2f}")
        print("✅ Thank you for shopping!")
        self.items = []
        self.user.save_cart(self.items)

    def save(self):
        self.user.save_cart(self.items)