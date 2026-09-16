class ShoppingCart:
    def __init__(self,owner_name):
        self.owner_name = owner_name
        self.item = [] 
        self.total_price = 0
    def add_item(self, item_name, price):
        self.item.append(item_name)
        self.total_price += price
    def view_cart(self):
        print(f"Items in the cart: ")
        for item in self.item:
            print(f" - {item}")
        print(f"final total price - {self.total_price}")


# Starter code to test:
cart = ShoppingCart("Rehan")
cart.add_item("Black Overcoat", 120)
cart.add_item("Wireless Mouse", 30)

cart.view_cart()