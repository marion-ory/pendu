import pygame
from ui import drawer
from ui.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class GameScreen:
    def __init__(self, game_state):
        self.state = game_state

    def draw(self, screen, current_ticks):
        # 1. Fond (Affiche l'image ou le rectangle gris si image absente)
        drawer.draw_background(screen)

        # 2. Pendu (Central et Blanc)
        drawer.draw_hangman(screen, self.state.errors_count)

        # 3. Timer
        drawer.draw_timer_bar(screen, current_ticks, self.state.timer_start)

        # 4. Score
        drawer.draw_score(screen, self.state.score)

        # 5. Affichage du mot secret (C'est ici que ça plantait)
        self._draw_word_display(screen)

        # 6. Messages de feedback
        if hasattr(self.state, "last_message") and self.state.last_message:
            drawer.draw_feedback(screen, self.state.last_message)

        # 7. Tour actuel
        drawer.draw_current_turn(screen, self.state.get_current_player())

    def _draw_word_display(self, screen):
        """Affiche les lettres trouvées et les tirets _ _ _"""
        # On utilise une police large
        font = pygame.font.SysFont("arial", 60, bold=True)
        
        # Construction de la chaîne (ex: "K O N _ H _")
        display_text = ""
        # On utilise secret_word et found_letters pour correspondre au controller
        for letter in self.state.secret_word:
            if letter in self.state.found_letters:
                display_text += letter.upper() + " "
            else:
                display_text += "_ "
        
        text_surface = font.render(display_text.strip(), True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120))
        
        # Ombre pour la visibilité
        shadow = font.render(display_text.strip(), True, (0, 0, 0))
        screen.blit(shadow, (text_rect.x + 2, text_rect.y + 2))
        
        screen.blit(text_surface, text_rect)