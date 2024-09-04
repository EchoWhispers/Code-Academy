class Country:
    def __init__(self, country, pop, area):
        self.country = country
        self.pop = pop
        self.area = area

    def get_pop(self):
        return self.pop

    def is_big(self):
        if australia.get_pop() > andorra.get_pop():
            return print(f"Australia is bigger")
        else:
            return print(f"Andora is bigger")



# Creating country objects
australia = Country(country= "Australia", pop= 23545500, area= 7692024)
andorra = Country(country= "Andorra", pop= 76098, area= 468)



# print(australia.get_pop())
# print(andorra.get_pop())

# Printing country details
# print(australia)
# print(andorra)


# Getting specific details using methods
print(australia.is_big())
