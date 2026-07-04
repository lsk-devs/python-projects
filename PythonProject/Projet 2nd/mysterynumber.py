import random
import os
from time import sleep

def regle():
    print("""
            ========================================
                        📜 RÈGLES 📜
            ========================================

            🎯 Objectif :
            Trouver le nombre mystère choisi
            aléatoirement par le programme.

            📌 Comment jouer ?

            - Entrez un nombre.
            - Le programme vous indiquera :
                📈 "C'est plus grand"
                📉 "C'est plus petit"

            - Continuez jusqu'à trouver
            le nombre mystère.

            🏆 Plus vous trouvez rapidement,
            plus votre score est bon !
            Ps: Le nombre d'essais est random...
            """)
    input("Appuie sur Entrée pour revenir au menu...")
    os.system("cls" if os.name == "nt" else "clear")

def game():
    essais = 0
    essais_max = random.randint(3, 9)

    nombre_ordi = random.randint(1, 100)
    while essais < essais_max:
        print("Essais restant : ",essais_max - essais)
        choix_num = input("🔢 Entrez un nombre : ")

        if not choix_num.isdigit():
            print("")
            print("❌ Entrée invalide.")
            print("")
            continue

        choix_num = int(choix_num)
        essais += 1

        if choix_num > nombre_ordi:
            print("")
            print("📉 C'est plus petit")
            print("")
        elif choix_num < nombre_ordi:
            print("")
            print("📈 C'est plus grand")
            print("")
        else:
            print("")
            print(f"🎉 Bravo ! Tu as trouvé le nombre en {essais} essais !")
            print("")
            input("Appuie sur Entrée pour revenir au menu...")
            break
    else:
        print("")
        print("💀 Perdu ! Le nombre était :", nombre_ordi)
        print("")
        input("Appuie sur Entrée pour revenir au menu...")
    os.system("cls" if os.name == "nt" else "clear")

def exit():
    print("""
    ========================================
            👋 FERMETURE DU JEU 👋
    ========================================

    Merci d'avoir joué à Mystery Number !

    À bientôt ! 🎲
    ========================================
    """)    

def main():
    while True:
        essais = 0
        essais_max = random.randint(3, 9)

        print("""
        ========================================
                🎲 MYSTERY NUMBER 🎲
        ========================================

        Bienvenue dans Mystery Number !

        Le but est de deviner le nombre
        mystère choisi aléatoirement.
        Ps: Le nombre d'essais est random...

        📈 Plus grand
        📉 Plus petit

        ========================================

        [1] Jouer
        [2] Règles
        [3] Quitter

        ========================================
        """)

        choix = input(">> ")

        if choix not in ("1", "2", "3"):
            sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            print("❌ Choix invalide.")
            input("Appuyer sur entrée pour revenir au menu principal...")
            os.system("cls" if os.name == "nt" else "clear")
            continue

        if choix == "1":
            game()
            continue

        if choix == "2":
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            regle()
            continue

        if choix == "3":
            os.system("cls" if os.name == "nt" else "clear")
            sleep(1)
            exit()
            sleep(2)
            break

if __name__ == "__main__":
    main()
