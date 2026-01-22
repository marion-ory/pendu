# controller/game_controller.py
import pygame
import time

from domain.game_logic import is_valid_input, check_letter
from domain.ia_engine import get_best_move
from domain.score_manager import save_player_score
from ui.constants import PENALTY, POINTS_PER_LETTER, AI_THINKING_DELAY_MS
from domain.turn_manager import TurnManager
from ui.drawer import draw_feedback  # pour afficher les messages
from domain.word_manager import select_random_word
from domain.game_logic import is_victory

class GameController:
    """
    Contrôleur principal du jeu.
    Gère :
    - tour humain et IA
    - timer et pénalités
    - score live et sauvegarde
    - lettres devinées et utilisées
    - messages feedback
    """

    def __init__(self, game_state):
        self.state = game_state
        self.turn_manager = TurnManager(game_state)
        self.ai_last_action_tick = 0  # pour gérer le délai IA non bloquant

    def handle_events(self, current_ticks, screen):
        """
        Retourne False si QUIT, True sinon
        """
        current_player = self.turn_manager.get_current_player()

        # -----------------------------
        # 1️⃣ Vérification du timer expiré
        # -----------------------------
        if self.turn_manager.check_time_expired(current_ticks):
            self.state.score -= PENALTY
            self.state.last_message = "Temps écoulé ! -1 point"
            self.turn_manager.switch_player(current_ticks)

        # -----------------------------
        # 2️⃣ Tour humain
        # -----------------------------
        if "Humain" in current_player or "Joueur" in current_player:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.KEYDOWN:
                    char = event.unicode.lower()

                    # Lettre valide ?
                    if not is_valid_input(char):
                        self.state.last_message = "Caractère invalide !"
                        draw_feedback(screen, self.state.last_message)
                        return True

                    # Lettre déjà utilisée ?
                    if char in self.state.used_letters:
                        self.state.last_message = "Lettre déjà utilisée !"
                        draw_feedback(screen, self.state.last_message)
                        return True

                    # Ajouter aux lettres utilisées
                    self.state.used_letters.add(char)

                    # Vérifier si correcte
                    if check_letter(char, self.state.secret_word):
                        self.state.found_letters.add(char)
                        self.state.add_score(POINTS_PER_LETTER)
                        self.state.last_message = "Super ! Continue comme ça !"
                        save_player_score(current_player, self.state.score)
                    else:
                        self.state.add_error()
                        self.state.last_message = "Dommage pour toi !"

                    draw_feedback(screen, self.state.last_message)

                    # Changer de joueur
                    self.turn_manager.switch_player(current_ticks)

        # -----------------------------
        # 3️⃣ Tour IA
        # -----------------------------
        elif current_player == "IA":
            # Vérifier si le délai IA est écoulé
            if current_ticks - self.ai_last_action_tick >= AI_THINKING_DELAY_MS:
                letter = get_best_move(self.state)

                if letter:
                    self.state.used_letters.add(letter)

                    if check_letter(letter, self.state.secret_word):
                        self.state.found_letters.add(letter)
                        self.state.add_score(POINTS_PER_LETTER)
                        self.state.last_message = "IA a trouvé une lettre ! +3 points"
                        save_player_score("IA", self.state.score)
                    else:
                        self.state.add_error()
                        self.state.last_message = "IA a fait une erreur !"

                    draw_feedback(screen, self.state.last_message)

                # Switch joueur après action IA
                self.turn_manager.switch_player(current_ticks)
                self.ai_last_action_tick = current_ticks

        return True

def check_end_game(self):
    # On vérifie si toutes les lettres du mot secret sont dans found_letters
    if is_victory(self.state.secret_word, self.state.found_letters):
        winner = self.turn_manager.get_current_player()
        self.state.last_message = f"BRAVO ! {winner} a remporté la manche !"
        return True
    return False

def reset_round(self):
    """Prépare la manche suivante avec un nouveau mot"""
    self.state.secret_word = select_random_word()
    self.state.found_letters = set()
    self.state.used_letters = set()
    self.state.errors_count = 0
    self.state.last_message = "Nouveau mot ! À vous de jouer."