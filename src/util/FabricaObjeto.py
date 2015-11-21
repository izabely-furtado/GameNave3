import pygame
from pygame.rect import Rect


class FabricaObjeto(object):
    def __init__(self, nome, imagem_escolhida):
        self.nome = nome
        self.imagemObjeto = self.cria_figura(imagem_escolhida)
        self.posicao = self.cria_posicao()
        self.area = self.cria_area()
        self.velocidade = self.cria_velocidade()
        self.atingido = False
        
    # """-----------ACOES-------------------"""
    def get_area(self):
        return self.area

    #    @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.cria_area()
    
    # """--------ATRIBUTOS----------------"""
    @staticmethod
    def cria_figura(figura):
        f = pygame.image.load(figura).convert_alpha()
        return f

    @staticmethod
    def cria_posicao():
        return {"x": 0, "y": 0, "direcao": "DIREITA"}

    def cria_area(self):
        self.area = Rect(self.posicao["x"], self.posicao["y"],
                         self.imagemObjeto.get_width(), self.imagemObjeto.get_height())
        return Rect(self.posicao["x"], self.posicao["y"], self.imagemObjeto.get_width(), self.imagemObjeto.get_height())

    @staticmethod
    def cria_velocidade():
        return {"x": 0, "y": 2}
