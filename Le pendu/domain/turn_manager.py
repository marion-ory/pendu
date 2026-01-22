from ui.constants import TIMER_LIMIT_MS, PENALTY
from domain.timer_logic import check_timer_expiry

class TurnManager:
    """
    Le "maître du jeu" qui gère :
    - l'alternance des joueurs
    - le timer de chaque tour
    - l'application des pénalités si le temps est dépassé
    """

    def __init__(self, game_state):
        """
        Args:
            game_state: instance de GameState
        """
        self.state = game_state

    # ----------------------
    # Retourne le joueur actif ("Humain" ou "IA")
    # ----------------------
    def get_current_player(self):
        return self.state.get_current_player()

    # ----------------------
    # Passe au joueur suivant et réinitialise le timer
    # ----------------------
    def switch_player(self, current_ticks):
        self.state.current_player_index = (self.state.current_player_index + 1) % len(self.state.players)
        self.reset_timer(current_ticks)

    # ----------------------
    # Réinitialise le timer du tour
    # ----------------------
    def reset_timer(self, current_ticks):
        self.state.timer_start = current_ticks

    # ----------------------
    # Vérifie si le temps du tour est expiré
    # ----------------------
    def check_time_expired(self, current_ticks):
        """
        Retourne True si le temps imparti est écoulé et applique la pénalité
        """
        if check_timer_expiry(current_ticks, self.state.timer_start):
            # Appliquer pénalité au joueur actuel
            self.state.score -= PENALTY
            # Passer au joueur suivant
            self.switch_player(current_ticks)
            return True
        return False

