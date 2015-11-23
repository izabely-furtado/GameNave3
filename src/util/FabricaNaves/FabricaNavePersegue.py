import random
from src.cci.Metricas import Metricas
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga

class FabricaNavePersegue(FabricaNaveInimiga.FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super().__init__('Nave Perseguidora', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 40
        self.municao = self.cria_municao()

    # """---------------ACOES----------------------"""
    # @abc.override
    def move(self):
        aleatorio = random.randint(0, 10)
        if (self.posicao["x"] < Metricas.lim_largura) and (self.posicao["x"] > 0):
            if aleatorio > 6:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == Metricas.lim_largura:
            self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["x"] == 0:
            self.posicao["x"] += self.velocidade["x"]+2

        self.posicao["y"] += self.velocidade["y"]+2
        self.cria_area()

    # """------------ATRIBUTO-------------------"""
    
    # @abc.override
    @staticmethod
    def cria_velocidade():
        return {"x": 2, "y": 2}
    
    # @abc.override
    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(4, 2)
