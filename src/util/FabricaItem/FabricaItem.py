from src.util import FabricaObjeto


class FabricaItem(FabricaObjeto):
    def __init__(self, nome, imagem_escolhida, preco, probabilidade):
        super(FabricaItem, self).__init__(nome, imagem_escolhida)
        self.preco = preco
        self.probabilidade = probabilidade
        
    # """-----------ACOES-------------------"""
    def modificacoes(self, nave):
        # return 0
        pass
