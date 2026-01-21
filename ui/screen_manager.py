import pygame
from ui.constant import *


def setup():
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Jeu du Pendu - Bachelor IA")
    return screen


def afficher_menu(surface):
    surface.fill(ECRAN)

    # 1. Définition des zones des boutons (x, y, largeur, hauteur)
    rect_jouer = pygame.Rect(LARGEUR // 2 - 100, 200, 200, 50)
    rect_ajouter = pygame.Rect(LARGEUR // 2 - 100, 300, 200, 50)
    rect_quitter = pygame.Rect(LARGEUR // 2 - 100, 400, 200, 50)

    # 2. Dessin des rectangles (Boutons)
    pygame.draw.rect(surface, WHITE, rect_jouer)
    pygame.draw.rect(surface, WHITE, rect_ajouter)
    pygame.draw.rect(surface, WHITE, rect_quitter)

    # 3. Création de la police
    font = pygame.font.SysFont("Arial", 24)

    # 4. Création des images de texte (Render)
    txt_jouer = font.render("1 - JOUER", True, BLEU)
    txt_ajouter = font.render("2 - AJOUTER", True, BLEU)
    txt_quitter = font.render("3 - QUITTER", True, BLEU)

    # 5. Affichage des textes sur les boutons (Blit)
    # On utilise center pour que le texte soit parfaitement au milieu du rectangle
    surface.blit(txt_jouer, txt_jouer.get_rect(center=rect_jouer.center))
    surface.blit(txt_ajouter, txt_ajouter.get_rect(center=rect_ajouter.center))
    surface.blit(txt_quitter, txt_quitter.get_rect(center=rect_quitter.center))


def afficher_jeu(surface, mot_a_deviner, lettres_trouvees):
    surface.fill(ECRAN)

    font = pygame.font.SysFont("Arial", 50)

    # 1. On récupère la chaîne de caractères (ex: "B _ C H _ L _ R")
    from logique import affciher_mot

    texte_mot = affciher_mot(mot_a_deviner, lettres_trouvees)

    # 2. Création de l'image du texte
    img_mot = font.render(texte_mot, True, WHITE)

    # 3. On centre le texte au milieu de l'écran (720x1280 selon tes constantes)
    rect_texte = img_mot.get_rect(center=(LARGEUR // 2, HAUTEUR // 2))
    surface.blit(img_mot, rect_texte)


def afficher_saisie_mot(surface, mot_en_cours):
    surface.fill(ECRAN)
    font = pygame.font.SysFont("Arial", 30)

    # Message d'instruction
    titre = font.render("Tapez le nouveau mot :", True, WHITE)
    surface.blit(titre, (50, 100))

    # Affichage de ce que l'utilisateur tape
    img_saisie = font.render(mot_en_cours, True, BLEU)
    surface.blit(img_saisie, (50, 200))

    # Aide en bas
    aide = font.render("Appuyez sur ENTREE pour valider", True, WHITE)
    surface.blit(aide, (50, 400))


# def afficher_score(surface, donnees_partie):

# def afficher_resultat(surface, gagne, score):
