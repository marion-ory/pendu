import pygame
from ui.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from ui.drawer import load_background, draw_background
from models.game_state import GameState
from controller.game_controller import GameController
from ui.screen_manager import GameScreen
from domain.word_manager import select_random_word

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Le Pendu de Konoha")
    
    # 1. Charger l'image (utilise le chemin de constants.py)
    load_background() 
    
    # 2. Initialiser l'état du jeu
    word = select_random_word()
    state = GameState(word)
    
    # Correction cruciale pour la compatibilité avec ton GameController
    state.used_letters = set()
    state.found_letters = set()
    state.players = ["Humain", "IA"] # Pour ton TurnManager
    state.current_player_index = 0
    
    controller = GameController(state)
    game_view = GameScreen(state)
    
    clock = pygame.time.Clock()
    running = True

    while running:
        current_ticks = pygame.time.get_ticks()
        
        # Gère les entrées clavier directement dans la fenêtre
        running = controller.handle_events(current_ticks, screen)
        
        # Dessine l'image de fond et le jeu
        game_view.draw(screen, current_ticks)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()