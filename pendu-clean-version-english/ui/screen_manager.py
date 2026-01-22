import pygame
from ui.constant import *
from ui.drawer import draw_hangman
from pendu import logique
import random

class EmojiRain:
    def __init__(self, emoji_list):
        # On crée 30 particules pour une pluie dense
        self.particles = []
        for _ in range(30):
            self.particles.append({
                'x': random.randint(0, 1280),
                'y': random.randint(-720, 0),
                'char': random.choice(emoji_list),
                'speed': random.randint(4, 8)
            })

    def update_and_draw(self, surface, font):
        for p in self.particles:
            p['y'] += p['speed']
            # Reset quand l'emoji sort de l'écran
            if p['y'] > 720:
                p['y'] = -50
                p['x'] = random.randint(0, 1280)
            
            img = font.render(p['char'], True, (255, 255, 255))
            surface.blit(img, (p['x'], p['y']))


rain_game = EmojiRain(["🔪", "🔥"])     # Shuriken et Feu
rain_lose = EmojiRain(["👎"])           # Pouce retourné
rain_win = EmojiRain(["😍", "🎊"])       # Yeux coeur et Confettis


def draw_button(surface, text, rect, bg_color):
    pygame.draw.rect(surface, bg_color, rect, border_radius=10)
    pygame.draw.rect(surface, WHITE, rect, 2, border_radius=10)
    font = pygame.font.SysFont("Arial", 22, bold=True)
    img_txt = font.render(text, True, WHITE)
    surface.blit(img_txt, img_txt.get_rect(center=rect.center))

def setup():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT))

def display_menu(surface, highscore):
    
    
    # Titre et Record
    font_title = pygame.font.SysFont("Arial", 80, bold=True)
    img_title = font_title.render("HANGMAN", True, WHITE)
    surface.blit(img_title, img_title.get_rect(center=(WIDTH // 2, 80)))
    
    font_record = pygame.font.SysFont("Arial", 30, bold=True)
    img_record = font_record.render(f"BEST SCORE: {highscore}", True, GOLD)
    surface.blit(img_record, img_record.get_rect(center=(WIDTH // 2, 160)))

    # Boutons de difficulté (espacement de 55px entre chaque)
    draw_button(surface, "EASY (<= 6)", pygame.Rect(X_CENTER, 220, BTN_WIDTH, 45), (50, 150, 50))
    draw_button(surface, "MEDIUM (7-10)", pygame.Rect(X_CENTER, 275, BTN_WIDTH, 45), (150, 150, 50))
    draw_button(surface, "HARD (=> 10)", pygame.Rect(X_CENTER, 330, BTN_WIDTH, 45), (150, 50, 50))
    
    # Boutons utilitaires (descendus pour laisser de la place)
    draw_button(surface, "ADD WORD", pygame.Rect(X_CENTER, 400, BTN_WIDTH, 45), BLUE)
    draw_button(surface, "QUIT", pygame.Rect(X_CENTER, 455, BTN_WIDTH, 45), RED)

def display_game(surface, word, letters, errors, score, elapsed_time):
    font_e = pygame.font.SysFont("Segoe UI Symbol", 35)
    rain_game.update_and_draw(surface, font_e)
    # Ton code habituel suit ici...
    
    draw_hangman(surface, errors)
    font_info = pygame.font.SysFont("Arial", 25, bold=True)
    surface.blit(font_info.render(f"Errors: {errors} / 11", True, WHITE), (20, 20))
    surface.blit(font_info.render(f"Score: {score}", True, WHITE), (20, 55))
    surface.blit(font_info.render(f"Time: {elapsed_time}s", True, GOLD), (20, 90))
    
    display_txt = logique.display_word(word, letters)
    font_size = 70
    test_font = pygame.font.SysFont("Arial", font_size, bold=True)
    
    while test_font.size(display_txt)[0] > (WIDTH - 60) and font_size > 20:
        font_size -= 5
        test_font = pygame.font.SysFont("Arial", font_size, bold=True)
        
    img_word = test_font.render(display_txt, True, BLACK )
    surface.blit(img_word, img_word.get_rect(center=(WIDTH // 2, HEIGHT - 100)))

def display_victory(surface, score, time_spent):
    surface.fill((20, 60, 20))

    font = pygame.font.SysFont("Arial", 80, bold=True)
    img = font.render("VICTORY!", True, GOLD)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, 150)))
    font_e = pygame.font.SysFont("Segoe UI Symbol", 35)
    rain_win.update_and_draw(surface, font_e)
    font_stats = pygame.font.SysFont("Arial", 40)
    surface.blit(font_stats.render(f"Final Score: {score}", True, WHITE), font_stats.render(f"Final Score: {score}", True, WHITE).get_rect(center=(WIDTH // 2, 250)))
    surface.blit(font_stats.render(f"Time: {time_spent}s", True, WHITE), font_stats.render(f"Time: {time_spent}s", True, WHITE).get_rect(center=(WIDTH // 2, 310)))
    
    draw_button(surface, "BACK TO MENU", pygame.Rect(X_CENTER, 420, BTN_WIDTH, 50), BLUE)

def display_game_over(surface, correct_word):
    surface.fill((50, 0, 0))
    font_e = pygame.font.SysFont("Segoe UI Symbol", 35)
    rain_lose.update_and_draw(surface, font_e)
    font = pygame.font.SysFont("Arial", 80, bold=True)
    img = font.render("GAME OVER!", True, WHITE)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, 150)))
    
    font_m = pygame.font.SysFont("Arial", 30)
    img_m = font_m.render(f"The word was: {correct_word}", True, WHITE)
    surface.blit(img_m, img_m.get_rect(center=(WIDTH // 2, 260)))
    draw_button(surface, "BACK TO MENU", pygame.Rect(X_CENTER, 420, BTN_WIDTH, 50), BLUE)

def display_add_word(surface, current_input):
    
    font = pygame.font.SysFont("Arial", 50)
    img = font.render("Word: " + current_input + "_", True, WHITE)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, HEIGHT // 2)))