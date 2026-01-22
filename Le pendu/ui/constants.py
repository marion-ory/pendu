# ==========================================
# CONFIGURATION DE LA FENÊTRE
# ==========================================
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# ==========================================
# CHEMINS DES FICHIERS (Alias de compatibilité)
# ==========================================
# Pour word_manager.py et game_controller.py
WORDS_FILE = "mots.txt"
WORDS_FILE_PATH = "mots.txt"

# Pour score_manager.py
SCORES_FILE = "scores.txt"
SCORES_FILE_PATH = "scores.txt"


# Modifiez ces lignes exactement comme ceci :
BACKGROUND_IMAGE_PATH = "Background2.jpg"
BG_IMAGE_PATH = "images/Background2.jpg"


# ==========================================
# RÈGLES DE JEU ET SCORE
# ==========================================
TIMER_LIMIT = 30 
TIMER_LIMIT_MS = TIMER_LIMIT * 1000

# AJOUTEZ CETTE LIGNE :
TURN_TIME_MS = TIMER_LIMIT_MS  # Pour satisfaire domain/timer_logic.py

MAX_ERRORS = 10
PENALTY = 50 
POINTS_PER_LETTER = 20

# ==========================================
# COULEURS (RGB)
# ==========================================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEXT_COLOR = (30, 30, 30)
HANGMAN_COLOR = (0, 0, 0)
TIMER_GREEN = (0, 200, 0)
TIMER_RED = (200, 0, 0)
ERROR_COLOR = TIMER_RED
SUCCESS_COLOR = TIMER_GREEN
BACKGROUND_COLOR = (245, 245, 245)

# ==========================================
# POLICES
# ==========================================
FONT_NAME = "arial"
FONT_SMALL = 20
FONT_MEDIUM = 28
FONT_LARGE = 36

# ==========================================
# IA — CONFIGURATION (Alias de compatibilité)
# ==========================================
# Pour ia_engine.py et game_controller.py
AI_LETTER_FREQUENCY = [
    "e", "s", "a", "i", "t", "n", "r", "o", "l", "u",
    "d", "c", "m", "p", "g", "b", "v", "h", "f", "q",
    "y", "x", "j", "k", "w", "z"
]
LETTER_FREQUENCIES = AI_LETTER_FREQUENCY

# Délai de réflexion visuel
AI_THINKING_DELAY_MS = 1500