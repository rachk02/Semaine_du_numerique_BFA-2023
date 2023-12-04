try:
    user_input = input("entrer une operation\n> ")
    # result = eval(user_input)
    if "+" in user_input:
        lst = user_input.split("+")
        result = int(lst[0]) + int(lst[1])
    elif "*" in user_input:
        lst = user_input.split("*")
        result = int(lst[0]) * int(lst[1])
    elif "/" in user_input:
        lst = user_input.split("/")
        result = int(lst[0]) / int(lst[1])
    elif "-" in user_input:
        lst = user_input.split("-")
        result = int(lst[0]) - int(lst[1])
    elif "%" in user_input:
        lst = user_input.split("%")
        result = int(lst[0]) % int(lst[1])
    print("Le resultat du calcul est:", result)
except ValueError:
    print("Veuillez reessayer avec des nombres.\n")
except ZeroDivisionError:
    print("Veuillez vous assurer que le diviseur ne soit pas pas de 0.\n")
