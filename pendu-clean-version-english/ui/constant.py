import pygame

# Dimensions ajustées
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Pour garder la compatibilité avec tes autres fichiers qui utilisent peut-être WIDTH/HEIGHT
WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 100, 200)
RED = (150, 0, 0)
GOLD = (255, 215, 0)
GREEN = (50, 200, 50)

BTN_WIDTH = 250
BTN_HEIGHT = 50
X_CENTER = (WIDTH // 2) - (BTN_WIDTH // 2)

RECT_PLAY = pygame.Rect(X_CENTER, 300, BTN_WIDTH, BTN_HEIGHT)
RECT_ADD_WORD = pygame.Rect(X_CENTER, 370, BTN_WIDTH, BTN_HEIGHT)
RECT_QUIT = pygame.Rect(X_CENTER, 440, BTN_WIDTH, BTN_HEIGHT)
RECT_BACK = pygame.Rect(X_CENTER, 550, BTN_WIDTH, BTN_HEIGHT)

