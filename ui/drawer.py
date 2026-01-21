import pygame
from ui.constant import *

# Fonctions de dessin pur (pendu, textes)


def dessiner_pendu(surface, erreurs):
    # Exemple : dessiner la base si erreurs > 0
    if erreurs == 0:
        pygame.draw.line(surface, NOIR, (100, 500), (300, 500), 5)
    if erreurs == 1:
        pygame.draw.line(BLEU)
