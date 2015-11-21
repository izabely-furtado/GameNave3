from src.util.FabricaItem import FabricaItem
from src.cgd import Path


class FabricaRestaura(FabricaItem):
    def __init__(self):
        super(FabricaRestaura, self).__init__('Restaura', Path.get_path() + "Imagem/Item/Restaura.png", 100, 30)
        
    #  @abc.abstract
    def modificacoes(self, jogador):
        jogador.restaura(jogador)
