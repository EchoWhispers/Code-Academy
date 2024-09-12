# Create a few examples of yourself where you show four pillars of OOP in action.

# 1.Inheritance
# 2.Polymorfism
# 3.Abstraction
#4.Encapsulation



#1.


class Cars:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    
    def show(self):
        print(self.make, self.model, self.year, self.price)

class Audi(Cars):
    def __init__(self, make, model, year, price):
        super().__init__(make, model, year, price)

class BMW(Cars):
    def __init__(self, make, model, year, price):
        super().__init__(make, model, year, price)

class Ford(Cars):
    def __init__(self, make, model, year, price):
        super().__init__(make, model, year, price)


au = Audi("Audi", "A3", 2012, 9500)
bm = BMW("BMW", "X5", 2020, 11500)
fo = Ford("Ford", "Fusion", 2024, 12600)

au.show()
bm.show()
fo.show()