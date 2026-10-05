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
x=larg/2-20
y=0

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela


#todo jogo fica em um loop infinito
while True:
    relogio.tick(200) #5 frames por segundo
    tela.fill((0,0,0))
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
       
    pygame.draw.rect(tela,(255,0,0),(x,y,40,50)) #(tela, (r,g,b), (coordenadas, tamanho))
    if y==490:
        y=-67
    y+=1

    pygame.display.update() #atualiza a tela do jogo
    