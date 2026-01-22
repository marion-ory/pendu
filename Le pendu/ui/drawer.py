import pygame
import os
from ui.constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    BACKGROUND_IMAGE_PATH,
    WHITE, HANGMAN_COLOR,
    TIMER_GREEN, TIMER_RED,
    FONT_NAME, FONT_SMALL, FONT_MEDIUM, FONT_LARGE,
    TIMER_LIMIT_MS
)



def load_background():
    global _background_image
    # On construit le chemin absolu pour éviter les erreurs de dossier
    current_dir = os.getcwd() 
    full_path = os.path.join(current_dir, "images", "Background2.jpg")
    
    if os.path.exists(full_path):
        image = pygame.image.load(full_path)
        _background_image = image.convert()
        _background_image = pygame.transform.scale(_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        print(f"ALERTE : Image non trouvée à l'adresse : {full_path}")
        _background_image = None

        
def draw_background(screen):
    if _background_image:
        screen.blit(_background_image, (0, 0))
    else:
        screen.fill((30, 30, 30))

    # AJOUT DE L'OVERLAY (Voile léger bleu nuit pour le contraste) 
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((20, 20, 60, 80))  # Bleu très foncé, opacité 80/255
    screen.blit(overlay, (0, 0))

def _get_font(size, bold=False):
    font = pygame.font.SysFont(FONT_NAME, size)
    if bold:
        font.set_bold(True)
    return font

def draw_feedback(screen, message):
    # Message en GRAS et BLANC
    font = _get_font(FONT_MEDIUM, bold=True)
    text = font.render(message, True, WHITE)
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, 120))
    screen.blit(text, rect)

def draw_current_turn(screen, current_player_name):
    message = "Tour de l'IA" if current_player_name == "IA" else "À ton tour"
    font = _get_font(FONT_SMALL, bold=True)
    text = font.render(message, True, WHITE)
    screen.blit(text, (20, SCREEN_HEIGHT - 60))

def draw_score(screen, score):
    # Score en BLANC au centre
    font = _get_font(FONT_MEDIUM, bold=True)
    text = font.render(f"Score : {score}", True, WHITE)
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, 40))
    screen.blit(text, rect)

def draw_timer_bar(screen, current_ticks, timer_start):
    elapsed = current_ticks - timer_start
    remaining_ratio = max(0, 1 - elapsed / TIMER_LIMIT_MS)
    bar_width = int(SCREEN_WIDTH * remaining_ratio)
    color = TIMER_GREEN if remaining_ratio > 0.3 else TIMER_RED
    
    # Barre de timer plus visible
    pygame.draw.rect(screen, color, (0, SCREEN_HEIGHT - 20, bar_width, 20))
    pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20), 2)

def draw_hangman(screen, errors):
    # On déplace le pendu plus vers le CENTRE et on le met en GRAS (épaisseur 6)
    # Centre approximatif x=SCREEN_WIDTH//2 - 100
    base_x = SCREEN_WIDTH // 2 - 150
    base_y = 550
    color = WHITE # Le pendu en blanc pour ressortir sur le voile bleu
    thick = 6     # Épaisseur du trait pour l'effet "Gras"

    # Potence
    if errors >= 1: pygame.draw.line(screen, color, (base_x, base_y), (base_x + 200, base_y), thick)
    if errors >= 2: pygame.draw.line(screen, color, (base_x + 50, base_y), (base_x + 50, base_y - 350), thick)
    if errors >= 3: pygame.draw.line(screen, color, (base_x + 50, base_y - 350), (base_x + 200, base_y - 350), thick)
    if errors >= 4: pygame.draw.line(screen, color, (base_x + 200, base_y - 350), (base_x + 200, base_y - 300), thick)

    # Personnage
    if errors >= 5: pygame.draw.circle(screen, color, (base_x + 200, base_y - 275), 25, thick) # Tête
    if errors >= 6: pygame.draw.line(screen, color, (base_x + 200, base_y - 250), (base_x + 200, base_y - 150), thick) # Corps
    if errors >= 7: pygame.draw.line(screen, color, (base_x + 200, base_y - 230), (base_x + 160, base_y - 190), thick) # Bras G
    if errors >= 8: pygame.draw.line(screen, color, (base_x + 200, base_y - 230), (base_x + 240, base_y - 190), thick) # Bras D
    if errors >= 9: pygame.draw.line(screen, color, (base_x + 200, base_y - 150), (base_x + 170, base_y - 80), thick)  # Jambe G
    if errors >= 10: pygame.draw.line(screen, color, (base_x + 200, base_y - 150), (base_x + 230, base_y - 80), thick) # Jambe D
