class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def get_info(self):  # Method
        return f"Car: {self.brand} {self.model}"


# Creating an object of the Car class
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())  # Calling the method to get the car's information


#Attributes = properties or data of the object.
#Methods = actions or behaviors the object can perform.