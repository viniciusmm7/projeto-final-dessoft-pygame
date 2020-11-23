import pygame
from os import path

pygame.init()

# Menu do jogo
#limites da tela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Raposa Loka')
world_speed= -10
pygame.SYSTEM_CURSOR_IBEAM
#cores usadas
vermelho = (255,0,0)
branco=(255,255,255)
vermelho2=(192, 0, 38)
verde = (0, 255, 0)

#objeto para atualizações das imagens
clock = pygame.time.Clock()

def jogo():
    clock.tick(60)
    game = 1

    #imagens
    #Fundo do menu
    image_menu = pygame.image.load ('Projeto/Imagens/fundo-menu.png').convert()
    image_menu = pygame.transform.scale( image_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))

    #Fundo jogo
    image_game = pygame.image.load('Projeto/Imagens/fundo-jogo.png').convert()
    image_game = pygame.transform.scale(image_game, (WINDOW_WIDTH, WINDOW_HEIGHT))

    
    FPS = 15

    # Loop principal
    while game != 0:
        # Eventos
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = 0
        
        window.fill((192, 0, 38))

    
        # vertices = [(100, 100), (1500, 100), (1500, 800), (100, 800)]
        game = menu_tela(image_menu)

#textos
def textos (text, cor, tamanho, x, y):
    font = pygame.font.SysFont(None, tamanho)
    title = font.render(text, True, cor)
    window.blit(title, (x, y))
    return title

#botões
def botoes(txt,posx,posy,larg,alt,cret,clet,action = None):
     
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if posx + larg > mouse [0] > posx and posy + alt > mouse[1] > posy:
        pygame.draw.rect(window, clet,(posx, posy, larg,alt))
        if click[0] == 1 and action != None:
            if action == "jogar":
                game_loop()
            elif action == "sair":
                pygame.quit()

    else:
        pygame.draw.rect (window, cret, (posx, posy, larg, alt))

    #posicionando o texto
    Texto = pygame.font.SysFont(None, 50)
    textSurf, textRect = text_objects(txt, Texto)
    textRect.center = ((posx + (larg/2)),(posy +(alt/2)))
    window.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, branco)
    return textSurface, textSurface.get_rect()

# tela do menu
def menu_tela (fundo):
    #titulo_1 = font.render('Iniciar', True, branco)
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio=False
                return 0
        
        window.blit(fundo,(0,0))
        #carrega textos
        #window.blit(fundo, (0, 0))
        textos('Raposa', vermelho2,100, (WINDOW_WIDTH/2)-100, 50)
        textos('Loka', vermelho2,100, (WINDOW_WIDTH/2)-50, 110)
        textos('Raposa', vermelho,100, (WINDOW_WIDTH/2)-105, 50)
        textos('Loka', vermelho,100, (WINDOW_WIDTH/2)-55, 110)

        #botões        
        botoes("Jogar!", (WINDOW_WIDTH/2)-75, 300, 200,75,vermelho, vermelho2,"jogar")
        botoes("Sair!", (WINDOW_WIDTH/2)-75, 400, 200,75,vermelho, vermelho2,"sair")        
        pygame.display.update() 


jogo()
# Finalizando pygame
pygame.quit()