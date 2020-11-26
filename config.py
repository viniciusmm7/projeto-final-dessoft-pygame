from os import path

# Pasta com figuras, sons e fonte.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SFX_DIR = path.join(path.dirname(__file__), 'assets', 'sfx')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

# Gerando a página
WIDTH = 1600 # Largura da página que vai abrir
HEIGHT = 900 # Altura da página que vai abrir

# Configurações necessárias do herói
FPS = 60
HERO_WIDTH = int(WIDTH // 10)
HERO_HEIGHT = int(HEIGHT // 5.625)

hero_y = 2*HEIGHT/3 # Variável da posição no eixo y do herói

gravidade = int(HEIGHT // 225) # Gravidade
vi_pulo = 15 * gravidade # Velocidade inicial do pulo
GROUND = (HEIGHT * 5 - HEIGHT / 4.5) // 6

# State
STILL = 0
JUMPING = 1   

# Configurações necessárias do inimigo
ENEMY_WIDTH = int(HERO_WIDTH // 2.5)
ENEMY_HEIGHT = int(HERO_HEIGHT // 2)

enemy_y = 2*HEIGHT/3 # Variável da posição no eixo y do inimigo

# Configurações necessárias do tiro
BULLET_WIDTH = int(HERO_WIDTH // 1.6)
BULLET_HEIGHT = int(HERO_HEIGHT // 2)

# Estados pré jogo
INIT = 0
GAME = 1
QUIT = 2

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
INSPER_RED = (192, 0, 38)
