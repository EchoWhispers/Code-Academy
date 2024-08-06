# Ask the user for a number, and print a triangle pattern that counts up to that number
#Each line should contain numbers from 1 to the line number.


a = int(input("Enter the triangle size:"))

for x in range(1, a+1):
    for y in range(1,x + 1):
        print(y, end=" ")
    print("*")





