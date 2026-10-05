#https://www.youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ
#video 0
#pip install pygame

#video 01
import pygame
from pygame.locals import *
from sys import exit #para fechar a janela

#inicializar as funções e variáveis do pygame
pygame.init()
#criar objeto tela
larg=800
alt=600
tela = pygame.display.set_mode((larg,alt))
pygame.display.set_caption('jogo')#título da janela
#s=pygame.Surface([100,100])
#s.set_at((10,10),(0,0,0))
#s.fill((0,0,0),(10,10))

#todo jogo fica em um loop infinito
while True:
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
    #atualiza a tela do jogo
    pygame.display.update()
    