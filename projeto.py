# Importando bibliotecas a serem utilizadas:
import pygame, random, time
from pygame.locals import *

# ============================== ATENÇÃO, FALTA COLOCAR SOM ==============================
pygame.init()
pygame.mixer.init()

# Gerando a página
WIDTH = 1600 # Largura da página que vai abrir
HEIGHT = 900 # Altura da página que vai abrir
TITULO = 'Insper > fgv'
window = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
pygame.display.set_caption(TITULO)        # Título do jogo


# Configurações necessárias do herói
FPS = 60
HERO_WIDTH = int(WIDTH // 10)
HERO_HEIGHT = int(HEIGHT // 5.625)

hero_y = 2*HEIGHT/3 # Variável da posição no eixo y do herói

gravidade = int(HEIGHT // 225) # Gravidade
vi_pulo = 15 * gravidade # Velocidade inicial do pulo
GROUND = (HEIGHT * 5 - HEIGHT/4.5) // 6

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

# ================================== Funções e classes: ==================================
# Função para iniciar elementos do jogo
def load_assets():
    explosion_anim = [] # Criando lista vazia para adicionar a animação da explosão
    for i in range(9):
        filename = 'assets/img/regularExplosion0{}.png'.format(i)
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (30, 30))
        explosion_anim.append(img)
        
    assets = {} # Dicionário vazio para inserir elementos do jogo
    assets['background'] = pygame.image.load('assets/img/game-background-1.png').convert()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
    assets['enemy_img'] = pygame.image.load('assets/img/mad-enemy-left-1.png').convert_alpha()
    assets['enemy_img'] = pygame.transform.scale(assets['enemy_img'], (ENEMY_WIDTH, ENEMY_HEIGHT))
    assets['hero_img'] = pygame.image.load('assets/img/hero-right-0.png').convert_alpha()
    assets['hero_img'] = pygame.transform.scale(assets['hero_img'], (HERO_WIDTH, HERO_HEIGHT))
    assets['bullet_img'] = pygame.image.load('assets/img/bullet.png').convert_alpha()
    assets['bullet_img'] = pygame.transform.scale(assets['bullet_img'], (BULLET_WIDTH, BULLET_HEIGHT))
    assets["explosion_anim"] = explosion_anim
    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    
    return assets

# ----- Herói (raposa) -----
class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construindo o Sprite do herói
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['hero_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 2 * HERO_WIDTH
        self.rect.y = hero_y
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.state = STILL
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 100 # Tempo para poder atirar novamente em milisegundos

    def update(self):

        self.speedy += gravidade
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.speedy = 0
            self.state = STILL

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            
            self.last_shot = now
        
            new_bullet = Bullet(self.assets, self.rect.right, self.rect.center)
            self.groups['all_sprites'].add(new_bullet)
            self.groups['all_bullets'].add(new_bullet)

    def jump(self):

        if self.state == STILL:
            self.speedy -= vi_pulo
            self.state = JUMPING

# ----- Inimigo (lagartixa) -----
class Enemy(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construindo o Sprite do vilão
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['enemy_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH/2, WIDTH - ENEMY_WIDTH)
        self.rect.y = enemy_y
        self.speedx = random.randint(-20, -5)
        self.speedy = 0

    def update(self):
        # Atualizando a posição do inimigo
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(WIDTH/2, WIDTH - ENEMY_WIDTH)
            self.rect.y = enemy_y
            self.speedx = random.randint(-20, -5)
            self.speedy = 0

# ----- Projétil -----
class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, right, center):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = 15
        

    def update(self):

        self.rect.x += self.speedx

        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

# ----- Explosão (dano)-----
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)

        self.explosion_anim = assets['explosion_anim']

        self.frame = 0
        self.image = self.explosion_anim[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()

        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now

            self.frame += 1

            if self.frame == len(self.explosion_anim):
                self.kill()
                
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# ----- Função principal -----
def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de inimigos
    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_enemies'] = all_enemies
    groups['all_bullets'] = all_bullets

    # Criando o jogador
    player = Hero(groups, assets)
    all_sprites.add(player)

    # Criando os inimigos
    for j in range(2):
        enemy = Enemy(assets)
        all_sprites.add(enemy)
        all_enemies.add(enemy)

    # Status
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    status = PLAYING

    keys_down = {}
    score = 0
    lives = 3
        
    # ===== Loop principal =====
    while status != DONE:
        clock.tick(FPS)
        
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                status = DONE
            # Verifica teclado modo de jogo
            if status == PLAYING:
                # Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:

                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 10

                    if event.key == pygame.K_RIGHT:
                        player.speedx += 10

                    if event.key == pygame.K_SPACE:
                        player.shoot()

                    if event.key == pygame.K_UP:
                        player.jump()

                # Verifica se soltou alguma tecla
                if event.type == pygame.KEYUP:
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 10
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 10

        # ----- Atualiza o estado do jogo
        all_sprites.update()

        if status == PLAYING:
        
            hits = pygame.sprite.groupcollide(all_enemies, all_bullets, True, True)
            for hit in hits:
                # Inimigo morto precisa de recriação
                m = Enemy(assets)
                all_sprites.add(m)
                all_enemies.add(m)
                
                # No lugar do inimigo antigo, adicionar uma explosão
                explosao = Explosion(hit.rect.center, assets)
                all_sprites.add(explosao)

                # Pontos recebidos pela eliminação do inimigo
                score += 100
                if score % 1000 == 0:
                    lives +=1

            hits = pygame.sprite.spritecollide(player, all_enemies, True)
            if len(hits) > 0:
                player.kill()
                lives -= 1
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                status = EXPLODING
                keys_down = {}
                explosion_tick = pygame.time.get_ticks()
                explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim)
                
        elif status == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                if lives == 0:
                    status = DONE
                else:
                    status = PLAYING
                    player = Hero(groups, assets)
                    all_sprites.add(player)
                    enemy = Enemy(assets)
                    all_sprites.add(enemy)
                    all_enemies.add(enemy)

        # ----- Gera saídas
        window.fill((0, 0, 0))
        window.blit(assets['background'], (0, 0))
        # Desenhando os sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets['score_font'].render('{:08d}'.format(score), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH/2, 10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets['score_font'].render(chr(9829) * lives, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT -10)
        window.blit(text_surface, text_rect)
        
        pygame.display.update() # Mostra um novo frame

print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize a tecla "ESPAÇO" ou seta para cima para pular.')

# ===== Finalizando =====
try:
    game_screen(window)
finally:
    pygame.quit()
