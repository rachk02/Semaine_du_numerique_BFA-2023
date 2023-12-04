
user_input = (input("entrer un verbe du premier groupe\n> ").lower())

while not (user_input.endswith("er")) or user_input == "aller":
    user_input = (input("Veuillez entrer un verbe du premier groupe\n> ").lower())
verb = user_input.removesuffix("er")
je = 'Je'
if verb[0] in ('a', 'e', 'i', 'o', 'u', 'h'):
    je = "J'"
if verb.endswith('g'):
    print(f"""le verbe {user_input} au present de l'indicatif
    {je} {verb}e
    Tu {verb}es
    Il {verb}e
    Nous {verb}eons
    Vous {verb}ez
    Ils {verb}ent""")
else:
    print(f"""le verbe {user_input} au present de l'indicatif
    {je} {verb}e
    Tu {verb}es
    Il {verb}e
    Nous {verb}ons
    Vous {verb}ez
    Ils {verb}ent""")
