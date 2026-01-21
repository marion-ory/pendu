import pygame
from ui.constant import WIDTH

def draw_hangman(surface, errors):
    C = (200, 200, 200)
    BODY_C = (255, 182, 193)
    E = 6
    X = WIDTH // 2 - 50
    Y_BASE = 450

    if errors >= 1:
        pygame.draw.line(surface, C, (X-100, Y_BASE), (X+100, Y_BASE), E)
        pygame.draw.line(surface, C, (X, Y_BASE), (X, Y_BASE-300), E)
        pygame.draw.line(surface, C, (X, Y_BASE-300), (X+150, Y_BASE-300), E)
        pygame.draw.line(surface, C, (X+150, Y_BASE-300), (X+150, Y_BASE-250), E)
        pygame.draw.line(surface, C, (X, Y_BASE-250), (X+50, Y_BASE-300), E)
    if errors >= 2:
        pygame.draw.circle(surface, BODY_C, (X+150, Y_BASE-220), 30)
        pygame.draw.circle(surface, (0,0,0), (X+150, Y_BASE-220), 30, 2)
    if errors >= 3: pygame.draw.line(surface, (0,0,0), (X+150, Y_BASE-190), (X+150, Y_BASE-80), E)
    if errors >= 4: pygame.draw.line(surface, (0,0,0), (X+150, Y_BASE-160), (X+110, Y_BASE-110), E)
    if errors >= 5: pygame.draw.line(surface, (0,0,0), (X+150, Y_BASE-160), (X+190, Y_BASE-110), E)
    if errors >= 6: pygame.draw.line(surface, (0,0,0), (X+150, Y_BASE-80), (X+110, Y_BASE-20), E)
    if errors >= 7: pygame.draw.line(surface, (0,0,0), (X+150, Y_BASE-80), (X+190, Y_BASE-20), E)