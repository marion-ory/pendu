import os  # gestion des fichiers en python
import random  # choix des mots
import keyboard  # choix lettre sur clavier
import pygame  # interface visuelle
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


# BOUCLE JEU
while True:
    nom_joueur = input("Nom du joueur : ")
    print("Que souhaitez-vous faire ? ")
    print("1 - Jouer")
    print("2 - Choisir un mot")
    print("3 - Quitter")
    choix = input("Votre choix : ")

    match choix:
        case "1":  # JOUE
            with open("mot.txt", "r", encoding="utf-8") as fichier:
                liste_mot = fichier.read().splitlines()

            if liste_mot:
                debut_chronometre = time.time()  # debut chronometre
                mot_a_deviner = random.choice(liste_mot)
                mon_niveau, points = niveau_difficulte(mot_a_deviner)
                print(f"Niveau : {mon_niveau}, Rapporte : {points} points")

                compteur_erreur = 0
                lettre_trouve = []
                print("Le mot à deviner :", affciher_mot(mot_a_deviner, lettre_trouve))

                while compteur_erreur <= 6:
                    choix_lettre = input("Tapez une lettre : ").upper()
                    verifier_lettre(choix_lettre, mot_a_deviner)
                    affichage = affciher_mot(mot_a_deviner, lettre_trouve)
                    print(affichage)

                    if "_" not in affichage:
                        fin_chronometre = time.time()
                        temps_total = round(
                            fin_chronometre - debut_chronometre, 2
                        )  # Chrono total si gagné
                        score_final, bonus = chrono_score(points, temps_total)
                        print(f"Gagné en : {temps_total}s , Bonus rapidité + {bonus}")
                        print(f"Score total final : {score_final}")
                        with open(
                            "scores.txt", "a", encoding="utf-8 "
                        ) as f_scores:  # ajout dans score.TXT
                            f_scores.write(
                                f"Joueur :{  nom_joueur} , Niveau: { mon_niveau}, Score : { points} s , Bonus temps : { bonus}, en {temps_total}, le : {date_actuelle}\n "
                            )
                        break
                    if compteur_erreur >= 6:
                        fin_chronometre = time.time()
                        temps_total = round(
                            fin_chronometre - debut_chronometre, 2
                        )  # Chrono total si perdu
                        print(f"Perdu en : {temps_total}")
                        break

        case "2":  # AJOUT MOT
            ajout_mot = input("Ajoutez un mot à faire découvrir : ")
            ajout_mot = ajout_mot.strip().upper()

            # L'ouverture du fichier doit être dans le case 2
            with open("mot.txt", "a", encoding="utf-8") as fichier:
                fichier.write(ajout_mot + "\n")
            print(f"Le mot '{ajout_mot}' a bien été ajouté !")

        case "3":
            break
