class GameState:
    def __init__(self, word):
        self.secret_word = word
        self.found_letters = set()    # Pour les bonnes lettres
        self.used_letters = set()     # Pour toutes les lettres tentées
        self.errors_count = 0
        self.score = 0
        self.timer_start = 0
        self.last_message = ""
        self.current_player = "Humain"
        self.players = ["Humain", "IA"] # Ajouté pour le TurnManager
        self.current_player_index = 0

    def get_current_player(self):
        return self.players[self.current_player_index]

    def add_error(self):
        self.errors_count += 1
        
    def add_score(self, points):
        self.score += points
    
    # Timer
    def reset_timer(self, current_ticks):
        
        #Réinitialise le départ du timer pour le joueur courant
        
        self.timer_start = current_ticks
