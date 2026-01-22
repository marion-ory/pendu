import pygame
from ui.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, FONT_NAME
from ui.drawer import draw_background

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(FONT_NAME, 50, bold=True)

    def run(self):
        waiting = True
        choice = None
        while waiting:
            draw_background(self.screen) # Ton image de Konoha
            
            title = self.font.render("LE PENDU", True, WHITE)
            txt1 = self.font.render("1. Joueur vs IA", True, WHITE)
            txt2 = self.font.render("2. Deux joueurs humains", True, WHITE)
            
            self.screen.blit(title, (SCREEN_WIDTH//2 - 100, 150))
            self.screen.blit(txt1, (SCREEN_WIDTH//2 - 200, 300))
            self.screen.blit(txt2, (SCREEN_WIDTH//2 - 200, 400))
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        choice = "IA"
                        waiting = False
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        choice = "HUMAIN"
                        waiting = False
        return choice