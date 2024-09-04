class House:
    def __init__(self, cost, age, door_count): # konstruktorius
        self.cost = cost
        self.age = age
        self.door_count = door_count
    def __str__(self):
        return f"Cost: {self.cost}, Age: {self.age}, Door count: {self.door_count}"


a = House(20000, 20, 1)
b = House(15000, 10, 3)# objektas

print(a)
print(b)
