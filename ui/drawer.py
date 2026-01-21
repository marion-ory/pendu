import pygame
from ui.constant import *


def dessiner_pendu(surface, erreurs):
    # Couleur du pendu (Noir ou Marron)
    COULEUR_PENDU = (50, 30, 0)
    EPAISSEUR = 5

    # Étape 1 : Le socle
    if erreurs >= 1:
        pygame.draw.line(surface, COULEUR_PENDU, (100, 600), (300, 600), EPAISSEUR)
    # Étape 2 : Le poteau vertical
    if erreurs >= 2:
        pygame.draw.line(surface, COULEUR_PENDU, (200, 600), (200, 200), EPAISSEUR)
    # Étape 3 : La barre transversale
    if erreurs >= 3:
        pygame.draw.line(surface, COULEUR_PENDU, (200, 200), (400, 200), EPAISSEUR)
    # Étape 4 : La corde
    if erreurs >= 4:
        pygame.draw.line(surface, COULEUR_PENDU, (400, 200), (400, 250), EPAISSEUR)
    # Étape 5 : La tête
    if erreurs >= 5:
        pygame.draw.circle(surface, COULEUR_PENDU, (400, 280), 30, EPAISSEUR)
    # Étape 6 : Le corps
    if erreurs >= 6:
        pygame.draw.line(surface, COULEUR_PENDU, (400, 310), (400, 450), EPAISSEUR)
    # Étape 7 : Les bras et jambes (Le personnage complet)
    if erreurs >= 7:
        # Bras
        pygame.draw.line(surface, COULEUR_PENDU, (400, 350), (350, 400), EPAISSEUR)
        pygame.draw.line(surface, COULEUR_PENDU, (400, 350), (450, 400), EPAISSEUR)
        # Jambes
        pygame.draw.line(surface, COULEUR_PENDU, (400, 450), (350, 520), EPAISSEUR)
        pygame.draw.line(surface, COULEUR_PENDU, (400, 450), (450, 520), EPAISSEUR)
