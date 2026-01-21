import pygame
from constant import *
from drawer import dessiner_pendu
import logique


def afficher_jeu(surface, mot_a_deviner, lettres_trouvees, erreurs):
    surface.fill(ECRAN)

    # 1. Dessiner le pendu (via drawer.py)
    dessiner_pendu(surface, erreurs)

    # 2. Afficher le mot avec underscores
    font_mot = pygame.font.SysFont("Arial", 60)
    # On utilise ta fonction logique pour avoir le "P _ T H _ N"
    mot_visuel = logique.affciher_mot(mot_a_deviner, lettres_trouvees)

    img_mot = font_mot.render(mot_visuel, True, WHITE)
    # On place le mot à droite du pendu
    rect_mot = img_mot.get_rect(center=(LARGEUR // 2 + 100, HAUTEUR // 2))
    surface.blit(img_mot, rect_mot)

    # 3. Afficher le compteur d'erreurs pour info
    font_info = pygame.font.SysFont("Arial", 24)
    txt_erreurs = font_info.render(f"Erreurs : {erreurs} / 7", True, WHITE)
    surface.blit(txt_erreurs, (20, 20))


def afficher_saisie_mot(surface, mot_en_cours):
    surface.fill(ECRAN)
    font = pygame.font.SysFont("Arial", 40)

    # 1. Message d'instruction
    texte_titre = font.render("Nouveau mot :", True, WHITE)
    surface.blit(texte_titre, (LARGEUR // 2 - 100, HAUTEUR // 4))

    # 2. Affichage du mot que l'utilisateur est en train de taper
    # On ajoute un curseur "_" à la fin pour le style
    image_saisie = font.render(mot_en_cours + "_", True, WHITE)
    rect_saisie = image_saisie.get_rect(center=(LARGEUR // 2, HAUTEUR // 2))

    # On dessine un rectangle pour souligner la saisie
    pygame.draw.rect(
        surface,
        WHITE,
        (rect_saisie.x - 10, rect_saisie.y + 50, rect_saisie.width + 20, 2),
        2,
    )
    surface.blit(image_saisie, rect_saisie)

    # 3. Aide en bas
    font_aide = pygame.font.SysFont("Arial", 20)
    aide = font_aide.render("Appuyez sur ENTREE pour valider", True, WHITE)
    surface.blit(aide, (LARGEUR // 2 - 120, HAUTEUR - 100))
