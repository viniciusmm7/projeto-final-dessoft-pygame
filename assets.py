import pygame, os
from config import WIDTH, HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, HERO_WIDTH, HERO_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT, IMG_DIR, SFX_DIR, FNT_DIR

MENU_BACKGROUND = 'menu_background'
BACKGROUND = 'background'
ENEMY_IMG = 'enemy_img'
ENEMY_IMG = 'enemy_img'
HERO_IMG = 'hero_img'
HERO_IMG = 'hero_img'
BULLET_IMG = 'bullet_img'

EXPLOSION_ANIM = 'explosion_anim'
SCORE_FONT = 'score_font'

# ----- Falta colocar os sons -----
BOOM_SOUND = 'boom_sound'
ENEMY_DEATH_SOUND = 'enemy_death_sound'
MAGIC_THROW_SOUND = 'magic_throw_sound'
HERO_JUMP_SOUND = 'hero_jump_sound'
HERO_DAMAGE_SOUND = 'hero_damage_sound'
GAME_OVER_SOUND = 'game_over_sound'

def load_assets():
    explosion_anim = [] # Criando lista vazia para adicionar a animação da explosão
    for i in range(9):
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (30, 30))
        explosion_anim.append(img)        
        
    assets = {} # Dicionário vazio para inserir elementos do jogo
    # Imagens do jogo
    assets[MENU_BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'menu-background.jpeg')).convert()
    assets[MENU_BACKGROUND] = pygame.transform.scale(assets[MENU_BACKGROUND], (WIDTH, HEIGHT))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'game-background-1.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[ENEMY_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'mad-enemy-left-1.png')).convert_alpha()
    assets[ENEMY_IMG] = pygame.transform.scale(assets[ENEMY_IMG], (ENEMY_WIDTH, ENEMY_HEIGHT))
    assets[HERO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'hero-right-0.png')).convert_alpha()
    assets[HERO_IMG] = pygame.transform.scale(assets[HERO_IMG], (HERO_WIDTH, HERO_HEIGHT))
    assets[BULLET_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'bullet.png')).convert_alpha()
    assets[BULLET_IMG] = pygame.transform.scale(assets[BULLET_IMG], (BULLET_WIDTH, BULLET_HEIGHT))
    
    # Animação
    assets[EXPLOSION_ANIM] = explosion_anim

    # Fonte do placar
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Sons do jogo
    pygame.mixer.music.load(os.path.join(SFX_DIR, 'wind_sound.wav'))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load(os.path.join(SFX_DIR, 'game_background_song.wav'))
    pygame.mixer.music.set_volume(0.5)
    assets[BOOM_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'boom_sound.wav'))
    assets[ENEMY_DEATH_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'enemy_death_sound.wav'))
    assets[MAGIC_THROW_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'magic_throw_sound.wav'))
    assets[HERO_JUMP_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'hero_jump_sound.ogg'))
    assets[HERO_DAMAGE_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'hero_damage_sound.wav'))
    assets[GAME_OVER_SOUND] = pygame.mixer.Sound(os.path.join(SFX_DIR, 'game_over_sound.wav'))
    
    return assets
