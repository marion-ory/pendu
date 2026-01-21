import random  # choix des mots
import datetime
import time

date_actuelle = datetime.datetime.now().strftime(" %D/%M/%Y %H:%M")
compteur_erreur = 0
lettre_trouve = []


def verifier_lettre(lettre_tape, mot_a_deviner):
    global compteur_erreur
    if lettre_tape in mot_a_deviner:
        lettre_trouve.append(lettre_tape)
        print("Bravo")
        return True
    else:
        print("Perdu")
        compteur_erreur += 1
        return False


def affciher_mot(mot_a_deviner, lettre_deja_trouve):
    resultat = ""

    for lettre in mot_a_deviner:
        if lettre in lettre_deja_trouve:
            resultat += lettre + " "
        else:
            resultat += "_ "
    return resultat


# Niveau selon longueur de mot
def niveau_difficulte(mot_a_deviner):
    longueur = len(mot_a_deviner)
    if longueur <= 6:
        return " Facile", 5
    elif 6 < longueur < 12:
        return " Moyen", 10
    else:
        return " Difficile", 15


# Chrono score
def chrono_score(points_niveau, temps_passe):
    if temps_passe < 40:
        bonus = 15
    elif temps_passe < 60:
        bonus = 5
    else:
        bonus = 0

    score_final = points_niveau + bonus
    return score_final, bonus
