# You are tasked with creating a Python program that manages student grades. The program should perform the following operations:
# Store Student Grades: Input student names and their corresponding grades, storing them in a dictionary.
# Calculate Average Grade: Compute the average grade of all students.
# Remove Underperforming Students: Remove students with grades below 80 from the dictionary.
# Check Student Existence: Check if a specific student exists in the dictionary and display an appropriate message.

# Detailed steps:
# Create a Dictionary of Grades: Prompt the user to input student names and grades, and store them in a dictionary where the name is the key and the grade is the value.
# Calculate the Average Grade: Use Python's sum() and len() functions on the dictionary values to calculate the average grade.
# Remove Students with Grades Below 80: Iterate through the dictionary to find students with grades below 80 and remove them.
# Check for a Student's Existence: Prompt for a student's name, check if this name exists in the dictionary, and print whether the student is found.


Dictionary_of_Grades = {}

while True:

    name = input("Enter student name (or type 'done' to finish):").lower()

    if name == "done":
        break
    else:

        grade = float(input("Enter grade:"))
        Dictionary_of_Grades[name] = grade



suma = list(Dictionary_of_Grades.values())
sumos = sum(suma)
element = Dictionary_of_Grades.__len__()
avg = sumos / element
print("Average Grades" ,avg)

students_below_80 = {name for name, grade in Dictionary_of_Grades.items() if grade < 80}
for student in students_below_80:
    del Dictionary_of_Grades[student]

while True:

    student_to_check = input("Enter a student name to check (or type 'done' to finish):").lower()
    if student_to_check == "done":
        break
    else:
        if student_to_check in Dictionary_of_Grades:
            print(f" {student_to_check} found. Average grade: {Dictionary_of_Grades[student_to_check]}")
        else:
            print(student_to_check, "Not Found")