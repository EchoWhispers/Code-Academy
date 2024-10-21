import sqlite3

connection = sqlite3.connect("finance.db")
c = connection.cursor()

# query = """
# CREATE TABLE finance (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     income INTEGER,
#     expenses INTEGER,
#     amount INTEGER,
#     workplace STRING
# );
# """
# with connection:
#     c.execute(query)

while True:

    print("Press 1 to add income")
    print("Press 2 to add expense")
    print("Press 3 for amount")
    print("Press 4 to get all income")
    print("Press 5 to get all expense")
    print("Press 6 to delete income")
    print("Press 7 to delete expense")
    print("Press 8 to alter income")
    print("Press 9 to alter expense")
    print("Press 0 to Exit")

    user = int(input("Enter: "))

    if user == 1:
        option1 = input("Please enter income amount you want to add: ")
        query1 = f"INSERT INTO finance (income) VALUES ({option1})"
        print(f"You added income {option1} EUR")
        with connection:
            c.execute(query1)


    elif user == 2:
        option2 = input("Please enter expense amount you want to add: ")
        query2 = f"INSERT INTO finance (expenses) VALUES ({option2})"
        print(f"You added expense {option2} EUR")
        with connection:
            c.execute(query2)


    elif user == 3:
        income_amount = f"SELECT income FROM finance WHERE id = 1"
        expense_amount = f"SELECT expenses FROM finance WHERE id = 2"

        with connection:
            c.execute(income_amount)
            income = c.fetchone()
            income = income[0] if income else 0 # cia prasiau chatgpt pakalbos, nes niekaip nesugalvojau kaip man istraukti ta skaiciu be error :(

            c.execute(expense_amount)
            expense = c.fetchone()
            expense = expense[0] if expense else 0 # cia prasiau chatgpt pakalbos, nes niekaip nesugalvojau kaip man istraukti ta skaiciu be error :(
            total = income - expense
            print(f"Your total amount is : {total} EUR")


    elif user == 4:

        query4 = "SELECT SUM(income) FROM finance"

        with connection:
            c.execute(query4)
            total_income = c.fetchone()[0]
            print(f"Your total income is : {total_income} EUR")


    elif user == 5:

        query5 = "SELECT SUM(expenses) FROM finance"

        with connection:
            c.execute(query5)
            total_expense = c.fetchone()[0]
            print(f"Your total expenses is : {total_expense} EUR")


    elif user == 6:

        option = input("Enter id of income you want to delete: ")
        query6 = f"UPDATE finance SET income = 0 WHERE id = {option}"

        with connection:
            c.execute(query6)
            print(f"Income row with id {option} was deleted")


    elif user == 7:

        option = input("Enter id of expenses you want to delete: ")
        query7 = f"UPDATE finance SET expenses = 0 WHERE id = {option}"

        with connection:
            c.execute(query7)
            print(f"Expense row with id {option} was deleted")

    elif user == 8:

        option_id = input("Enter id of income you want to alter: ")
        new_value = input("Enter new amount: ")
        query8 = f"UPDATE finance SET income = {new_value} WHERE id = {option_id}"

        with connection:
            c.execute(query8)
            print(f"Income with id {option_id} was altered and new amount of {new_value} EUR was set!")

    elif user == 9:

        option_id = input("Enter id of expense you want to alter: ")
        new_value = input("Enter new amount: ")
        query9 = f"UPDATE finance SET expenses = {new_value} WHERE id = {option_id}"

        with connection:
            c.execute(query9)
            print(f"Expense with id {option_id} was altered and new amount of {new_value} EUR was set!")

    elif user == 0:
        print("Thank you , and see you soon!")
        break
