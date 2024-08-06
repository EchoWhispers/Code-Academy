import random
number = random.randint(1 , 100)



while True:
    guess = int(input("spek: "))
    if guess == number:
        print("atspejai")
        break
    elif guess < number:
        print("per mazas")
    else:
        print("skaiciu per didelis")