#Heitor Augusto Paula Hardman e Lucas Rangel Littig 
import pygame as pg
from pathlib import Path
import gif_pygame

# Encontrando os caminhos de arquivo
pasta_assets = Path.cwd() / 'assets'
pasta_sprites = pasta_assets / 'sprites'
pasta_sons = pasta_assets / 'sounds'

#Inicio
pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
largura = 1280
altura = 720

tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Futebol de Botão')
relogio = pg.time.Clock()

fundo_img = pg.image.load(pasta_sprites / 'campo.jpg').convert()
fundo = pg.transform.scale(fundo_img, (largura, altura))

caminho_gif = pasta_sprites / 'campo_animado.gif'
example_gif = gif_pygame.load(caminho_gif)


gif_pygame.transform.scale(example_gif, (largura, altura))

#Audios
#Musica de fundo
pg.mixer.music.load(pasta_sons / "som_fundo.mp3")
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(-1)

gol_som = pg.mixer.Sound(pasta_sons / "som_gol.wav")
gol_som.set_volume(0.4)

rede_som = pg.mixer.Sound(pasta_sons / "som_rede.wav")
rede_som.set_volume(0.4)

apito_som = pg.mixer.Sound(pasta_sons / "apito.wav")
apito_som.set_volume(0.4)

toque_som = pg.mixer.Sound(pasta_sons / "som_toque.wav")
toque_som.set_volume(0.4)

# Classes Sprites
class Peca(pg.sprite.Sprite):
    def __init__(self, caminho_imagem, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load(caminho_imagem).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

class Bola(pg.sprite.Sprite):
    def __init__(self, caminho_imagem, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load(caminho_imagem).convert_alpha()
        
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        
todos_sprites = pg.sprite.Group()
caminho_bola = pasta_sprites / 'bola.png'
bola = Bola(caminho_bola, largura // 2, altura // 2)
todos_sprites.add(bola)

# loop principal
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
            
    # Comemoração
    
    example_gif.render(tela, (0, 0))
    todos_sprites.draw(tela)
    pg.display.flip()
    relogio.tick(60)
    '''
    # Campo de jogo
    tela.blit(fundo, (0,0))
    todos_sprites.draw(tela)
    pg.display.flip()
    relogio.tick(60)'''
