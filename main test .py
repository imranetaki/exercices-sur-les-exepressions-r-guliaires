from expression_reg import recherche, verifie_chaine, remplace, verifie_numero, verifie_email

chaine = input("saisire votre paragraphe:")
mot = input("saisre le mot que vous voulez chercher:")

chiane2 = "ahmed mange la pomme "

numero = "123-444-333"

email = input("Sasire votre email:")

print("Est ce que le mot existe?:",recherche(mot, chaine))

print("Est que la chaine contient des nombre?:", verifie_chaine(chaine))

print(remplace(chiane2))

print("Est ce que le nombre est au format correspondant ( XX-XXX-XXXX.)?:",verifie_numero(numero))

print("Ce email est:",verifie_email(email))

