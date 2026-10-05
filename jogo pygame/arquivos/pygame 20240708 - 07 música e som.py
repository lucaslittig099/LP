#https://www.youtube.com/playlist?list=PLJ8PYFcmwFOxtJS4EZTGEPxMEo4YdbxdQ
#video 0
#pip install pygame

#video 01
import pygame
from random import randint
from pygame.locals import *
from sys import exit #para fechar a janela

#inicializar as funções e variáveis do pygame
pygame.init()

pygame.mixer.music.set_volume(0.3) # valor entre 0 e 1
som_fundo= pygame.mixer.music.load('som_fundo_CPU_Talk.mp3') #carrega o som de fundo pode ser mp3 ou wav
#som_fundo.set_volume(0.1)
pygame.mixer.music.play(-1) #-1 = repetir

som_colisao= pygame.mixer.Sound('som_colisao_smw_coin.wav') #carrega o som da colisão - deve ser wav - não pode ser mp3
som_colisao.set_volume(1) # valor entre 0 e 1

relogio = pygame.time.Clock() #objeto para controlar a taxa de frames

#criar objeto tela
larg=640
alt=480
x=int(larg/2)-20 #meio da largura
y=int(alt/2)-20 #meio da altura

x_az = randint(40,600)
y_az = randint(50,430)

pontos=0
fonte=pygame.font.SysFont('calibri',20,True,True) #fonte, tamanho, negrito, itálico
#pygame.font.get_fonts() - para saber das fontes existentes

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela


#todo jogo fica em um loop infinito
while True:
    relogio.tick(50) #frames por segundo - quanto maior, mais rápido
    tela.fill((0,0,0)) #preenche tela com preto
    mensagem = f'Pontos: {pontos}'
    textoformatado= fonte.render(mensagem, True, (255,255,255)) #texto, antialized texto menos serrilhado, cor
    
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
        ''' # primeiro jeito - não gera movimento contínuo quando a tecla é pressionada
        #deste jeito ele captura o evento pressionamento de tecla
        if event.type == KEYDOWN: #evento é tecla pressionada 
            if event.key ==K_a: #tecla a para esquerda
                x-=5
            if event.key==K_d: #tecla d para direita
                x+=5
            if event.key==K_w: #tecla w para cima
                y-=5
            if event.key==K_s: #tecla s para baixo
                y+=5 '''
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
    ret_vm = pygame.draw.rect(tela,(255,0,0),(x,y,40,50)) #(tela, (r,g,b), (coordenadas, tamanho)) - vermelho
    ret_az = pygame.draw.rect(tela,(0,0,255),(x_az,y_az,40,50)) #(tela, (r,g,b), (coordenadas, tamanho)) - azul
    
    #rect1.colliderect(rect2) - verifica colisão entre dois retângulos
    #ou pygame.Rect.colliderect(rect1,rect2)
    if ret_vm.colliderect(ret_az):
    #if pygame.Rect.colliderect(ret_vm,ret_az):
        x_az = randint(40,600)
        y_az = randint(50,430)
        pontos+=1
        som_colisao.play()
        
    tela.blit(textoformatado, (500,40)) #texto, pos
    pygame.display.update() #atualiza a tela do jogo
    