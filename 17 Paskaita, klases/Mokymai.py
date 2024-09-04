# # Inheritance
# class Employee:
#     def __init__(self, name, age, salary, experience):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.experience = experience
#
#     def show(self):
#         print(self.name, self.age, self.salary, self.experience)
#
# class Engineer(Employee):
#     def __init__(self, name, age, salary, experience, programming_language):
#         super().__init__(name, age, salary, experience ) #Tevines klases kintamuju iskvietimas
#         self.programming_language = programming_language
#     def show(self):
#         super().show()
#         print("Jei reik papildomai tik siai klasei")
# class Designer(Employee):
#     def __init__(self,name, age, salary, experience, program):
#         super().__init__(name, age, salary, experience) #Tevines klases kintamuju iskvietimas
#         self.program = program
#     def show(self):
#         super().show()
#         print("galima rasyt ir cia kazka kito jeigu reikia")
#
# en = Engineer(name="Jonas" ,age= 35 , salary= 5000, experience= 2, programming_language= "python")
# des = Designer(name= "Skaiste", age= 34,salary= 5000,experience= 2, program= "Figma")
#
#
# en.show()
# des.show()
# #----------------------------------------------------------------------------------------------------
#
# # Polymorfism
#
# class Reactangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w
#
#     def area(self):
#         return self.l * self.w
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
# rectangle = Reactangle(10, 20)
# square = Square(15)
# circle = Circle(7)
#
# shapes = [rectangle, square, circle]
#
# for shape in shapes:
#     print(shape.area())

#------------------------------------------------------------------------------
# # # Abstraction
# class Employee:
#     def __init__(self, name, age, salary, experience):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.experience = experience
#
#       # abstakcija
#     def show(self):
#         print(self.name, self.age, self.salary, self.experience)
#
#
# class Engineer(Employee):
#     def __init__(self, name, age, salary, experience, programming_language):
#         super().__init__(name, age, salary, experience ) #Tevines klases kintamuju iskvietimas
#         self.programming_language = programming_language
#     def show(self):
#         super().show()
#         print("Jei reik papildomai tik siai klasei")
#
#
# class Designer(Employee):
#     def __init__(self,name, age, salary, experience, program):
#         super().__init__(name, age, salary, experience) #Tevines klases kintamuju iskvietimas
#         self.program = program
#     def show(self):
#         super().show()
#         print("galima rasyt ir cia kazka kito jeigu reikia")
#
# en = Engineer(name="Jonas" ,age= 35 , salary= 5000, experience= 2, programming_language= "python")
# des = Designer(name= "Skaiste", age= 34,salary= 5000,experience= 2, program= "Figma")
#
#
# en.show()
# des.show()
#-------------------------------------------------------------------------------------------------------------
#Encapsulation


a = example  # public
_a = example # private
__a = example # hidden