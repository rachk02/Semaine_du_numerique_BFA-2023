e = "*"
s = " "
while True:
    try:
        n = int(input(">>> entrer un nombre entier positif\n> "))
        while n < 0:
            n = int(input("Veuillez entrer un nombre entier positif\n> "))
        for i in range(n):
            print(f"{(n - i - 1) * s}{(2 * i + 1) * e}")
        break
    except ValueError:
        print(">>> Veuillez reesayer avec un nombre entier positif.\n")
        continue

