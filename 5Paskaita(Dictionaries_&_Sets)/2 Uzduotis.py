# Create a program that collects a list of student names for a class trip. Use a set to ensure all names are unique and display the final list of students.
# Task instructions:
# Use a set to store student names.
# Continuously prompt the user to enter names until they decide to stop.
# Display the list of unique names at the end.


my_list = []
while True:

    zmones = input("Enter a student's name (or type 'done' to finish):")

    if zmones == "done":
        break

    else:
        my_list.append(zmones)
        print(zmones , "Was added to the list")

my_list = set(my_list)
print("List of students going on the trip:" , my_list)




# my_list = []
# while True:
#     input_ = input("Enter a student's name (or type 'done' to finish):")
#     if input_ == "done":
#         break
#     else:
#         my_list.append(input_)
#         print(input_, "was added to the list")
#
# print(my_list)