from src.cdp.Habilidades import Resistencia
from src.util.FabricaNaves import FabricaNave


class FabricaNaveJogador(FabricaNave):
    def __init__(self, nome, figura_nave, figura_explosao, som):
        super(FabricaNaveJogador).__init__(nome, figura_nave, figura_explosao, som)
        self.tempoMissel = 0
        self.municao = self.cria_municao()

    # """---------------ACOES----------------------"""
    #  @abc.override
    def move(self):
        self.posicao["y"] += self.velocidade["y"]
        self.cria_area()

    """
    #  @abc.override
    def atira(self):
        if self.cria_tiro(self.posicao) != "ERRO":
            self.cria_tiro(self.posicao)
        self.municao[-1].atira()
        self.buzina()
    """
    # """--------------ATRIBUTO------------------"""

    # @abc.override
    @staticmethod
    def cria_velocidade():
        return {"x": 2, "y": 2}
    
    # @abc.override
    @staticmethod
    def cria_resistencia():
        return Resistencia.Resistencia(10, 2)
