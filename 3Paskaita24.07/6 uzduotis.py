#Parašykite python programą, kuri paprašytų naudotojo įvesti 3 int tipo skaitmenis (1,2,3 etc..) ir rastų didžiausią įvestą reikšmę


first_int = int(input("Enter first integer : "))
second_int = int(input("Enter second integer : "))
third_int = int(input("Enter third integer : "))

biggest = [first_int, second_int, third_int]


print("This is a biggest integer you`re entered : ", max(biggest))