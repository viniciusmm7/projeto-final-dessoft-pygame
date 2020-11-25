import pygame
import random
import time

pygame.init()
pygame.mixer.init()

# Gerando a página
WIDTH = 800
HEIGHT = 450
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Raposona Braba')

# Configurações necessárias do herói
HERO_WIDTH = 100 # Mudar
HERO_HEIGHT = 100 # Mudar

hero_y = 2*HEIGHT/3-20

# Configurações necessárias do inimigo
ENEMY_WIDTH = 30
ENEMY_HEIGHT = 40

enemy_y = 2*HEIGHT/3

# Configurações necessárias do tiro

BULLET_WIDTH = 10
BULLET_HEIGHT = 10

# Inicia assets
assets = {}
assets['background'] = pygame.image.load('assets/img/game-background-1.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
assets['enemy_img'] = pygame.image.load('assets/img/mad-enemy-left-1.png').convert_alpha()
assets['enemy_img'] = pygame.transform.scale(assets['enemy_img'], (ENEMY_WIDTH, ENEMY_HEIGHT))
assets['hero_img'] = pygame.image.load('assets/img/hero-right-0.png').convert_alpha()
assets['hero_img'] = pygame.transform.scale(assets['hero_img'], (HERO_WIDTH, HERO_HEIGHT))
assets['bullet_img'] = pygame.image.load('assets/img/bullet.png').convert_alpha()
explosion_anim = []
for i in range(9):
    filename = 'assets/img/regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (30, 30))
    explosion_anim.append(img)
assets['explosion_anim'] = explosion_anim

class Hero(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construindo o Sprite do herói
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['hero_img']
        self.rect = self.image.get_rect()
        self.rect.x = 2 * HERO_WIDTH
        self.rect.y = hero_y-20
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):

        self.rect.x += self.speedx

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        new_bullet = Bullet(self.assets, self.rect.right, self.rect.centerx)
        self.groups['all_sprites'].add(new_bullet)
        self.groups['all_bullets'].add(new_bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construindo o Sprite do vilão
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['enemy_img']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH/2, WIDTH - ENEMY_WIDTH)
        self.rect.y = enemy_y
        self.speedx = -2
        self.speedy = 0

    def update(self):
        # Atualizando a posição do inimigo
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(WIDTH/2, WIDTH - ENEMY_WIDTH)
            self.rect.y = enemy_y
            self.speedx = -2
            self.speedy = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets, right, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['bullet_img']
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.right = right
        self.rect.x = 0
        self.rect.y = hero_y + 25
        self.speedx = 8
        self.speedy = 0

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()

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
                self.rect.center - center

game = 1

clock = pygame.time.Clock()
FPS = 60

# Criando inimigos
all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_enemies'] = all_enemies
groups['all_bullets'] = all_bullets

player = Hero(groups, assets)
all_sprites.add(player)

for i in range(2):
    enemy = Enemy(assets)
    all_sprites.add(enemy)
    all_enemies.add(enemy)
    
# ----- Loop principal -----
while game != 0:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedx -= 3
            if event.key == pygame.K_RIGHT:
                player.speedx += 3
            if event.key == pygame.K_SPACE:
                player.shoot()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedx += 3
            if event.key == pygame.K_RIGHT:
                player.speedx -= 3
            
    all_sprites.update()

    hits = pygame.sprite.groupcollide(all_enemies, all_bullets, True, True)
    for hit in hits: 
        m = Enemy(assets)
        all_sprites.add(m)
        all_enemies.add(m)

        explosao = Explosion(enemy.rect.center, assets)
        all_sprites.add(explosao)

    hits = pygame.sprite.spritecollide(player, all_enemies, True)
    if len(hits) > 0:
        game = 0

    window.fill((192, 0, 38))
    window.blit(assets['background'], (0, 0))

    all_sprites.draw(window)
    
    pygame.display.update()


pygame.quit()
