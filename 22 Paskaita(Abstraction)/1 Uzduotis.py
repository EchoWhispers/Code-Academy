from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


    def get_name(self, name):
        self.name = name
        return self.name


class Dog(Animal):

    def speak(self):
        return f"Dog says woof"
class Cat(Animal):
    def speak(self):
        return f"Cat says meow"



dog = Dog(name= "Bobr")
cat = Cat(name= "Pinki")

print(dog.get_name("Bobr"))
print(cat.get_name("Pinki"))

print(dog.speak())
print(cat.speak())