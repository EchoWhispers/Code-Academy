class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item_name):
        if any(item["item"] == item_name for item in self.menu):
            self.orders.append(item_name)
            return "Order was added!"
        elif item_name != self.menu:
            return "This item is currently unavailable!"

    def fulfill_order(self, item_name):
        if any(item["item"] == item_name for item in self.orders):
            return f"The {item_name} is ready!"
        elif self.orders == 0:
            return "All orders have been fulfilled!"

    def list_orders(self):
        return self.orders

menu = [
    {"item": "orange juice", "type": "drink", "price": 1.80},
    {"item": "lemonade", "type": "drink", "price": 2.90},
    {"item": "cranberry juice", "type": "drink", "price": 1.80},
    {"item": "pineapple juice", "type": "drink", "price": 1.80},
    {"item": "lemon iced tea", "type": "drink", "price": 2.00},
    {"item": "vanilla chai latte", "type": "drink", "price": 3.20},
    {"item": "hot chocolate", "type": "drink", "price": 2.50},
    {"item": "iced coffee", "type": "drink", "price": 2.50},
    {"item": "tuna sandwich", "type": "food", "price": 3.90},
    {"item": "ham and cheese sandwich", "type": "food", "price": 3.50},
    {"item": "bacon and egg", "type": "food", "price": 4.50},
    {"item": "steak", "type": "food", "price": 6.50},
    {"item": "hamburger", "type": "food", "price": 2.50},
    {"item": "cinnamon roll", "type": "food", "price": 1.50},
]

shop = CoffeeShop("Tea House", menu)

shop.add_order("hot cocoa")
shop.list_orders()