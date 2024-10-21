class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
        return self

    def set_age(self, age):
        self.age = age
        return self

p = Person("Bobas", 25)
p.set_name("Jonas").set_age(30)
print(p.name)
print(p.age)