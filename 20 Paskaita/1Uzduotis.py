
def add_one(number): #1
    print("Welcome to ADD ONE function!")
    if type(number) == int:
        print("Correct type!")
        return number + 1
    else:
        print("A number needs to be an integer!")
        print("Bye!")


my_list = [1, 2, 3] #2

for item in my_list: #3
    result = add_one(item) #4
    print("Result: ", result + 1)#5