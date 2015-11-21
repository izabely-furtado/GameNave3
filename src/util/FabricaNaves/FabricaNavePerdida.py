import random
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


class FabricaNavePerdida(FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super(FabricaNavePerdida).__init__('Nave Perdida', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 20
        self.municao = self.cria_municao()

    # """---------------ACOES--------------------"""
    #  @abc.override
    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < LIM_WIDTH) and (self.posicao["x"] > 0):
            if aleatorio > 5:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == LIM_WIDTH:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]
        
        self.posicao["y"] += self.velocidade["y"]    
        self.cria_area()
    """
    #   @abc.override
    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.municao[-1].atira()
        self.municao.buzina()
    """
    # """--------------ATRIBUTO------------------------------------------------"""

    # @abc.override
    @staticmethod
    def cria_velocidade():
        return {"x": 1, "y": 1}
    
    # @abc.override
    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(2, 2)
