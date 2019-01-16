import os
import pickle
import random 

nbr_coup_max = 10

liste_mots = [
    "handball",
    "fornite",
    "jouer",
    "crocodile",
    "manger",
    "table",
    "couteau",
    "gagner",
    "voyager",
    "glace",
    "journal",
    "admirable",
    "lampe",
    "rouler",
    "montagne",
    "remise",
    "ordinateur",
    "taxi",
    "vampire",
    "courir",
    "bracelet",
    "pied",
    "reveiller",
    "sauna",
    "circuit",
    "alliance",
    "date",
    "sorciere",
    "yeux",
    "camera",
    "profil",
    "charrue",
    "oiseau",
    "monnaie",
    "wagon",
    "etoile",
    "defendre",
    "soif",
    "vodka",
    "handicape"
]

def recup_lettre():

    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Lettre non valide")
        return recup_lettre()
    else:
        return lettre

def choisir_mot():
    
    return random.choice(liste_mots)

def recup_mot(random_mot, lettres_trouvees):
    
    mot_masque = ""
    for lettre in random_mot:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "_"
    return mot_masque

continuer_partie = 'o'

while continuer_partie != 'n':
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot(mot_a_trouver, lettres_trouvees)
    nbr_chances = nbr_coup_max
    while mot_a_trouver!=mot_trouve and nbr_chances>0:
    	lettre = recup_lettre()
    	if lettre in lettres_trouvees:
    		print("Tu as deja taper cette lettre")
    	elif lettre in mot_a_trouver:
    		lettres_trouvees.append(lettre)
    		print("Continue")
    	else:
    		nbr_chances -= 1
    		print("Elle n'est pas dans le mot")
    	mot_trouve = recup_mot(mot_a_trouver, lettres_trouvees)
    	print(mot_trouve)
    if mot_a_trouver==mot_trouve:
    	print("Tu as gagner")
    	print(mot_a_trouver)
    else:
    	print("Tu as perdu")
    	print(mot_a_trouver)
    continuer_partie = input("Veux-tu rejouer(o/n) ?")