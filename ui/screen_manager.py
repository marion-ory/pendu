import pygame
from ui.constant import *
from ui.drawer import draw_hangman
from pendu import logique

def draw_button(surface, text, rect, bg_color):
    pygame.draw.rect(surface, bg_color, rect, border_radius=10)
    pygame.draw.rect(surface, WHITE, rect, 2, border_radius=10)
    font = pygame.font.SysFont("Arial", 30, bold=True)
    img_txt = font.render(text, True, WHITE)
    surface.blit(img_txt, img_txt.get_rect(center=rect.center))

def setup():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT))

def display_menu(surface, highscore):
    surface.fill(SCREEN_COLOR)
    font_title = pygame.font.SysFont("Arial", 80, bold=True)
    img_title = font_title.render("HANGMAN", True, WHITE)
    surface.blit(img_title, img_title.get_rect(center=(WIDTH // 2, 100)))
    
    font_record = pygame.font.SysFont("Arial", 30, bold=True)
    img_record = font_record.render(f"BEST SCORE: {highscore}", True, GOLD)
    surface.blit(img_record, img_record.get_rect(center=(WIDTH // 2, 180)))

    draw_button(surface, "PLAY", RECT_PLAY, BLUE)
    draw_button(surface, "ADD WORD", RECT_ADD_WORD, BLUE)
    draw_button(surface, "QUIT", RECT_QUIT, RED)

def display_game(surface, word, letters, errors, score, elapsed_time):
    surface.fill(SCREEN_COLOR)
    draw_hangman(surface, errors)
    font_info = pygame.font.SysFont("Arial", 30, bold=True)
    surface.blit(font_info.render(f"Errors: {errors} / 7", True, WHITE), (30, 30))
    surface.blit(font_info.render(f"Score: {score}", True, WHITE), (30, 70))
    surface.blit(font_info.render(f"Time: {elapsed_time}s", True, GOLD), (30, 110))
    
    font_word = pygame.font.SysFont("Arial", 70, bold=True)
    img_word = font_word.render(logique.display_word(word, letters), True, WHITE)
    surface.blit(img_word, img_word.get_rect(center=(WIDTH // 2, HEIGHT - 100)))

def display_victory(surface, score, time_spent):
    surface.fill((20, 60, 20))
    font = pygame.font.SysFont("Arial", 80, bold=True)
    img = font.render("VICTORY!", True, GOLD)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, 150)))
    
    font_stats = pygame.font.SysFont("Arial", 40)
    img_score = font_stats.render(f"Final Score: {score}", True, WHITE)
    img_time = font_stats.render(f"Time: {time_spent}s", True, WHITE)
    
    surface.blit(img_score, img_score.get_rect(center=(WIDTH // 2, 250)))
    surface.blit(img_time, img_time.get_rect(center=(WIDTH // 2, 310)))
    draw_button(surface, "BACK TO MENU", RECT_BACK, BLUE)

def display_game_over(surface, correct_word):
    surface.fill((50, 0, 0))
    font = pygame.font.SysFont("Arial", 80, bold=True)
    img = font.render("GAME OVER!", True, WHITE)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, 150)))
    
    font_m = pygame.font.SysFont("Arial", 30)
    img_m = font_m.render(f"The word was: {correct_word}", True, WHITE)
    surface.blit(img_m, img_m.get_rect(center=(WIDTH // 2, 250)))
    draw_button(surface, "BACK TO MENU", RECT_BACK, BLUE)

def display_add_word(surface, current_input):
    surface.fill(SCREEN_COLOR)
    font = pygame.font.SysFont("Arial", 50)
    img = font.render("Word: " + current_input + "_", True, WHITE)
    surface.blit(img, img.get_rect(center=(WIDTH // 2, HEIGHT // 2)))