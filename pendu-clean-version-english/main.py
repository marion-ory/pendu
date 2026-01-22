import pygame
import time
import random
import os

from ui.screen_manager import (
    setup,
    display_menu,
    display_game,
    display_add_word,
    display_game_over,
    display_victory
)
from ui.constant import *
from pendu import logique

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sonor/music_font.mp3")  # Remplace par le nom exact de ton fichier
pygame.mixer.music.play(-1)  # Boucle infinie

# Effet sonore de victoire
victory_sound = pygame.mixer.Sound("sonor/gagner.mp3")

game_over = pygame.mixer.Sound("sonor/perdu.mp3")



# FENÊTRE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Le pendu de Konoha")

clock = pygame.time.Clock()


# BACKGROUND 

background = pygame.image.load("images/Background2.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# FONCTIONS

def load_highscore():
    if not os.path.exists("scores.txt"):
        return 0
    try:
        with open("scores.txt", "r") as f:
            scores = [
                int(line.split("Score:")[1].split(",")[0].strip())
                for line in f if "Score:" in line
            ]
            return max(scores) if scores else 0
    except:
        return 0


# VARIABLES JEU

screen = setup()
running = True
current_screen = "MENU"

new_word_input = ""
game_score = 0
errors_count = 0
found_letters = []
word_to_guess = ""

highscore = load_highscore()

TIMER_DECREASE = pygame.USEREVENT + 1

# Zones de clic
RECT_EASY = pygame.Rect(X_CENTER, 220, BTN_WIDTH, 45)
RECT_MEDIUM = pygame.Rect(X_CENTER, 275, BTN_WIDTH, 45)
RECT_HARD = pygame.Rect(X_CENTER, 330, BTN_WIDTH, 45)
RECT_ADD = pygame.Rect(X_CENTER, 400, BTN_WIDTH, 45)
RECT_QUIT_MENU = pygame.Rect(X_CENTER, 455, BTN_WIDTH, 45)
RECT_RETOUR_FIN = pygame.Rect(X_CENTER, 420, BTN_WIDTH, 50)



while running:
    clock.tick(FPS)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "MENU":
                difficulty = None
                if RECT_EASY.collidepoint(event.pos):
                    difficulty = "EASY"
                elif RECT_MEDIUM.collidepoint(event.pos):
                    difficulty = "MEDIUM"
                elif RECT_HARD.collidepoint(event.pos):
                    difficulty = "HARD"

                if difficulty:
                    if os.path.exists("mot.txt"):
                        with open("mot.txt", "r", encoding="utf-8") as f:
                            words = f.read().splitlines()
                        filtered = logique.filter_words_by_difficulty(words, difficulty)
                        if filtered:
                            word_to_guess = random.choice(filtered).upper()
                            errors_count = 0
                            game_score = 0
                            found_letters = []
                            start_time = time.time()
                            current_screen = "GAME"
                            pygame.time.set_timer(TIMER_DECREASE, 5000)

                elif RECT_ADD.collidepoint(event.pos):
                    current_screen = "ADD_WORD"
                elif RECT_QUIT_MENU.collidepoint(event.pos):
                    running = False

            elif current_screen in ["GAME_OVER", "VICTORY"]:
                if RECT_RETOUR_FIN.collidepoint(event.pos):
                    highscore = load_highscore()
                    current_screen = "MENU"

        if event.type == TIMER_DECREASE and current_screen == "GAME":
            game_score = max(0, game_score - 5)

        if event.type == pygame.KEYDOWN:
            if current_screen == "GAME" and event.unicode.isalpha():
                letter = event.unicode.upper()
                if logique.check_letter(letter, word_to_guess, found_letters):
                    game_score += 10
                else:
                    errors_count += 1

                if errors_count >= 11:
                    pygame.time.set_timer(TIMER_DECREASE, 0)

                    game_over.play()

                    current_screen = "GAME_OVER"

                elif "_" not in logique.display_word(word_to_guess, found_letters):
                    pygame.time.set_timer(TIMER_DECREASE, 0)
                    final_time = round(time.time() - start_time, 2)
                    with open("scores.txt", "a") as f:
                        f.write(
                            f"Date: {logique.get_current_date()}, "
                            f"Score: {game_score}, Time: {final_time}s\n"
                        )

                        victory_sound.play()
                    current_screen = "VICTORY"

            elif current_screen == "ADD_WORD":
                if event.key == pygame.K_RETURN and new_word_input:
                    with open("mot.txt", "a", encoding="utf-8") as f:
                        f.write(new_word_input.upper() + "\n")
                    new_word_input = ""
                    current_screen = "MENU"
                elif event.key == pygame.K_BACKSPACE:
                    new_word_input = new_word_input[:-1]
                elif event.unicode.isalpha():
                    new_word_input += event.unicode.upper()

    
    screen.blit(background, (0, 0))  

    if current_screen == "MENU":
        display_menu(screen, highscore)
    elif current_screen == "GAME":
        display_game(
            screen,
            word_to_guess,
            found_letters,
            errors_count,
            game_score,
            int(time.time() - start_time)
        )
    elif current_screen == "ADD_WORD":
        display_add_word(screen, new_word_input)
    elif current_screen == "GAME_OVER":
        display_game_over(screen, word_to_guess)
    elif current_screen == "VICTORY":
        display_victory(
            screen,
            game_score,
            round(time.time() - start_time, 2)
        )

    pygame.display.flip()

pygame.quit()
