print("Welcome to student grade tracker")

students = {}

while True:
    start = str(input("If you want to add student to grade tracker please type 'add' ,for exit type 'done': "))
    if "done" == start:
        print("You succesfully exited the grade tracker")
        break
    elif "add" == start:

        name = str(input("Enter the student name: "))
        grade1 = int(input("Enter grade: "))
        grade2 = int(input("Enter grade: "))
        grade3 = int(input("Enter grade: "))

        if grade1 < 0 or grade1 > 100:
            print("You entered incorrect grade(grade from 0 to 100)")
        elif grade2 < 0 or grade2 > 100:
            print("You entered incorrect grade(grade from 0 to 100)")
        elif grade3 < 0 or grade3 > 100:
            print("You entered incorrect grade(grade from 0 to 100)")
        else:
            print(f" {grade1}, {grade2} and {grade3} for {name} was entered")
            students[name] = grade1 , grade2 , grade3
    else:
        print("Incorrect command, Try again")

suma = list(students.values())
#sumos = sum(suma)
element = name.__len__()
#avg = sumos / element
print("Average Grades" ,element)

#average = sum(x)/ len(students)
#You can then easily get averages by using sum() and len() built-in functions
# Example of sum and len:
# list = [1,3,5]
# average = sum(list) / len(list) # 9 / 3




#
#             print(f" {grade1} for {student} was entered")
#             students.append([student, grade1, ])
#
#         # grade2 = float(input("Enter grade: "))
#         # if grade2 < 0 or grade2 > 100:
#         #     print("You entered incorrect grade(grade from 0 to 100)")
#         # else:
#         #     print(f" {grade2} for {student} was entered")
#         #     students.update({student : grade2})
# print(students)
#         # # grade3 = float(input("Enter grade: "))
#         # if grade3 < 0 or grade3 > 100:
#         #     print("You entered incorrect grade(grade from 0 to 100)")
#         # else:
#         #     print(f"{grade3} for {student} was entered")
#         #     students.append(student)
#
# #     else:
# #         print("You have entered incorrect word, please try again")
# # students_dict = set(students)
# # print(students_dict)
#
