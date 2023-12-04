from pathlib import Path
from csv import *


class Student:
    """Class to represent a student"""

    def __init__(self, nom, prenom, age, sexe, note):
        self.nom = nom
        self.prenom = prenom
        self.age = int(age)
        self.sexe = sexe
        self.note = float(note)


def csv_creater(csv_file):
    if not (csv_file.exists()):
        with open(csv_file, mode='w', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=["nom", "prenom", "age", "sexe", "note"])
            writer.writeheader()


folder = Path.cwd() / "liste des etudiants"
folder.mkdir(parents=True, exist_ok=True)
dbs_csv = folder / "DBS.csv"
esi_csv = folder / "ESI.csv"
csv_creater(dbs_csv)
csv_creater(esi_csv)


def csv_adder(csv_path, data):
    with open(csv_path, mode='a', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=["nom", "prenom", "age", "sexe", "note"])
        writer.writerow(data)


def csv_reader(csv_path):
    std_dict = {}
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = DictReader(file)
        for row in reader:
            std_dict[f"{row['nom'] + ' ' + row['prenom']}"] = row
    std_dict = dict(sorted(std_dict.items()))
    return std_dict


def csv_updater(csv_path, data):
    with open(csv_path, mode='w', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=["nom", "prenom", "age", "sexe", "note"])
        writer.writeheader()
        writer.writerows(data)


def std_saver():
    nom = input("Entrez le nom de l'etudiant\n> ")
    prenom = input("Entrez le prenom de l'etudiant\n> ")
    age = input("Entrez l'age de l'etudiant\n> ")
    sexe = input("Entrez le sexe de l'etudiant\n> ")
    note = float(input("Entrez la note de l'etudiant\n> "))
    return Student(nom, prenom, age, sexe, note).__dict__


def std_updater(update_dict):
    nom = input("Modifier le nom de l'etudiant(Passez! pour conserver)\n> ")
    update_dict["nom"] = update_dict["nom"] if nom.lower() == '' else nom
    prenom = input("Modifier le prenom de l'etudiant(pass pour conserver)\n> ")
    update_dict["prenom"] = update_dict["prenom"] if prenom.lower() == '' else prenom
    age = input("Modifier l'age de l'etudiant(pass pour conserver)\n> ")
    update_dict["age"] = update_dict["age"] if age == '' else age
    sexe = input("Modifier le sexe de l'etudiant(pass pour conserver)\n> ")
    update_dict["sexe"] = update_dict["sexe"] if sexe.lower() == '' else sexe
    note = input("Modifier la note de l'etudiant(pass pour conserver)\n> ")
    update_dict["note"] = update_dict["note"] if note == '' else note
    return update_dict


def alter_std(std_csv):
    idd = input("Entrer le nom et le prenom de l'etudiant a modifier\n> ")
    std_dict = csv_reader(std_csv)
    update_dict = std_dict[idd.lower()]
    std_dict[idd.lower()] = std_updater(update_dict)
    new_id = f"{std_dict[idd.lower()]['nom']} {std_dict[idd.lower()]['prenom']}"
    std_dict[new_id] = std_dict.pop(idd.lower())
    csv_updater(std_csv, std_dict.values())


def del_std(std_csv):
    id = input("Entrer le nom et le prenom de l'etudiant a supprimer\n> ")
    std_dict = csv_reader(std_csv)
    if id.lower() in std_dict:
        del std_dict[id.lower()]
    csv_updater(std_csv, std_dict.values())
    print(f"L'etudiant {id.lower()} a ete supprime")


def alter_std_note1(std_csv):
    std_dict = csv_reader(std_csv)
    for key in std_dict:
        if float(std_dict[key]["note"]) < 10:
            std_dict[key]["note"] = str(float(std_dict[key]["note"]) + 1)
    csv_updater(std_csv, std_dict.values())


def alter_std_note0(std_csv):
    std_dict = csv_reader(std_csv)
    for key in std_dict:
        if 10 <= float(std_dict[key]["note"]) <= 15:
            std_dict[key]["note"] = str(float(std_dict[key]["note"]) + 0.5)
    csv_updater(std_csv, std_dict.values())


def mean_std(std_csv):
    length = 0
    total = 0
    std_dict = csv_reader(std_csv)
    for key in std_dict:
        total += float(std_dict[key]["note"])
        length += 1
    return total / length


def note_max(std_csv):
    note = {}
    tri = []
    std_dict = csv_reader(std_csv)
    for key in std_dict:
        note[float(std_dict[key]["note"])] = key
    for value in note:
        tri.append(float(value))
    return note[max(tri)]


def std_displayer(std_dict):
    print(
        f"+{28 * '-'}+{59 * '-'}+{5 * '-'}+{10 * '-'}+{6 * '-'}+\n|{12 * ' '}nom {12 * ' '}|{26 * ' '}prenom {26 * ' '}| age |   sexe   | note |\n+{28 * '-'}+{59 * '-'}+{5 * '-'}+{10 * '-'}+{6 * '-'}+")

    for key in std_dict:
        print(
            f"| {std_dict[key]['nom'].upper()}{(27 - len(std_dict[key]['nom'])) * ' '}| {std_dict[key]['prenom'].title()}{(58 - len(std_dict[key]['prenom'])) * ' '}| {std_dict[key]['age']}{(4 - len(std_dict[key]['age'])) * ' '}| {std_dict[key]['sexe']}{(9 - len(std_dict[key]['sexe'])) * ' '}| {std_dict[key]['note']}{(5 - len(std_dict[key]['note'])) * ' '}|")
        print(f"+{28 * '-'}+{59 * '-'}+{5 * '-'}+{10 * '-'}+{6 * '-'}+")


