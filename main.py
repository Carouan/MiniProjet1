""""
Mini Projet 1 - Groupe 18

Membres :
---------
AIT HASSOU Mohamed - mohamed.aithassou@student.unamur.be
AL-AARAJY Mustafa - mustafa.alaarajy@student.unamur.be
AMETJAOU Omar - omar.ametjaou@student.unamur.be
EL-MCHACHTI Othmane - othmane.elmchachti@student.unamur.be
AUSPERT William - william.auspert@student.unamur.be
Baudoux Sébastien - sebastien.baudoux@student.unamur.be
BOECKMANS Noah - noah.boeckmans@student.unamur.be

- Ditribution du travail après la séance du 08/10/21
    Division du travail entre chaque membre.
    Chacun essaie de créer une fonction pour les différentes fonctionnalités du jeu.

Sébastien : Création compte
William/Omar : Combat
Noah : Achat/Capture
Mustapha : Vendre
Ottman : Capture
Mohamed : Evolution

"""
import gaming_tools, os
import account, purchase

print ("---------------------------------------- \n")
print (" Hi \n Welcome in the mini game from group 18")
print ("---------------------------------------- \n")

"""
print ("List of existing players : \n")
game_db = _load_game_db()
print (""+ game_db['players'] + "")
"""

# First step : Account creation
playername = input ("Enter your player name : ")
account.player_managment(playername)

# Second step : Purchase or capture a creature
def purchase_or_capture (choice):
    if (choice == "purchase"):
        # appel purchase
        purchase.shop(playername)
    elif (choice =="capture"):
        # call capture
        print("Capture")
    else:
        choice = input("Please enter 'purchase or 'capture'. \n")
        purchase_or_capture(choice)

choice = input ("Would you like to 'purchase' or 'capture' a creature ? \n")
purchase_or_capture(choice)
































#
