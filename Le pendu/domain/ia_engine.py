from ui.constants import AI_LETTER_FREQUENCY

def analyze_frequencies(hidden_word, excluded_letters):
    """
    Analyse les lettres les plus fréquentes et retourne la première lettre
    qui n'a pas encore été utilisée.
    
    Args:
        hidden_word (str): le mot actuel du jeu (mot secret)
        excluded_letters (set): lettres déjà utilisées

    Returns:
        str | None: la lettre la plus probable ou None si aucune disponible
    """
    for letter in AI_LETTER_FREQUENCY:
        if letter not in excluded_letters:
            return letter
    return None  # toutes les lettres fréquentes sont utilisées


def get_best_move(state):
    """
    Détermine la meilleure lettre pour l'IA
    en fonction du mot caché et des lettres déjà utilisées.

    Args:
        state (GameState): instance de l'état du jeu

    Returns:
        str | None: la lettre choisie par l'IA
    """
    hidden_word = state.secret_word
    excluded_letters = state.used_letters

    return analyze_frequencies(hidden_word, excluded_letters)
