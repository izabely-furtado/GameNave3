from src.util.FabricaItem import FabricaItem


class FabricaMunicao(FabricaItem):
    def __init__(self, imagem, preco, probabilidade):
        super(FabricaMunicao, self).__init__('Municao', imagem, preco, probabilidade)
        
    #  @abc.abstract
    def modificacoes(self, jogador):
        # return 0
        pass
