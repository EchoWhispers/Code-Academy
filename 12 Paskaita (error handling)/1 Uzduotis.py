# try:
#     print("pries")
#     print(10/0)
#     print("po")
# except:
#     print("pagavau")
# print("baigta")


#Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.

# 1.-------------------------------------------------------------------------------------------
# name = ["Jonas", "Petras", "Kazys"]
# try:
#     print(names)
# except NameError:
#     print("turetu buti >name<")
#
#2.---------------------------------------------------------------------------------------------
# def dalyba():
#     try:
#         a = float(input("iveskite skaiciu , kuri norite padalinti: "))
#         b = float(input("iveskite skaiciu is kurio norite padalinti: "))
#         c = a / b
#         return c
#
#     except ZeroDivisionError:
#         return "Dalyba is 0 negalima"
#
# print(dalyba())
#
#3.-----------------------------------------------------------------------------------------------
# try:
#     num = int(input("enter number: "))
#     print(num)
# except ValueError:
#     print("iveskite sveika skaiciu")

#4.------------------------------------------------------------------------------------------------
# try:
#     abc = [1, 2, 3, 4, 5]
#     print(abc[5])
# except IndexError:
#     print("nera tokios vietos")
#
#5.----------------------------------------------------------------------------------------------
try:
    typeA = [1, 2]
    typeB = {1,}
    typeC = typeA + typeB

    print(typeC)
except TypeError:
    print("netoks tipas")