from math import factorial
while True:
    try:
        n = int(input(f"entrer un nombre entier\n> "))
        for i in range(int(n)):
            x = []
            for j in range(i + 1):
                val = (factorial(i) / (factorial(j) * factorial(i - j)))
                x.append(int(val))
            y = ""
            for k in range(len(x)):
                length = str(x[k])
                if len(length) > 1:
                    y += f"{str(x[k])}{(7 - len(length) + 1) * ' '}"
                else:
                    y += f"{str(x[k])}{7 * ' '}"
                del length
            print(f"{y}")
        break
    except:
        s = input("Vous avez saisi une valeur erronee,\nVoulez-vous reessayer!\nTapez o si Oui\n> ")
        if s.lower() == "o":
            continue
        else:
            break
