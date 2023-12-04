while True:
    try:
        user_input = int(input("entrer un nombre entier\n> "))
        if (user_input % 2) == 0:
            print(f"le nombre {user_input} est pair")
        else:
            print(f"le nombre {user_input} est impair")
        break
    except ValueError:
        print("Veuillez reesayer avec un nombre entier.\n")
        continue
