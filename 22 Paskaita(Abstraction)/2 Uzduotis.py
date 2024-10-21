from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


    def area(self):
        return self.weight * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * 2 * self.radius* 2

c = Circle(6)
print(f"Circle area: {c.area()}")
r = Rectangle(3, 6)
print(f"Rectangle area: {r.area()}")