def home_page():
    print(f"""
            **********************Finale du concours <<Mini programme>>**********************
               1-   Enregistrer un etudiant de Digital Business School
               2-   Enregistrer un etudiant de l'ecole superieire d'informatique
               3-   Afficher la liste des etudiants de Digital Business School
               4-   Afficher la liste des etudiants de l'ecole Superieure d'informatique
               5-   Modifier un etudiant d'un etablissement donne (DBS School ou ESI)
               6-   Supprimer un etudiant d'un etablissement donne (DBS School ou ESI)
               7-   Incrementer de 1 point les notes des etudiants ayant une note
                    strictement inferieure a 10 (pour les deux etablissements)
               8-   Incrementer de 1 point les notes des etudiants ayant une note
                    comprise entre [10-15] (pour les deux etablissements)
               9-   Calculer la moyenne de classe en mathematique des etudiants des deux
                    etablissements
               10-  Afficher les informations du meilleur etudiant qui excelle en mathematique pour
                    les deux etablissements
               11-  Quitter
            *********************MERCI POUR L'ORGANISATION DE LA FINALE *********************""")


home_page()
while True:
    try:
        n = int(input("Choisissez une des options ci-dessus\n> "))
        while n < 0 or n > 11:
            n = int(input("Veuillez choisir une des options ci-dessus(1 - 11)\n> "))
        if n == 1:
            while True:
                dbs_std = std_saver()
                csv_adder(dbs_csv, dbs_std)
                add = input("Voulez-vous ajouter un etudiant du Digital Business School?\no pour Oui!\n> ")
                if add.lower() == "o":
                    continue
                else:
                    break
            continue

        elif n == 2:
            while True:
                esi_std = std_saver()
                csv_adder(esi_csv, esi_std)
                add = input("Voulez-vous ajouter un etudiant de l'Ecole Superieur d'Informatique?\no pour Oui!\n> ")
                if add.lower() == "o":
                    continue
                else:
                    break
            continue

        elif n == 3:
            dbs_std_dict = csv_reader(dbs_csv)
            std_displayer(dbs_std_dict)
            continue

        elif n == 4:
            esi_std_dict = csv_reader(esi_csv)
            std_displayer(esi_std_dict)
            continue

        elif n == 5:
            choice = input("Voulez-vous modifier les donnees d'un etudiant du DBS(d) ou de l'ESI(e)?\n> ")
            if choice.lower() == "d":
                alter_std(dbs_csv)
                continue
            elif choice.lower() == "e":
                alter_std(esi_csv)
                continue
            else:
                continue

        elif n == 6:
            choice = input("Voulez-vous supprimer un etudiant du DBS(d) ou de l'ESI(e)?\n> ")
            if choice.lower() == "d":
                del_std(dbs_csv)
                continue
            elif choice.lower() == "e":
                del_std(esi_csv)
            continue

        elif n == 7:
            alter_std_note1(dbs_csv)
            alter_std_note1(esi_csv)
            continue

        elif n == 8:
            alter_std_note0(dbs_csv)
            alter_std_note0(esi_csv)
            continue

        elif n == 9:
            choice = input("Voulez-vous calculer la moyenne en mathemathique des etudiants du DBS(d) ou de l'ESI(e) ou "
                           "des deux[a la fois](x)?\n> ")
            if choice.lower() == "d":
                mean = mean_std(dbs_csv)
                print(f"La moyenne en mathematiques des etudiants du Digital Business School est\n>>> {mean:.2f}")

            elif choice.lower() == "e":
                mean = mean_std(esi_csv)
                print(
                    f"La moyenne en mathematiques des etudiants de l'Ecole Superieur d'Informatique est\n>>> {mean:.2f} ")

            elif choice.lower() == "x":
                print(
                    f"La moyenne en mathematiques des etudiants du Digital Business School est\n>>> {mean_std(dbs_csv):.2f}")
                print(
                    f"La moyenne en mathematiques des etudiants de l'Ecole Superieur d'Informatique est\n>>> {mean_std(esi_csv):.2f} ")
            continue

        elif n == 10:
            dbs_std_dict = csv_reader(dbs_csv)
            dbs_key = note_max(dbs_csv)
            dbs_nom = dbs_std_dict[dbs_key]["nom"].upper()
            dbs_prennom = dbs_std_dict[dbs_key]["prenom"].capitalize()
            dbs_note = float(dbs_std_dict[dbs_key]["note"])
            esi_std_dict = csv_reader(esi_csv)
            esi_key = note_max(esi_csv)
            esi_nom = esi_std_dict[esi_key]["nom"].upper()
            esi_prennom = esi_std_dict[esi_key]["prenom"].capitalize()
            esi_note = float(esi_std_dict[esi_key]["note"])
            esi = len(f"{esi_nom} {esi_prennom} {esi_note}")
            dbs = len(f"{dbs_nom} {dbs_prennom} {dbs_note}")

            print(f"""
            =========                                                               =========
            MEILLEUR                                                                 MEILLEUR
            =========                                                               =========
            ESI                                                                    DBS School
            {esi_nom} {esi_prennom} {esi_note}{(81 - (esi + dbs)) * ' '}{dbs_nom} {dbs_prennom} {dbs_note}
            =================================================================================""")
            continue

        elif n == 11:
            break

        elif n == 0:
            home_page()
            continue

    except:
        print("Veuillez saisir un nombre compris entre 1 et 10")
        continue
