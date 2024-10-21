class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides


    def area(self):
        pass



class Rectangle(Shape):
    def __init__(self, width, height, name, sides):
        super().__init__(name, sides)
        self.width = width
        self.height = height


    def area(self):
        area = self.width * self.height
        return area

class Square(Rectangle):

    def __init__(self, width, height, name, sides, side_length):
        super().__init__(width, height, name, sides)
        self.side_length = side_length

    def area(self):
        area = self.sides * self.side_length
        return area






rectangle = Rectangle(width=2, height=4, name= "React" , sides=4)
print(rectangle.area())
square = Square(width=4, height=4,name="Square", sides=4, side_length=4)
print(square.area())

