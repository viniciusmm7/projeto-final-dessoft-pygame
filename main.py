# ===== Inicializando =====
# ----- Importa e inicia pacotes
import pygame, random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from game_screen import game_screen
from init_screen import init_screen

pygame.init()
pygame.mixer.init()

# ----- Gerando tela principal
TITULO = 'RAPOSA LOKA'
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITULO)

pre_state = INIT
while pre_state != QUIT:
    if pre_state == INIT:
        pre_state = init_screen(window)
    elif pre_state == GAME:
        pre_state = game_screen(window)
    else:
        pre_state = QUIT

# ===== Finalizando =====
pygame.quit()
