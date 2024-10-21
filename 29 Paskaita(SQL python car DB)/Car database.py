import sqlite3

connection = sqlite3.connect("car_makes")
c = connection.cursor()

query = """
SELECT * FROM car_makes
WHERE Make = "Audi"
"""

with connection:
    c.execute(query)
    record = (c.fetchone()) #istraukiam 1 elementa
    print(record)


def main_menu():
    while True:
        print("\nPersonal Finance Manager")
        print("1. Enter Income")
        print("2. Enter Expense")
        print("3. Get Balance")
        print("4. Get All Incomes")
        print("5. Get All Expenses")
        print("6. Delete Income/Expense")
        print("7. Update Income/Expense")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            enter_income()
        elif choice == '2':
            enter_expenses()
        elif choice == '3':
            get_balance()
        elif choice == '4':
            get_all_incomes()
        elif choice == '5':
            get_all_expenses()
        elif choice == '6':
            delete_record()
        elif choice == '7':
            update_record()
        elif choice == '8':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")