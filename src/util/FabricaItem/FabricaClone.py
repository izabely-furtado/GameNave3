from src.util.FabricaItem import FabricaItem


class FabricaClone(FabricaItem):
    def __init__(self, imagem):
        super(FabricaClone, self).__init__('Clone', imagem, 100, 6)
        
    @staticmethod
    def modificacoes(jogador):
        jogador.clone(jogador)
