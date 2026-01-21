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
    # On les centre en utilisant tes constantes LARGEUR et HAUTEUR
    rect_jouer = pygame.Rect(LARGEUR // 2 - 100, 200, 200, 50)
    rect_ajouter = pygame.Rect(LARGEUR // 2 - 100, 300, 200, 50)
    rect_quitter = pygame.Rect(LARGEUR // 2 - 100, 400, 200, 50)

    # 2. Dessin des rectangles (Boutons)
    pygame.draw.rect(surface, WHITE, rect_jouer)
    pygame.draw.rect(surface, WHITE, rect_ajouter)
    pygame.draw.rect(surface, WHITE, rect_quitter)

    # 3. Ajout du texte sur les boutons
    font = pygame.font.SysFont("Arial", 24)


# def afficher_score(surface, donnees_partie):

# def afficher_resultat(surface, gagne, score):
