from math import factorial
while True:
    try:
        user_input = int(input("entrer un nombre entier\n> "))
        if user_input < 0:
            print(f"{user_input}! = {-factorial(-user_input)}")
        else:
            print(f"{user_input}! = {factorial(user_input)}")
        break
    except ValueError:
        print("Veuillez reesayer avec un nombre entier.\n")
        continue
