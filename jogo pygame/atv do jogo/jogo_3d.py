import pygame 
import math

pygame.init()

largura_tela = 1280
altura_tela = 720
meia_largura = largura_tela // 2
meia_altura = altura_tela // 2

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo 3D")
relogio = pygame.time.Clock()

mapa = [
    "#############",
    "#.....#.....#",
    "#.....#.....#",
    "#..#....##..#",
    "#...........#",
    "#....##..#..#",
    "####..#..#..#",
    "#........#..#",
    "#.....#.....#",
    "#############",
]

escala = 12
x, y, angulo = 1.5, 4.5, 0.0
campo_visao = math.pi / 3 
colunas = 320
largura = largura_tela // colunas
inimigos = [[9.5, 4.5], [11.5, 1.5], [8.5, 7.5]]
tiro = 0

def parede(px, py):
    return mapa[int(py)][int(px)] == "#"

def raio(a):
    c, s = math.cos(a), math.sin(a)
    d = 0
    while not parede(x + c * d, y + s * d):
        d += 0.02
    return d

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                tiro = 6
            if evento.key == pygame.K_ESCAPE:
                rodando = False

    teclas = pygame.key.get_pressed()
    giro = teclas[pygame.K_d] - teclas[pygame.K_a]
    angulo += giro * 0.05
    frente = teclas[pygame.K_w] - teclas[pygame.K_s]
    passo = frente * 0.08
    dx = math.cos(angulo) * passo
    dy = math.sin(angulo) * passo
    if not parede(x + dx * 4, y):
        x += dx
    if not parede(x, y + dy * 4):
        y += dy
    
    # Céu e Chão
    tela.fill("gray10")
    pygame.draw.rect(tela, "sienna4", (0, meia_altura, largura_tela, meia_altura))
    
    # Raycasting (Paredes)
    distancias = []
    for i in range(colunas):
        a = angulo - campo_visao / 2 + campo_visao * i / colunas
        d = raio(a)
        px = x + math.cos(a) * d
        py = y + math.sin(a) * d
        d *= math.cos(a - angulo)
        distancias.append(d)
        luz = max(30, 230 - d * 22)
        if abs(px - round(px)) < 0.03:
            luz *= 0.7
        altura = min(altura_tela, altura_tela / d)
        cor = (luz, luz * 0.9, luz * 0.75)
        faixa = (i * largura, meia_altura - altura / 2, largura + 1, altura)
        pygame.draw.rect(tela, cor, faixa)
        pygame.draw.line(tela, "yellow", (x * escala, y * escala), (px * escala, py * escala))

    # Inimigos
    inimigos.sort(key=lambda e: -math.dist(e, (x, y)))
    for inimigo in inimigos[:]:
        dx, dy = inimigo[0] - x, inimigo[1] - y
        distancia = math.hypot(dx, dy)
        if distancia > 0.8:
            inimigo[0] -= dx / distancia * 0.03
            inimigo[1] -= dy / distancia * 0.03
        rel = math.atan2(dy, dx) - angulo
        rel = (rel + math.pi) % (2 * math.pi) - math.pi
        sx = meia_largura + rel / (campo_visao / 2) * meia_largura
        col = int(sx / largura)
        if not 0 <= col < colunas or distancias[col] < distancia:
            continue
        altura = altura_tela / distancia
        corpo = pygame.Rect(0, 0, altura * 0.5, altura * 0.7)
        corpo.midbottom = (sx, meia_altura + altura / 2)
        pygame.draw.ellipse(tela, "darkred", corpo)
        for ox in (sx - altura * 0.1, sx + altura * 0.1):
            olho = (ox, corpo.y + altura * 0.2)
            pygame.draw.circle(tela, "gold", olho, altura / 20)
        if tiro == 6 and abs(sx - meia_largura) < altura * 0.25:
            inimigos.remove(inimigo)
            tiro = 5

    # Minimapa
    for my, linha in enumerate(mapa):
        for mx, c in enumerate(linha):
            if c == "#":
                bloco = (mx * escala, my * escala, escala, escala)
                pygame.draw.rect(tela, "gray40", bloco)
    for ex, ey in inimigos:
        pos = (ex * escala, ey * escala)
        pygame.draw.circle(tela, "red", pos, 4)
    pygame.draw.circle(tela, "white", (x * escala, y * escala), 5)

    # Tiro e Arma
    if tiro > 0:
        pygame.draw.circle(tela, "orange", (meia_largura, altura_tela - 230), 60)
        pygame.draw.circle(tela, "yellow", (meia_largura, altura_tela - 230), 30)
        tiro -= 1

    arma = [
        (meia_largura - 80, altura_tela),
        (meia_largura - 40, altura_tela - 140),
        (meia_largura + 40, altura_tela - 140),
        (meia_largura + 80, altura_tela)
    ]
    pygame.draw.polygon(tela, "gray35", arma)
    pygame.draw.rect(tela, "gray20", (meia_largura - 20, altura_tela - 210, 40, 110))
    pygame.draw.circle(tela, "white", (meia_largura, meia_altura), 4)
        
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()