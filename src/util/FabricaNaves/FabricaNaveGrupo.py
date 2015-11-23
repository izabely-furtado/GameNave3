from src.cci.Metricas import Metricas
from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga


class FabricaNaveGrupo(FabricaNaveInimiga.FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super().__init__('Nave de Grupo', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 10
        
    # """---------------ACOES-------------------"""
    #    @abc.override
    def move(self):
        if self.posicao["direcao"] == "DIREITA":
            if self.posicao["x"] < Metricas.lim_largura:
                self.posicao["x"] += self.velocidade["x"]
            else:
                self.posicao["direcao"] = "ESQUERDA"
                self.posicao["x"] -= self.velocidade["x"]
        elif self.posicao["direcao"] == "ESQUERDA":
            if self.posicao["x"] > 0:
                self.posicao["x"] -= self.velocidade["x"]
            else:
                self.posicao["direcao"] = "DIREITA"
                self.posicao["x"] += self.velocidade["x"]
        
        self.posicao["y"] += self.velocidade["y"]    
        self.cria_area()
        
    # """--------------ATRIBUTO--------------------"""
    #   @abc.override
    @staticmethod
    def cria_velocidade():
        return {"x": 1, "y": 1}
    
    #  @abc.override
    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(1, 1)
