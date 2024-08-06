# # Create a simple phone book application where the user can add, search, and delete contacts from a dictionary.
# #The contacts should be stored as key-value pairs where the key is the person's name and the value is their phone number.
# #
# # Task instructions:
# # The user should be prompted with options to 'Add', 'Search', 'Delete', or 'Exit'.
# # 'Add' should prompt for a name and number, and add them to the dictionary.
# # 'Search' should prompt for a name and display the number if found.
# # 'Delete' should prompt for a name and remove the contact if found.
# # 'Exit' should break the loop and print all contacts.
#
#
phonebook = {}
while True:


    word = input("""
Add user with word 'Add'
Search user with word 'Search'
Delete user with word'Del'
or type 'Exit'.
""").lower()

    if "add" in word:
        name = input("Enter Name: ").lower()
        number = input("Enter number: ")
        phonebook.update({name : number})

    elif "search" in word:
        search = input("Enter Name: ").lower()
        print("The number is:" ,phonebook.get(search))

    elif "del" in word:
        del_ = input("Enter Name you want to delete:").lower()
        print("Phone contact was deleted:", phonebook.pop(del_))

    elif "exit" in word:
        print("You just exited phonebook")
        break

    else:
        print("Invalid action, please choose again")




# contacts = {}
#
# while True:
#     action = input("Choose an action: Add, Search, Delete, Exit: ").lower()
#     if action == 'add':
#         name = input("Enter contact name: ")
#         number = input("Enter contact number: ")
#         contacts[name] = number
#         print("Contact added.")
#     elif action == 'search':
#         name = input("Enter contact name to search: ")
#         print(f"Number: {contacts.get(name, 'Not found')}")  # Default message if not found
#     elif action == 'delete':
#         name = input("Enter contact name to delete: ")
#         if name in contacts:
#             del contacts[name]
#             print("Contact deleted.")
#         else:
#             print("Contact not found.")
#     elif action == 'exit':
#         print("Exiting phone book.")
#         break
#     else:
#         print("Invalid action. Please choose again.")
#
# print("All contacts:", contacts)


