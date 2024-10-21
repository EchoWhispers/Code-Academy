class Temperature:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return round(kelvin - 273.15, 1)

    @staticmethod
    def kelvin_to_farenheit(kelvin):
        return round((kelvin - 273.15) * 9 / 5 + 32, 1)

    def __str__(self):
        celsius = Temperature.kelvin_to_celsius(self.kelvin)
        farenheit = Temperature.kelvin_to_farenheit(self.kelvin)
        return f"Temp: {self.kelvin}K, {celsius}C, {farenheit}"



print(Temperature.kelvin_to_celsius(300))
print(Temperature.kelvin_to_farenheit(300))

