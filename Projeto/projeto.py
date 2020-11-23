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
#objeto para atualizações das imagens
clock = pygame.time.Clock()

def jogo():
    clock.tick(60)
    game = 1

    #imagens
    #Fundo do menu
    image_menu = pygame.image.load ('Imagens/fundo-menu.png').convert()
    image_menu = pygame.transform.scale(image_menu, (WINDOW_WIDTH, WINDOW_HEIGHT))

    #Fundo jogo
    image_game = pygame.image.load('Imagens/fundo-jogo.png').convert()
    image_game = pygame.transform.scale(image_game, (WINDOW_WIDTH, WINDOW_HEIGHT))

    
    FPS = 15

    # Loop principal
    while game != 0:
        # Eventos
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game = 0
        
        window.fill((192, 0, 38))

        cor = (0, 255, 0)
        # vertices = [(100, 100), (1500, 100), (1500, 800), (100, 800)]
        menu_tela(image_menu)
def textos (text, cor, tamanho, x, y):
    font = pygame.font.SysFont(None, tamanho)
    title = font.render(text, True, cor)
    window.blit(title, (x, y))
    return title

#botões
def botoes(txt,posx,posy,larg,alt,ci,cf,action = None):
     
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + larg > mouse [0] > x and y + alt > mouse[1] > y:
        pygame.draw.rect(tela, cf,(x, y, larg,a))
        if click[0] == 1 and action != None:
            if action == "ENTRAR":
                game_loop()
            elif action == "quit":
                pygame.quit()

    else:
        pygame.draw.rect (tela, ci, (x, y, larg,alt))

# tela do menu
def menu_tela (fundo):
    #titulo_3 = font.render('Iniciar', True, branco)
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        #carrega
        #window.blit(fundo, (0, 0))
        textos('Raposa', vermelho2,50, 355, 200)
        textos('Loka', vermelho2,50, 355, 130)

        # Atualiza o estado do jogo
        window (fundo)
        ##fundo_interacao = background.get_rect()
        ##pygame.draw.rect (window, vermelho, fundo_interacao)
        
        botoes("Jogar!",150, 300, 100,50,vermelho, branco,"ENTRAR")
        botoes("Sair!",550, 300, 100,50,vermelho, branco,"quit")        
        pygame.display.update()


        

jogo()
# Finalizando pygame
pygame.quit()