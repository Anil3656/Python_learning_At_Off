from Items import *
from Shopping_Cart import ShoppingCart
from User import User

class Shop:
    def __init__(self):
        self.user = None
        self.cart = None

    def login(self):
        username = input("Enter your username: ").strip().lower()
        self.user = User(username)
        self.cart = ShoppingCart(self.user)
        print(f"👤 Welcome, {username.capitalize()}!")

    def run(self):
        self.login()
        while True:
            print("\n--- Shopping Cart Menu ---")
            print("1. Add item")
            print("2. View cart")
            print("3. Remove item")
            print("4. Checkout")
            print("5. Save & Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                name = input("Enter item name: ")
                try:
                    price = float(input("Enter price (₹): "))
                    quantity = int(input("Enter quantity: "))
                    self.cart.add_item(Item(name, price, quantity))
                except ValueError:
                    print("⚠️ Please enter valid price and quantity.")

            elif choice == "2":
                self.cart.view_cart()

            elif choice == "3":
                self.cart.remove_item()

            elif choice == "4":
                self.cart.checkout()
                break

            elif choice == "5":
                self.cart.save()
                print("👋 Goodbye!")
                break

            else:
                print("⚠️ Invalid choice. Enter 1–5.")

# Run the application
if __name__ == "__main__":
    shop = Shop()
    shop.run()