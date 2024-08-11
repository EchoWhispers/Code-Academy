print("Welcome to grade tracker")


num_students = int(input("Enter the number of students you like to add: "))

students = {}

i = 0
while i < num_students:

    name = input("Enter student name: ")
    grade1 = float(input("Enter Math grade: "))

    if grade1 < 0 or grade1 > 100:
        print("Please enter a valid grade between 0 and 100.")
        break
    else:
        print("You have entered Math grade:", grade1)

    grade2 = float(input("Enter English language grade: "))
    if grade2 < 0 or grade2 > 100:
        print("Please enter a valid grade between 0 and 100.")
        break
    else:
        print("You have entered English language grade:", grade2)

    grade3 = float(input("Enter Chemistry grade: "))
    if grade3 < 0 or grade3 > 100:
        print("Please enter a valid grade between 0 and 100.")
        break
    else:
        print("You have entered Chemistry grade:", grade3)


    students[name] = {"grade1": grade1, "grade2": grade2, "grade3": grade3}
    i += 1
for name, grades in students.items():
    sum_of_grades = sum(grades.values())
    average = sum_of_grades / len(grades)
    print(f"Average grade for all subjects for {name}: is {average}")





#print(sum_of_grades)
#You can then easily get averages by using sum() and len() built-in functions
# Example of sum and len:
# list = [1,3,5]
# average = sum(list) / len(list) # 9 / 3

