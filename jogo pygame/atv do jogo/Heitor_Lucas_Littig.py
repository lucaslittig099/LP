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

#Variáveis da bola
bola_x = larg / 2
bola_y = alt / 2
bola_raio = 10
vel_bola_x = 1 #velocidade horizontal
vel_bola_y = 1 #velocidade vertical

evento_acelerar = pygame.USEREVENT + 1
pygame.time.set_timer(evento_acelerar, 10000)

tela = pygame.display.set_mode((larg,alt)) #cria tela com largura e altura
pygame.display.set_caption('jogo')#título da janela

fonte_placar = pygame.font.SysFont('calibri', 50, True, True)
pontos_vermelho = 0
pontos_azul = 0

#todo jogo fica em um loop infinito
while True:
    relogio.tick(100) #5 frames por segundo
    tela.fill((0,150,0))
    #loop para checar se um evento ocorreu
    #pygame.event.get() - lista de eventos capturados pelo pygame
    for event in pygame.event.get():
        if event.type == QUIT: #clicar no x no canto superior da tela
            pygame.quit()
            exit()

        #Aumenta a velocidade com o passar do tempo
        if event.type == evento_acelerar:
            if vel_bola_x > 0:
                vel_bola_x += 1
            else:
                vel_bola_x += -1

            if vel_bola_y > 0:
                vel_bola_y += 1
            else:
                vel_bola_y += -1

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

    #Atualizaa posição da bola
    bola_x += vel_bola_x
    bola_y += vel_bola_y

    #Colisão com as bordas(teto e chão)
    if bola_y - bola_raio <= 120 or bola_y + bola_raio >= 660:
        vel_bola_y *= -1

    #Criando os retângulos para checar colisão
    rect_bola = pygame.Rect(bola_x - bola_raio, bola_y - bola_raio, bola_raio * 2, bola_raio * 2)
    rect_vermelho = pygame.Rect(40, y1, 10, 70)
    rect_azul = pygame.Rect(960, y2, 10, 70)

    #Checando colisão da bola com as raquetes
    if rect_bola.colliderect(rect_vermelho) or rect_bola.colliderect(rect_azul):
        vel_bola_x *= -1

    #Verificando pontuação(passou das raquetes)
    if bola_x < 40: # azul marca ponto
        pontos_azul += 1
        bola_x, bola_y = larg / 2, alt / 2 #volta pro centro
        vel_bola_x = 1 #reseta a velocidade e saca pra direita

        if vel_bola_y > 0: #reseta o y mantendo direção
            vel_bola_y = 1
        else:
            vel_bola_y = -1

    elif bola_x > 960: #vermelho marca ponto
        pontos_vermelho += 1
        bola_x, bola_y = larg / 2, alt / 2
        vel_bola_x = -1 #reseta a velocidade e saca pra esquerda

        if vel_bola_y > 0: #mesma coisa de antes
            vel_bola_y = 1
        else:
            vel_bola_y = -1
        

    pygame.draw.rect(tela, (255, 0, 0), (40, y1, 10, 70))
    pygame.draw.rect(tela, (0, 0, 255), (960, y2, 10, 70))
    pygame.draw.circle(tela, (255, 255, 0), (int(bola_x), int(bola_y)), bola_raio)

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