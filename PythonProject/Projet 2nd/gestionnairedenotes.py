import os 
import statistics
from time import sleep

notes = []

def gestionnaire():    
    choix_max = ["1", "2", "3", "4"]
    while True:
        print("Bienvenue dans le gestionnaire de notes, voici les fonctions : [1] Ajoutez notes, [2] Afficher les notes, [3] Affichez la moyenne des notes, [4] Affichez la meilleur note")
        choix = input(">> ")

        if choix not in choix_max:
            os.system('cls')
            print("Vous avez uniquement la possibilité de sélectionner parmi ces options : [1], [2], [3], [4]")
            print(" ")
            input("Tapez sur entrée pour retourner au menu principal...")
            os.system('cls')
            continue
        if choix == choix_max[0]:
            os.system('cls')
            print("Quelle note voulez vous ajoutez ?")
            choix1 = input(">> ")
            if choix1.isdigit():
                note = int(choix1)
                if 0 <= note <= 20:
                    notes.append(note)
                    print("Note Ajouté avec succés !")
                    print(" ")
                    input("Tapez sur entrée pour retourner au menu principal...")
                    os.system('cls')
                    continue    
                else:
                    sleep(.5)
                    print("Erreur de note, veillez à avoir correctement saisi un nombre entre 0 et 20 (les '.', '-' sont exclus par le programme).")
                    print(" ")
                    input("Tapez sur entrée pour retourner au menu principal...")
                    os.system('cls')
                    continue
            else:
                    sleep(.5)
                    print("Erreur de note, veillez à avoir correctement saisi un nombre entre 0 et 20 (les '.', '-' sont exclus par le programme).")
                    print(" ")
                    input("Tapez sur entrée pour retourner au menu principal...")
                    os.system('cls')
                    continue
        if choix == choix_max[1]:
            if notes:
                os.system('cls')
                sleep(.5)
                print("Voici les note actuellement enregistrées : ",notes)
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
            else:
                os.system('cls')
                sleep(.5)
                print("Aucune note n'est actuellement enregistrées.")
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
        if choix == choix_max[2]:
            if notes:
                os.system('cls')
                sleep(.5)
                sleep(.5)
                print("La moyenne des notes actuellement enregistrées est : ",statistics.mean(notes))
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
            else:
                os.system('cls')
                sleep(.5)
                print("Aucune note n'est actuellement enregistrées.")
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
        if choix == choix_max[3]:
            if notes:
                os.system('cls')
                sleep(.5)
                print("La meilleure notes parmis celles enregistrées est : ",max(notes))
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
            else:
                os.system('cls')
                sleep(.5)
                print("Aucune note n'est actuellement enregistrées.")
                print(" ")
                input("Tapez sur entrée pour retourner au menu principal...")
                os.system('cls')
                continue
gestionnaire()