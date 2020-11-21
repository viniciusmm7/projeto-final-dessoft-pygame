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
    image_menu = pygame.image.load('Imagens/fundo-menu.png').convert()
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
    title = font.render('{text}', True, cor)
    window.blit(title, (x, y))
    return title

#botões
def botoes():

    for event in pygame.events:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
# tela do menu
def menu_tela (fundo):
    #retangulos
    rect_width = 200
    rect_height = 75
    #textos
    
    titulo_1 = font.render('Raposa', True, vermelho2)
    titulo_2 = font.render('Loka', True, vermelho2)
    #titulo_3 = font.render('Iniciar', True, branco)
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        #carrega
        #window.blit(fundo, (0, 0))
        
        window.blit(titulo_2, (355, 130))
        window.blit(titulo_3, (((WINDOW_WIDTH-rect_width)/2),((WINDOW_HEIGHT-rect_height+50)/2))

        # Atualiza o estado do jogo
        pygame.display.set_mode
        fundo = pygame.transform.scale(fundo, (WINDOW_WIDTH, WINDOW_HEIGHT))
        ##fundo_interacao = background.get_rect()
        ##pygame.draw.rect (window, vermelho, fundo_interacao)
        
        rect_start = pygame.draw.rect (window, vermelho, (((WINDOW_WIDTH-rect_width)/2),((WINDOW_HEIGHT-rect_height+50)/2),rect_width,rect_height))
        rect_quit = pygame.draw.rect (window, vermelho, (((WINDOW_WIDTH-rect_width)/2),((WINDOW_HEIGHT+150)/2),rect_width,rect_height))        
        pygame.display.update()


        

jogo()
# Finalizando pygame
pygame.quit()