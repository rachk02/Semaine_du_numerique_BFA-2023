while True:
    try:
        n = int(input("Entrez la taille\n> "))
        while n < 0:
            n = int(input("Veuillez entrer un entier positif\n> "))
        x = "#" * (n + 1)
        s = " "
        pst = (len(x))-1
        if n == 0:
            print("+-+\n| |\n+-+")
            break
        else:
            for i in range(pst+1):
                if i == 0:
                    print(f"+{(pst+1) * '-'}+")
                print('|' + ('#' * (pst - i)) + s + ('#' * i) + '|')
                if i == (pst):
                    print(f"+{(pst + 1) * '-'}+")
            break
    except:
        print("Vous avez saisie une valeur erronee.\nVeuillez saisir un nombre entier.")
        break