from ui.constants import TURN_TIME_MS

def check_timer_expiry(current_ticks, timer_start):
    """
    Vérifie si le temps du tour est écoulé.
    
    Args:
        current_ticks (int): Temps actuel en millisecondes (pygame.time.get_ticks())
        timer_start (int): Temps de départ du tour en millisecondes
    
    Returns:
        bool: True si le temps est écoulé, False sinon
    """
    elapsed_time = current_ticks - timer_start
    return elapsed_time >= TURN_TIME_MS


def start_turn_timer(current_ticks):
    """
    Initialise le timer d'un tour à l'instant actuel.
    
    Args:
        current_ticks (int): Temps actuel en millisecondes
    
    Returns:
        int: Valeur du timer de départ (millisecondes)
    """
    return current_ticks
