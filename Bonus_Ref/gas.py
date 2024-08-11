print("Welcome to grade tracker")

def students():

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


        students[name] = {"Math": grade1, "English": grade2, "Chemistry": grade3}
        i += 1
    for name, grades in students.items():
        sum_of_grades = sum(grades.values())
        average = round(sum_of_grades / len(grades), ndigits=2)
        print(f"Average grade of all subjects for {name}: is {average}")
    return students
print(students())


