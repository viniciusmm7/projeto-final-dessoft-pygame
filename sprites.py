import pygame, random
from config import WIDTH, HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT, enemy_y, HERO_WIDTH, HERO_HEIGHT, hero_y, STILL, JUMPING, vi_pulo, gravidade, GROUND
from assets import HERO_IMG, MAGIC_THROW_SOUND, HERO_JUMP_SOUND, HERO_DAMAGE_SOUND, ENEMY_IMG, BULLET_IMG, EXPLOSION_ANIM

class Hero(pygame.sprite.Sprite):
 
    def __init__(self, groups, assets):
        # Construindo o Sprite do herói
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['hero_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = HERO_WIDTH
        self.rect.y = hero_y
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.state = STILL
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 150 # Tempo para poder atirar novamente em milisegundos

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
            self.assets[MAGIC_THROW_SOUND].play()

    def jump(self):

        if self.state == STILL:
            self.speedy -= vi_pulo
            self.state = JUMPING
            self.assets[HERO_JUMP_SOUND].play()

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

        self.image = assets[BULLET_IMG]
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
