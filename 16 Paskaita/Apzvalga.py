# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self,a , b):
#         return a - b
# c1 = Calculator()
# print(c1.add(3, 5 ))
# c2 = Calculator()
# print(c2.subtract(4, 6))

#
# class Employee:
#     def __init__(self, first_name, last_name):
#         self.fname = first_name
#         self.lname = last_name
#
#     def print_name(self):
#         return print(f"{self.fname}, {self.lname}")
# e1 = Employee("Aauri", "Paka")
# e1.print_name()

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 20_000_000 or self.area > 3_000_000

    def population_density(self):
        return self.population / self.area

    def compare_pd(self, other_country):
        if self.population_density() > other_country.population_density():
            return f"{self.name} has a larger density than {other_country.name}"
        else:
            return f"{other_country.name} has a larger density than {self.name}"


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
lithuania = Country("Lithuania", 2_880_000, 65300)
latvia = Country("Latvia", 1_900_000, 64589)

print(lithuania.compare_pd(latvia))
# print(latvia.compare_pd(lithuania))

# print(australia.population_density())
# print(lithuania.population_density())
# print(latvia.population_density())
#
# print(australia.is_big)
# print(andorra.is_big)
# print(lithuania.is_big)