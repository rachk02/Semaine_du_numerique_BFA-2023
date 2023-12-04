from math import sqrt

a = int(input("entrer nombre entier(a)\n> "))
b = int(input("entrer nombre entier(b)\n> "))
c = int(input("entrer nombre entier(c)\n> "))
delta = ((b**2)-4*a*c)
print(f"Delta est egale a : {delta}")
if delta > 0:
    x1 = ((-b-sqrt(delta))/(2 * a))
    x2 = ((-b + sqrt(delta))/(2 * a))
    print(f"Les solutions de l'equation sont :\n> X1= {x1:.3} et X2 = {x2:.3}")
elif delta == 0:
    x0 = (-b/(2*a))
    print(f"La solution de l'equation est :\n> X0 = {x0:.3}")
else:
    racine_cmplx = sqrt(-delta) * 1j
    x1 = ((-b-racine_cmplx)/(2 * a))
    x2 = ((-b + racine_cmplx) / (2 * a))
    print(f"Les solutions complexes de l'equation sont :\n> X1 = {x1:.3} et X2 = {x2:.3}")
