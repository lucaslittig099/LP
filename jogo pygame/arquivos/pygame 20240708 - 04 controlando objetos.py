#https://www.youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ
#video 0
#pip install pygame

#video 01
import pygame
from pygame.locals import *
from sys import exit #para fechar a janela

#inicializar as funções e variáveis do pygame
pygame.init()
relogio = pygame.time.Clock() #objeto para controlar a taxa de frames

#criar objeto tela
larg=640
alt=480
x=larg/2-20 #meio da largura
y=alt/2-20 #meio da altura

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela


#todo jogo fica em um loop infinito
while True:
    relogio.tick(20) #frames por segundo - quanto maior, mais rápido
    tela.fill((0,0,0))
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
        # primeiro jeito - não gera movimento contínuo quando a tecla é pressionada
        #deste jeito ele captura o evento pressionamento de tecla
        """if event.type == KEYDOWN: #evento é tecla pressionada 
            if event.key ==K_a: #tecla a para esquerda
                x-=10
            if event.key==K_d: #tecla d para direita
                x+=10
            if event.key==K_w: #tecla w para cima
                y-=10
            if event.key==K_s: #tecla s para baixo
                y+=10"""
    #segundo jeito - fora do for
    #deste jeito ele verifica se a tecla está pressionada - não é o pressionamento
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x-=10
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x+=10
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y-=10
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y+=10
    pygame.draw.rect(tela,(255,0,0),(x,y,40,50)) #(tela, (r,g,b), (coordenadas, tamanho))

    pygame.display.update() #atualiza a tela do jogo
    