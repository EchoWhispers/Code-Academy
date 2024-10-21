# class Animal:
#     def __init__(self, speak):
#         self.speak = speak
#         return f"Animal cant speak"
#
# class Dog(Animal):
#     def __init__(self, speak):
#         super().__init__(speak)
#         return
#
# d = Dog("Woof woof!")
# print(d.speak)
# class Cat(Animal):
#     def __init__(self, speak):
#         super().__init__(speak)
#         return
#
#
# c = Cat("Meow , Meow")
# print(c.speak)
#


class Animal:
    def speak(self):
        print("Animal cant speak")

class Dog(Animal):

    def speak(self):
        print("Woof woof")
class Cat(Animal):

    def speak(self):
        super().speak()
        print("meaow")


d = Dog()
d.speak()
c = Cat()
c.speak()