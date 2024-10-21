class ImperialToMetric:

    @staticmethod
    def inches_to_centimeters(inches):
        return f"Centimeters: {round(inches * 2.54, 2)}"

    @staticmethod
    def feet_to_meters(feet):
        return f"Meters:{round(feet * 0.3048, 2)}"

    @staticmethod
    def miles_to_kilometers(miles):
        return f"Kilometers: {round(miles * 1.60934, 2)}"

    @staticmethod
    def pounds_to_kg(kg):
        return f"Kilograms: {round(kg * 0.453592, 2)}"

    @staticmethod
    def gallons_to_liter(liter):
        return f"Liters:{round(liter * 3.78541, 2)}"


print(ImperialToMetric.inches_to_centimeters(1))
print(ImperialToMetric.feet_to_meters(1))
print(ImperialToMetric.miles_to_kilometers(1))
print(ImperialToMetric.pounds_to_kg(1))
print(ImperialToMetric.gallons_to_liter(1))