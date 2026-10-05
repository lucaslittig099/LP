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
larg=640
alt=480
tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela

#todo jogo fica em um loop infinito
while True:
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
    pygame.draw.rect(tela,(255,0,0),(200,300,40,50)) #(tela, (r,g,b), (coordenadas, tamanho))
    pygame.draw.circle(tela,(0,0,255),(300,300),40) #(tela, (r,g,b), (coordenadas), raio))
    pygame.draw.line(tela,(255,255,0),(300,300),(500,200),5) #(tela, (r,g,b), (coordenadas),(coordenadas),espessura))
    pygame.draw.line(tela,(255,255,0),(390,0),(390,479),5) #(tela, (r,g,b), (coordenadas),(coordenadas),espessura))

    
#atualiza a tela do jogo
    pygame.display.update()
    