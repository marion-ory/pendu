import logique
import datetime
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui.screen_manager import setup, afficher_menu, afficher_jeu, afficher_saisie_mot
from ui.constant import *
import ui.screen_manager as sm


# initialisation :

screen = sm.setup()
clock = pygame.time.Clock()
running = True
ecran_actuel = "MENU"  # On commence sur le menu
nom_joueur = "Joueur 1"
# BOUCLE JEU
# while True:
while running:

    for event in pygame.event.get():  # option pour fermer le jeu
        if event.type == pygame.QUIT:
            running = False

        # --- GESTION CLAVIER ---
        if event.type == pygame.KEYDOWN:

            # CAS 1 : DEPUIS LE MENU
            if ecran_actuel == "MENU":
                if event.key == pygame.K_1:  # jouer 1 correspond au print("1 - Jouer")
                    with open("mot.txt", "r", encoding="utf-8") as fichier:
                        liste_mot = fichier.read().splitlines()

                    if liste_mot:
                        debut_chronometre = time.time()  # debut chronometre
                        mot_a_deviner = logique.random.choice(liste_mot)
                        mon_niveau, points = logique.niveau_difficulte(mot_a_deviner)

                        # Initialisation de la partie
                        logique.compteur_erreur = 0
                        logique.lettre_trouve = []

                        # Basculer l'écran vers le jeu
                        ecran_actuel = "JEU"

                elif event.key == pygame.K_2:  # AJOUT MOT
                    ecran_actuel = "AJOUT_MOT"
                    nouveau_mot = ""  # On vide pour la nouvelle saisie

                elif event.key == pygame.K_3:  # Quitter
                    running = False

            # CAS 2 : SAISIE D'UN NOUVEAU MOT
            elif ecran_actuel == "AJOUT_MOT":
                if event.key == pygame.K_RETURN:  # Touche Entrée pour valider
                    if len(nouveau_mot) > 0:
                        nouveau_mot = nouveau_mot.strip().upper()
                        # L'ouverture du fichier doit être dans le case 2
                        with open("mot.txt", "a", encoding="utf-8") as fichier:
                            fichier.write(nouveau_mot + "\n")
                        print(f"Le mot '{nouveau_mot}' a bien été ajouté !")
                        ecran_actuel = "MENU"

                elif event.key == pygame.K_BACKSPACE:  # Effacer
                    nouveau_mot = nouveau_mot[:-1]

                elif event.unicode.isalpha():  # (seulement si c'est une lettre)
                    nouveau_mot += event.unicode.upper()

            # CAS 3 : PENDANT LA PARTIE (LE PENDU)
            elif ecran_actuel == "JEU":
                if event.unicode.isalpha() and len(event.unicode) == 1:
                    choix_lettre = event.unicode.upper()  # Tapez une lettre
                    logique.verifier_lettre(choix_lettre, mot_a_deviner)

                    # --- VERIFICATION DEFAITE (7 ERREURS) ---
                    if logique.compteur_erreur >= 7:
                        fin_chronometre = time.time()
                        temps_total = round(
                            fin_chronometre - debut_chronometre, 2
                        )  # Chrono total si perdu
                        print(f"Perdu... Le mot était : {mot_a_deviner}")
                        print(f"Temps de jeu : {temps_total}s")
                        ecran_actuel = "MENU"

                    # --- VERIFICATION VICTOIRE ---
                    else:
                        affichage = logique.affciher_mot(
                            mot_a_deviner, logique.lettre_trouve
                        )
                        if "_" not in affichage:
                            fin_chronometre = time.time()
                            temps_total = round(
                                fin_chronometre - debut_chronometre, 2
                            )  # Chrono total si gagné

                        # score final
                        score_final, bonus = logique.chrono_score(points, temps_total)

                        with open(
                            "scores.txt", "a", encoding="utf-8"
                        ) as f_scores:  # ajout dans score.TXT
                            f_scores.write(
                                f"Joueur : {nom_joueur}, Niveau: {mon_niveau}, Score : {score_final}, Bonus : {bonus}, Temps : {temps_total}s, le : {logique.date_actuelle}\n"
                            )

                        print(f"Gagné en {temps_total}s !")
                        ecran_actuel = "MENU"

    # --- PARTIE AFFICHAGE ---
    if ecran_actuel == "MENU":
        afficher_menu(screen)
    elif ecran_actuel == "JEU":
        # On appelle la nouvelle fonction avec TOUTES les infos nécessaires
        afficher_jeu(
            screen, mot_a_deviner, logique.lettre_trouve, logique.compteur_erreur
        )
    elif ecran_actuel == "AJOUT_MOT":
        screen.fill(ECRAN)

    pygame.display.flip()

pygame.quit()

# nom_joueur = input("Nom du joueur : ")
# print("Que souhaitez-vous faire ? ")
# print("1 - Jouer")
# # print("2 - Choisir un mot")
# print("3 - Quitter")
# choix = input("Votre choix : ")

# match choix:
#     case "1":  # JOUE
#         with open("mot.txt", "r", encoding="utf-8") as fichier:
#             liste_mot = fichier.read().splitlines()

#         if liste_mot:
#             debut_chronometre = time.time()  # debut chronometre
#             mot_a_deviner = logique.random.choice(liste_mot)
#             mon_niveau, points = logique.niveau_difficulte(mot_a_deviner)
#             print(f"Niveau : {mon_niveau}, Rapporte : {points} points")

#             logique.compteur_erreur = 0
#             logique.lettre_trouve = []
#             print(
#                 "Le mot à deviner :",
#                 logique.affciher_mot(mot_a_deviner, logique.lettre_trouve),
#             )

#             while logique.compteur_erreur <= 6:
#                 choix_lettre = input("Tapez une lettre : ").upper()
#                 logique.verifier_lettre(choix_lettre, mot_a_deviner)
#                 affichage = logique.affciher_mot(
#                     mot_a_deviner, logique.lettre_trouve
#                 )
#                 print(affichage)

#                 if "_" not in affichage:
#                     fin_chronometre = time.time()
#                     temps_total = round(
#                         fin_chronometre - debut_chronometre, 2
#                     )  # Chrono total si gagné
#                     score_final, bonus = logique.chrono_score(points, temps_total)
#                     print(f"Gagné en : {temps_total}s , Bonus rapidité + {bonus}")
#                     print(f"Score total final : {score_final}")
#                     with open(
#                         "scores.txt", "a", encoding="utf-8 "
#                     ) as f_scores:  # ajout dans score.TXT
#                         f_scores.write(
#                             f"Joueur :{  nom_joueur} , Niveau: { mon_niveau}, Score : { points} s , Bonus temps : { bonus}, en {temps_total}, le : {logique.date_actuelle}\n "
#                         )
#                     break
#                 if logique.compteur_erreur >= 6:
#                     fin_chronometre = time.time()
#                     temps_total = round(
#                         fin_chronometre - debut_chronometre, 2
#                     )  # Chrono total si perdu
#                     print(f"Perdu en : {temps_total}")
#                     break

#     # case "2":  # AJOUT MOT
#     #     ajout_mot = input("Ajoutez un mot à faire découvrir : ")
#     #     ajout_mot = ajout_mot.strip().upper()

#     #     # L'ouverture du fichier doit être dans le case 2
#     #     with open("mot.txt", "a", encoding="utf-8") as fichier:
#     #         fichier.write(ajout_mot + "\n")
#     #     print(f"Le mot '{ajout_mot}' a bien été ajouté !")

#     case "3":
#         break
