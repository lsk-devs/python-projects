import random
import os

choix = ["pierre", "feuille", "ciseaux"]

def jouer():
    score_joueur = 0
    score_ordinateur = 0

    while True:
        joueur = input("pierre / feuille / ciseaux (q pour quitter) : ").lower()

        if joueur == "q":
            return False  # on quitte totalement

        if joueur not in choix:
            print("Choix invalide")
            continue

        ordi = random.choice(choix)
        print("Ordinateur :", ordi)

        if joueur == ordi:
            print("Égalité")

        elif (joueur == "pierre" and ordi == "ciseaux") or \
             (joueur == "feuille" and ordi == "pierre") or \
             (joueur == "ciseaux" and ordi == "feuille"):
            score_joueur += 1
            print("Tu gagnes")

        else:
            score_ordinateur += 1
            print("Tu perds")

        print("Score :", score_joueur, "-", score_ordinateur)

        if score_joueur == 3:
            print("Tu as gagné la partie !")
            return True

        if score_ordinateur == 3:
            print("Tu as perdu la partie")
            return True

while True:
    jouer()

    retry = input("Rejouer ? (y/n) : ").lower()

    if retry != "y":
        print("Fin du programme")
        break
    else:
        os.system('cls')