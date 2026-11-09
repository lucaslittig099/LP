import pygame
import math

# Inicialização padrão do Pygame
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mecânica de Futebol de Botão")
relogio = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
VERDE = (34, 139, 34)
VERMELHO = (220, 20, 60)
PRETO = (0, 0, 0)
LIMITE_ARRASTO = 150

class BotaoJogador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = 20
        self.vel_x = 0
        self.vel_y = 0
        self.arrastando = False  # Estado: diz se o mouse está segurando este botão

    def desenhar(self, tela):
        # Desenha o botão
        pygame.draw.circle(tela, VERMELHO, (int(self.x), int(self.y)), self.raio)
        pygame.draw.circle(tela, PRETO, (int(self.x), int(self.y)), self.raio, 2) # Borda

    def atualizar(self):
        # Move o botão baseado na velocidade atual
        self.x += self.vel_x
        self.y += self.vel_y

        # Atrito: faz o botão ir parando aos poucos (multiplica por um valor menor que 1)
        self.vel_x *= 0.98
        self.vel_y *= 0.98

        # Se a velocidade ficar muito pequena, zera para ele parar totalmente
        if abs(self.vel_x) < 0.1: self.vel_x = 0
        if abs(self.vel_y) < 0.1: self.vel_y = 0

        # Colisão simples com as bordas da tela (para não sair do campo)
        if self.x - self.raio < 0 or self.x + self.raio > LARGURA:
            self.vel_x *= -1 # Inverte a direção x (rebate)
        if self.y - self.raio < 0 or self.y + self.raio > ALTURA:
            self.vel_y *= -1 # Inverte a direção y (rebate)

# Instanciando nosso jogador no centro da tela
meu_botao = BotaoJogador(LARGURA // 2, ALTURA // 2)
rodando = True

while rodando:
    tela.fill(VERDE)

    # Pegar a posição atual do mouse (útil para desenhar a linha de mira)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # 1. QUANDO APERTA O MOUSE
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: # Botão esquerdo do mouse
                # Verifica se clicou dentro do círculo (usando teorema de pitágoras para a distância)
                distancia = math.hypot(meu_botao.x - mouse_x, meu_botao.y - mouse_y)
                if distancia <= meu_botao.raio:
                    # Se a distância for menor que o raio, o clique foi no botão!
                    meu_botao.arrastando = True
                    # Zera a velocidade para poder mirar com ele parado
                    meu_botao.vel_x = 0
                    meu_botao.vel_y = 0

        # 2. QUANDO SOLTA O MOUSE
        elif evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1 and meu_botao.arrastando:
                meu_botao.arrastando = False
                
                # Calcula a diferença entre a posição do botão e onde o mouse foi solto.
                # Como você arrasta para trás para atirar para frente, subtraímos a pos do mouse da pos do botão.
                dx = meu_botao.x - mouse_x
                dy = meu_botao.y - mouse_y
                
                distancia_arrasto = math.hypot(dx, dy)
                
                if distancia_arrasto > LIMITE_ARRASTO:
                    fator_reducao = LIMITE_ARRASTO / distancia_arrasto
                    dx *= fator_reducao
                    dy *= fator_reducao
                
                # Multiplicamos por um fator de força (0.1) para não ficar rápido demais
                forca_multiplicador = 0.1
                meu_botao.vel_x = dx * forca_multiplicador
                meu_botao.vel_y = dy * forca_multiplicador

    # Se estiver arrastando, desenha uma linha mostrando o impulso
    if meu_botao.arrastando:
        
        dx_linha = mouse_x - meu_botao.x
        dy_linha = mouse_y - meu_botao.y
        distancia_linha = math.hypot(dx_linha, dy_linha)
        
        if distancia_linha > LIMITE_ARRASTO:
            fator_reducao = LIMITE_ARRASTO / distancia_linha
            dx_linha *= fator_reducao
            dy_linha *= fator_reducao
        
        ponto_final_x = meu_botao.x + dx_linha
        ponto_final_y = meu_botao.y + dy_linha
        
        pygame.draw.line(tela, BRANCO, (meu_botao.x, meu_botao.y), (ponto_final_x, ponto_final_y), 2)

    # Atualiza posição e desenha
    meu_botao.atualizar()
    meu_botao.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()