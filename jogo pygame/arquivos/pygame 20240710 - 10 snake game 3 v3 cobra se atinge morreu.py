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

pygame.mixer.music.set_volume(0.1) # valor entre 0 e 1
som_fundo= pygame.mixer.music.load('som_fundo_CPU_Talk.mp3') #carrega o som de fundo pode ser mp3 ou wav
#som_fundo.set_volume(0.1)
pygame.mixer.music.play(-1) #-1 = repetir

som_colisao= pygame.mixer.Sound('som_colisao_smw_coin.wav') #carrega o som da colisão - deve ser wav - não pode ser mp3
som_colisao.set_volume(1) # valor entre 0 e 1

relogio = pygame.time.Clock() #objeto para controlar a taxa de frames

#criar objeto tela
larg=640
alt=480

x_cobra=int(larg/2)-20 #meio da largura
y_cobra=int(alt/2)-20 #meio da altura
x_maca = randint(40,600)
y_maca = randint(50,430)
pontos=0
veloc= 10 #clock ticks para aumentar com o tempo
lista_cobra = []
lastkey=""
deltax=0
deltay=0
compr =5 #comprimento inicial da cobra
morreu =False

fonte=pygame.font.SysFont('calibri',20,True,True) #fonte, tamanho, negrito, itálico
#pygame.font.get_fonts() - para saber das fontes existentes

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela

def aumenta_cobra(lista_cobra): #desenha a cobra  
    for xey in lista_cobra: #xey é a lista [x,y]
        pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],20,20))

def reiniciar_jogo():
    global pontos,lista_cobra,compr,veloc,x_cobra,y_cobra,x_maca,y_maca,lastkey,deltax,deltay,morreu
    pontos=0
    lista_cobra = []
    compr =5
    veloc= 10
    x_cobra=int(larg/2)-20 #meio da largura
    y_cobra=int(alt/2)-20 #meio da altura
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    lastkey=""
    deltax=0
    deltay=0
    morreu =False

#todo jogo fica em um loop infinito
while True:
    relogio.tick(int(veloc)) #frames por segundo - quanto maior, mais rápido
    tela.fill((255,255,255)) #preenche tela com preto
    mensagem = f'Pontos: {pontos}' 
    textoformatado= fonte.render(mensagem, True, (0,0,255)) #texto, antialized texto menos serrilhado, cor

    #guarda as posiçoes antigas da cabeça antes de modificar
    x_old=x_cobra 
    y_old=y_cobra

    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()
        
        # primeiro jeito - não gera movimento contínuo quando a tecla é pressionada
        #deste jeito ele captura o evento pressionamento de tecla
        if event.type == KEYDOWN: #evento é tecla pressionada 
            if event.key ==K_a or event.key==K_LEFT: #tecla a para esquerda
                if not(deltax==20): #evita movimento contrário
                    deltax=-20
                    deltay=0
            if event.key==K_d or event.key==K_RIGHT: #tecla d para direita
                if not(deltax==-20): #evita movimento contrário
                    deltax=20
                    deltay=0
            if event.key==K_w or event.key==K_UP: #tecla w para cima
                if not(deltay==20): #evita movimento contrário
                    deltax=0
                    deltay=-20
            if event.key==K_s or event.key==K_DOWN: #tecla s para baixo
                if not(deltay==-20): #evita movimento contrário
                    deltax=0
                    deltay=20
                
    x_cobra+=deltax
    y_cobra+=deltay
    if y_cobra<0:
        y_cobra=470
        
    '''#segundo jeito - fora do for
    #deste jeito ele verifica se a tecla está pressionada - não é o pressionamento
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT] or lastkey=="L":
        x_cobra-=20
        lastkey="L"
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT] or lastkey=="R":
        x_cobra+=20
        lastkey="R"
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP] or lastkey=="U":
        y_cobra-=20
        lastkey="U"
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN] or lastkey=="D":
        y_cobra+=20
        lastkey="D"
    '''
    
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20)) #(tela, (r,g,b), (coordenadas, tamanho)) - verde
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20)) #(tela, (r,g,b), (coordenadas, tamanho)) - vermelho
    
    #rect1.colliderect(rect2) - verifica colisão entre dois retângulos
    #ou pygame.Rect.colliderect(rect1,rect2)
    if cobra.colliderect(maca):
    #if pygame.Rect.colliderect(cobra,maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos+=1
        compr+=1
        som_colisao.play()
        veloc+=0.3 #aumenta clock ticks

    lista_cabeca=[x_cobra,y_cobra]
    if not(x_old==x_cobra and y_old==y_cobra):#sem isto aqui, se a cobra parar as posiçoes mais antigas
        #assumem a posição da cabeça e como a lista possui tamanho fixo a cobra encolhe pois a maioria de
        #suas posiçoes será com a posição da cabeça
        lista_cobra.append(lista_cabeca)
        
    #quando fica parado a mesma posição é gravada várias vezes. Por isso a cobra diminui
    if len(lista_cobra)>compr:
        del lista_cobra[0]
    
    if lista_cobra.count(lista_cabeca)>1: #tem mais de um ponto com a coordenada da cabeça no corpoda cobra
        morreu=True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT: #clicar no x no canto superior da tela
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN: #evento é tecla pressionada 
                    if event.key ==K_r: #tecla r pressionada
                        reiniciar_jogo()

                    
        
    aumenta_cobra(lista_cobra)
        
    tela.blit(textoformatado, (500,40)) #texto, pos
    pygame.display.update() #atualiza a tela do jogo
    