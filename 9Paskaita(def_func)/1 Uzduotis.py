# Create a function to calculate and display the Body Mass Index (BMI) from user-provided height in meters and weight in kilograms.
# The formula is BMI = weight in kg/ height in m2. The output should be rounded to 2 digits after the decimal point.
#
#
# Enter height in meters: 1.8
# Enter weight in kilograms: 70
# The BMI is 21.60.

print("Welcome to BMI counter")

def bmi_printed(weight , height):
    height = float(input("Please enter your height: "))
    weight = float(input("Please enter your weight: "))
    bmi = weight / (height ** 2)
    return bmi

print(f"The BMI is:",(round(bmi_printed(weight= "weight", height="height"), ndigits=2)))


# def calculate_bmi(height, weight):
#     return weight / (height ** 2)
#
# height = float(input("Enter height in meters: "))
# weight = float(input("Enter weight in kilograms: "))
# bmi = calculate_bmi(height, weight)
# print(f"The BMI is {bmi:.2f}.")