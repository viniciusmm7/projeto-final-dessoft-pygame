import pygame, time
from config import FPS, WIDTH, HEIGHT, INSPER_RED
from assets import load_assets, ENEMY_DEATH_SOUND, BOOM_SOUND, HERO_DAMAGE_SOUND, GAME_OVER_SOUND, BACKGROUND, SCORE_FONT
from sprites import Hero, Enemy, Bullet, Explosion

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

    # Status
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    status = PLAYING

    keys_down = {}
    score = 0
    lives = 5

    # Criando os inimigos
    for j in range(4):
        enemy = Enemy(assets)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
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
                assets[BOOM_SOUND].play()
                assets[ENEMY_DEATH_SOUND].play()
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
                # Som da colisão
                assets[HERO_DAMAGE_SOUND].play()
                assets[ENEMY_DEATH_SOUND].play()
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
                    assets[GAME_OVER_SOUND].play()
                    time.sleep(5)
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
