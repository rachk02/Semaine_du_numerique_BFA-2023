import random

while True:
    n = random.randint(1, 100)
    for i in range(1, 4):
        print(f"Essai numero {i}")
        try:
            x = int(input("Veuillez emtrer un nombre positif\n> "))
            while x <= 0:
                x = int(input("Veuillez emtrer un nombre positif\n> "))
            if x > n:
                print(f"Oups! Le nombre saisi est plus grand, saisissez un nombre plus petit.")
            elif x < n:
                print(f"Oups! Le nombre saisi est plus petit, saisissez un nombre plus grand.")
            elif x == n:
                print("Parfait! Tu l'as devine !")
                break

        except:
            print("Veuillez vous assurer que la valeur saisie est un nombre svp!")

    print(f"le nombre etait {n}")
    print("Bonne chance pour la prochaine fois")
    y = input("Voulez-vous rejouer? ('y' pour continuer)\n> ")
    if not (y.lower() == "y"):
        break
    else:
        continue
