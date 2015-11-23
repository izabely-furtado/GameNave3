import pygame
from src.cdp.Habilidades import Resistencia
from src.cdp.Habilidades import Municao
from src.util import FabricaObjeto

class FabricaNave(FabricaObjeto.FabricaObjeto):

    def __init__(self, nome, figura_nave, figura_explosao, som):
        super().__init__(nome, figura_nave)
        self.som = self.cria_som(som)
        self.resistencia = self.cria_resistencia()
        self.explosao = self.cria_explosao(figura_explosao)
        self.municao = None

    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.cria_area()
    
    # @abc.override
    def explode(self, figura_explosao):
        if self.atingido:
            return self.cria_explosao(figura_explosao)

    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.municao[-1].atira()
        # self.buzina()

    @staticmethod
    def cria_som(som):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        return pygame.mixer.Sound(som)

    def buzina(self):
        self.som.set_volume(0.1)
        self.som.play()

    @staticmethod
    def cria_velocidade():
        return {"x": 0, "y": 2}

    @staticmethod
    def cria_resistencia():
        resiste = Resistencia.Resistencia(0, 0)
        return resiste

    @staticmethod
    def cria_explosao(figura_explosao):
        return FabricaNave.cria_figura(figura_explosao)

    def cria_tiro(self, pos_nave):
        m = Municao.Municao(pos_nave)
        if m.posicao == {}:
            m = "ERRO"
        else:
            self.municao.append(m)
        return m

    @staticmethod
    def cria_municao():
        return []
