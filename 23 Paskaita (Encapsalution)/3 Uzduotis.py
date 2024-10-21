class Base:
    def __init__(self, age, cost, year_built, weight):
        self.age = age
        self.cost = cost
        self.year_build = year_built
        self.weight = weight

    def display(self):
        return f"SpaceCraft age: {self.age}, Base cost: {self.cost}, Year build: {self.year_build}, and weight: {self.weight}"

class SpaceShuttle(Base):
    FUEL_COST = 0.8  # Cost per kg of fuel
    BURN_RATE = 2

    def __init__(self, age, cost, year_built, weight, number_of_ppl, salary, orbit_height):
        super().__init__(age, cost, year_built, weight)
        self.number_of_ppl = number_of_ppl
        self.salary = salary
        self.orbit_height = orbit_height

    def callculate(self):
        cost = self.number_of_ppl * self.salary
        fuel_cost = self.FUEL_COST * self.BURN_RATE
        return f"Peoples salaries : {cost} EUR, Fuel costs: {fuel_cost}l/km"

    def report(self):
        info = self.display()
        return info




#base = Base(10, 120000, 2024, 3000)
#print(base.display())

spaceshuttle = SpaceShuttle(11, 25000, 2022, 3000, 15, 4000, 500)
print(spaceshuttle.callculate())

print(spaceshuttle.report())



# class Spacecraft:
#     def __init__(self, age, cost, year_built, weight):
#         self.age = age
#         self.cost = cost
#         self.year_built = year_built
#         self.weight = weight
#
#     def display_info(self):
#         return f"Spacecraft Info - Age: {self.age} years, Cost: ${self.cost}, Year Built: {self.year_built}, Weight: {self.weight}kg"
#
# class SpaceShuttle(Spacecraft):
#     FUEL_COST = 0.8  # Cost per kg of fuel
#     BURN_RATE = 2  # Burn rate kg/mile
#
#     def __init__(self, age, cost, year_built, weight, orbit_height, number_of_people, base_salary):
#         super().__init__(age, cost, year_built, weight)
#         self.orbit_height = orbit_height
#         self.number_of_people = number_of_people
#         self.base_salary = base_salary
#
#     def calculate_mission_cost(self):
#         burn_rate_variable = 2500 / self.orbit_height
#         fuel_cost = self.FUEL_COST * self.BURN_RATE * burn_rate_variable
#         personal_cost = self.number_of_people * self.base_salary
#         return fuel_cost + personal_cost
#
#     def get_full_report(self):
#         info = self.display_info()
#         mission_cost = self.calculate_mission_cost()
#         report = (
#             f"{info}\n"
#             f"Orbit Height: {self.orbit_height} miles\n"
#             f"Number of Personnel: {self.number_of_people}\n"
#             f"Base Salary per Person: ${self.base_salary}\n"
#             f"Total Mission Cost: ${mission_cost:.2f}\n"
#         )
#         # Print to console
#         print(report)
#         # Write to a file
#         with open("mission_report.txt", "w") as file:
#             file.write(report)