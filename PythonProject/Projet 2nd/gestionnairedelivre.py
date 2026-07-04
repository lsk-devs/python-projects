import os
from time import sleep

livres = []

def jeu():
    max_choix = ["1", "2", "3", "4", "5", "6"]
    blacklist = [
    "@", "#", "$", "%", "&", "*", "!", "?",
    "/", "\\", "|", "=", "+", "<", ">",
    "{", "}", "[", "]", "(", ")", ";", ":"
    ]
    while True:
        print("""
            ========================================
                📚 BIBLIOTHÈQUE PERSONNELLE 📚
            ========================================

                [1] Ajouter un livre
                [2] Afficher les livres
                [3] Rechercher un livre
                [4] Supprimer un livre
                [5] Nombre de livres
                [6] Quitter

            ========================================
            """)
        print("")
        choix = input(">> ")

        if choix not in max_choix:
            print("❌ Choix invalide.")
            print("Veuillez sélectionner uniquement parmis ces choix : [1], [2], [3], [4], [5], [6]")
            print("")
            input("Appuyer sur entrée pour revenir au menu...")
            os.system('cls')
            sleep(1)
            continue
        if choix == max_choix[0]:
            os.system('cls')
            sleep(1)
            while True:
                print("📖 Entrez le titre du livre :")
                choix_livre = input(">> ")
                for i in choix_livre:
                    if i in blacklist:
                        print("❌ Titre invalide (verifier a ce qu'il n'y est aucun caractère spéciaux).")
                        input("Appuyer sur entrée pour revenir en arrière...")
                        os.system('cls')
                        break
                if choix_livre.isdigit():
                    print("❌ Choix invalide.")
                    input("Appuyer sur entrée pour revenir en arrière...")
                    os.system('cls')
                    continue
                else:
                    livres.append(choix_livre)
                    print("✅ Livre ajouté avec succès !")
                    print("")
                    input("Appuyer sur entrée pour revenir au menu...")
                    os.system('cls')
                    sleep(1)
                    break
jeu()
                
