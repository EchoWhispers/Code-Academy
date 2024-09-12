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
class CoffeeShop:
    def __init__(self, name , menu):
        self.name = name
        self.menu = menu
        self.orders = []


    def add_order(self):
        item_name = input("What you want to eat?: ")
        for x in self.menu:
            if item["item"] == item_name:
                self.orders.append(item)
                print("Was added")
                return
            else:
                print("Not on a menu!")
shop = CoffeeShop("BLA BLA", menu)
shop.add_order()

#
#     def add_order(self):
#         item_name = input("What would you like to order?: ").lower()
#         for item in self.menu:
#             if item["item"] == item_name:
#                 self.orders.append(item)
#                 print(f"{item_name} has been added to your order.")
#                 return
#         print(f"Sorry, {item_name} is not available in the menu.")
#
#     def show_orders(self):
#         if not self.orders:
#             print("No orders placed.")
#         else:
#             print("Your orders are:")
#             for order in self.orders:
#                 print(f"{order['item']} - ${order['price']:.2f}")
#
# # Define the menu
# menu = [
#     {"item": "orange juice", "type": "drink", "price": 1.80},
#     {"item": "lemonade", "type": "drink", "price": 2.90},
#     {"item": "cranberry juice", "type": "drink", "price": 1.80},
#     {"item": "pineapple juice", "type": "drink", "price": 1.80},
#     {"item": "lemon iced tea", "type": "drink", "price": 2.00},
#     {"item": "vanilla chai latte", "type": "drink", "price": 3.20},
#     {"item": "hot chocolate", "type": "drink", "price": 2.50},
#     {"item": "iced coffee", "type": "drink", "price": 2.50},
#     {"item": "tuna sandwich", "type": "food", "price": 3.90},
#     {"item": "ham and cheese sandwich", "type": "food", "price": 3.50},
#     {"item": "bacon and egg", "type": "food", "price": 4.50},
#     {"item": "steak", "type": "food", "price": 6.50},
#     {"item": "hamburger", "type": "food", "price": 2.50},
#     {"item": "cinnamon roll", "type": "food", "price": 1.50},
# ]
#
# # Create the CoffeeShop object
# shop = CoffeeShop("BLA BLA", menu)
#
# # Run without a loop: only ask for a single order
# shop.add_order()
#
# # Show the orders after adding
# shop.show_orders()










