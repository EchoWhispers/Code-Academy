class Vechile:
    def __init__(self, make , model, year, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity


    def display(self):

        print(f" Make: {self.make}, Model: {self.model}, Seating capacity: {self.capacity}, Year: {self.year}")

    def engine_start(self):
        print(f"Engine is running")

    def engine_stop(self):
        print(f"Engine is stopping")

    def fare(self):
        return self.capacity * 100

class Train(Vechile):
    def __init__(self, make , model, year, capacity):
        super().__init__(make , model, year, capacity)

class Taxi(Train):
    def __init__(self, make , model, year, capacity):
        super().__init__(make , model, year, capacity)

class Bus(Taxi):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year, capacity)

    def maintenance(self):
        return self.fare() * 0.10



vehicle = Vechile(make= "Toyota", model="Verso", year=2020, capacity=4)
train =Train(make= "Bobr", model="Grizzle", year= 2019, capacity= 350)
taxi = Taxi(make= "Toyota", model="Prius", year= 2015, capacity= 5)
bus = Bus(make= "Mercedes", model="Gigantus", year= 2018, capacity= 36)
vehicle.display()
train.display()
taxi.display()
bus.display()
print(vehicle.fare())
print(train.fare())
print(taxi.fare())
print(bus.fare())
print(bus.maintenance())