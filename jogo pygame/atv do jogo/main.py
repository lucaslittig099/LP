#código principal
import pygame
from pygame.locals import *
from sys import exit #para fechar a janela

#inicializar as funções e variáveis do pygame
pygame.init()
relogio = pygame.time.Clock() #objeto para controlar a taxa de frames

#criar objeto tela
larg=1000
alt=700

x=larg/2-20
y1 = alt/2-35
y2 = alt/2-35

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela

fonte_placar = pygame.font.SysFont('calibri', 50, True, True)
pontos_vermelho = 0
pontos_azul = 0

#todo jogo fica em um loop infinito
while True:
    relogio.tick(200) #5 frames por segundo
    tela.fill((0,150,0))
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()

    #Desenhando as bordas
    pygame.draw.rect(tela,(255,255,255),(20,100,970,20)) #horizontal de cima
    pygame.draw.rect(tela,(255,255,255),(20,100,20,560)) #vertical da esquerda
    pygame.draw.rect(tela,(255,255,255),(970,100,20,560)) #vertical da direita
    pygame.draw.rect(tela,(255,255,255),(20,alt-40,970,20)) #horizontal de baixo

    teclas = pygame.key.get_pressed()

    if teclas[K_w]:
        y1 -= 10
    if teclas[K_s]:
        y1 += 10

    if teclas[K_UP]:
        y2 -= 10
    if teclas[K_DOWN]:
        y2 += 10

    # Mantém os jogadores entre as bordas do campo
    y1 = max(120, min(y1, 660 - 70))
    y2 = max(120, min(y2, 660 - 70))

    pygame.draw.rect(tela, (255, 0, 0), (40, y1, 10, 70))
    pygame.draw.rect(tela, (0, 0, 255), (960, y2, 10, 70))

    # Exibindo o placar
    texto_vermelho = fonte_placar.render(f"Vermelho {pontos_vermelho}", True, (255, 0, 0))
    texto_azul = fonte_placar.render(f"{pontos_azul} Azul", True, (0, 0, 255))
    texto_x = fonte_placar.render("x", True, (255, 255, 255))
    
    pos_x = texto_x.get_rect(center=(larg // 2, 50))

    espaco = 30  # Distância entre o x e cada equipe

    pos_vermelho = texto_vermelho.get_rect(midright=(pos_x.left - espaco, 50))
    pos_azul = texto_azul.get_rect(midleft=(pos_x.right + espaco, 50))

    tela.blit(texto_vermelho, pos_vermelho)
    tela.blit(texto_x, pos_x)
    tela.blit(texto_azul, pos_azul)

    tela.blit(texto_vermelho, pos_vermelho)
    tela.blit(texto_x, pos_x)
    tela.blit(texto_azul, pos_azul)

    pygame.display.update() #atualiza a tela do jogo