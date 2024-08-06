# Task: Student Grade Tracker
#
#
# Requirements:
#
#
# Allow the user to input the number of students.
# For each student, prompt the user to enter their name and three subject grades (assume a scale of 0 to 100).
# Calculate and display the average grade for each student and their name
# A valid grade is between 0 and 100 only, if another number is entered, the program should print: "Please enter a valid grade between 0 and 100."
#
#
# If you did this task, you already learned everything quite well from the first lectures. Congrats :) Have more experience and want more challenges?
#
# Bonus Challenges (Optional):
#
# Allow the user to input the number of subjects dynamically.
# Determine and display the student name with the highest average grade.
# Ensure the program handles non-numeric inputs appropriately. (We didn't learn this yet, but read about try/except)
# Save the data about students to file (CSV)
# Any other improvements? Like adding lesson names for grades? Do it!
#
#
# Tips and tricks:
# You can use dictionaries to store information about each student. This helps organize data with meaningful keys like 'name' and 'grades'.
# Example - student = {'name': "Mantas Skara", 'grades': [0,15,72]}
# You can then easily get averages by using sum() and len() built-in functions
# Example of sum and len:
# list = [1,3,5]
# average = sum(list) / len(list) # 9 / 3
#
#
#
#
# Starting Code:
# num_students = int(input("Enter the number of students: "))
#
#
# students = []
#
#
# i = 0
# while i < num_students:
#    name = input("Enter student name: ")
#    students.append(name)
#    i+=1
#
#
# print(students)