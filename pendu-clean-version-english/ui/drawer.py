import pygame
from ui.constant import WIDTH

def draw_hangman(surface, errors):
    C = (0,0,0)
    BODY_C = (255, 182, 193)
    E = 6
    X = WIDTH // 2 - 220
    Y_BASE = 580

    # LA POTENCE 
    if errors >= 1: pygame.draw.line(surface, C, (X, Y_BASE), (X + 200, Y_BASE), E)
    if errors >= 2: pygame.draw.line(surface, C, (X + 50, Y_BASE), (X + 50, Y_BASE - 350), E)
    if errors >= 3: pygame.draw.line(surface, C, (X + 50, Y_BASE - 350), (X + 200, Y_BASE - 350), E)
    if errors >= 4: pygame.draw.line(surface, C, (X + 200, Y_BASE - 350), (X + 200, Y_BASE - 300), E)

    # LE BONHOMME 
    if errors >= 5: 
        pygame.draw.circle(surface, BODY_C, (X + 200, Y_BASE - 270), 30) # Tête centrée
        pygame.draw.circle(surface, (0,0,0), (X + 200, Y_BASE - 270), 30, 2)
    if errors >= 6: 
        pygame.draw.line(surface, (0,0,0), (X + 200, Y_BASE - 240), (X + 200, Y_BASE - 130), E) # Corps
    if errors >= 7: 
        pygame.draw.line(surface, (0,0,0), (X + 200, Y_BASE - 210), (X + 160, Y_BASE - 160), E) # Bras gauche
    if errors >= 8: 
        pygame.draw.line(surface, (0,0,0), (X + 200, Y_BASE - 210), (X + 240, Y_BASE - 160), E) # Bras droit
    if errors >= 9: 
        pygame.draw.line(surface, (0,0,0), (X + 200, Y_BASE - 130), (X + 160, Y_BASE - 70), E) # Jambe gauche
    if errors >= 10: 
        pygame.draw.line(surface, (0,0,0), (X + 200, Y_BASE - 130), (X + 240, Y_BASE - 70), E) # Jambe droite