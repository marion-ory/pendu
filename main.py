import pygame
import time
import random
import os
from ui.screen_manager import setup, display_menu, display_game, display_add_word, display_game_over, display_victory
from ui.constant import *
from pendu import logique

def load_highscore():
    if not os.path.exists("scores.txt"):
        return 0
    try:
        with open("scores.txt", "r") as f:
            lines = f.readlines()
            scores = []
            for line in lines:
                if "Score:" in line:
                    score_val = line.split("Score:")[1].split(",")[0].strip()
                    scores.append(int(score_val))
            return max(scores) if scores else 0
    except:
        return 0

screen = setup()
running = True
current_screen = "MENU"
new_word_input = ""
game_score = 0
highscore = load_highscore()
errors_count = 0
found_letters = []
final_time = 0
TIMER_DECREASE = pygame.USEREVENT + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "MENU":
                if RECT_PLAY.collidepoint(event.pos):
                    if os.path.exists("mot.txt"):
                        with open("mot.txt", "r") as f:
                            words = f.read().splitlines()
                        if words:
                            word_to_guess = random.choice(words).upper()
                            errors_count = 0
                            found_letters = []
                            game_score = 0
                            start_time = time.time()
                            current_screen = "GAME"
                            pygame.time.set_timer(TIMER_DECREASE, 5000)
                elif RECT_ADD_WORD.collidepoint(event.pos):
                    current_screen = "ADD_WORD"
                elif RECT_QUIT.collidepoint(event.pos):
                    running = False
            elif current_screen in ["GAME_OVER", "VICTORY"]:
                if RECT_BACK.collidepoint(event.pos):
                    highscore = load_highscore()
                    current_screen = "MENU"

        if event.type == TIMER_DECREASE and current_screen == "GAME":
            game_score = max(0, game_score - 5)

        if event.type == pygame.KEYDOWN:
            if current_screen == "GAME":
                if event.unicode.isalpha():
                    letter = event.unicode.upper()
                    if logique.check_letter(letter, word_to_guess, found_letters):
                        game_score += 10
                    else:
                        errors_count += 1
                    
                    if errors_count >= 7: 
                        pygame.time.set_timer(TIMER_DECREASE, 0)
                        current_screen = "GAME_OVER"
                    
                    if "_" not in logique.display_word(word_to_guess, found_letters):
                        pygame.time.set_timer(TIMER_DECREASE, 0)
                        final_time = round(time.time() - start_time, 2)
                        with open("scores.txt", "a") as f:
                            f.write(f"Date: {logique.get_current_date()}, Score: {game_score}, Time: {final_time}s\n")
                        current_screen = "VICTORY"
            
            elif current_screen == "ADD_WORD":
                if event.key == pygame.K_RETURN and new_word_input:
                    with open("mot.txt", "a") as f:
                        f.write(new_word_input.upper() + "\n")
                    new_word_input = ""
                    current_screen = "MENU"
                elif event.key == pygame.K_BACKSPACE:
                    new_word_input = new_word_input[:-1]
                elif event.unicode.isalpha():
                    new_word_input += event.unicode.upper()

    if current_screen == "MENU": 
        display_menu(screen, highscore)
    elif current_screen == "GAME":
        elapsed = int(time.time() - start_time)
        display_game(screen, word_to_guess, found_letters, errors_count, game_score, elapsed)
    elif current_screen == "ADD_WORD": 
        display_add_word(screen, new_word_input)
    elif current_screen == "GAME_OVER": 
        display_game_over(screen, word_to_guess)
    elif current_screen == "VICTORY":
        display_victory(screen, game_score, final_time)

    pygame.display.flip()

pygame.quit()