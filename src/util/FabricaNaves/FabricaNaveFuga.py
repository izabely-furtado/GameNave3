from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNaveInimiga


class FabricaNaveFuga(FabricaNaveInimiga):
    def __init__(self, figura_nave, figura_explosao, som):
        super(FabricaNaveFuga, self).__init__('Nave de Fuga', figura_nave, figura_explosao, som)
        self.pontuacao_derrotar = 50
        
    # """---------------ACOES-----------------"""
    # abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.posicao["x"] += self.velocidade["x"]
        self.cria_area()
        
    # """--------------ATRIBUTO---------------"""
    # abc.override
    @staticmethod
    def cria_velocidade():
        return {"x": 3, "y": 3}
    
    # abc.override
    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(5, 1)
