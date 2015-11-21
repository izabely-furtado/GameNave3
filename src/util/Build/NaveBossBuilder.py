from src.cgd import Path
from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNaveBoss


class NaveBossBuilder(NaveBuilder):
    def __init__(self):
        super(NaveBossBuilder, self).__init__()
        self.build_dano()
        self.buildimagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()
        
    # """--------------ATRIBUTO------------------------------"""
    #    @override
    def build_dano(self):
        self.nave_product.dano = 0
    
    #   @override
    def buildimagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + 'Imagem/Nave/NaveBoss.png'
    
    #   @override
    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + 'Imagem/Nave/NaveExplode.png'
    
    #   @override
    def build_som(self):
        self.nave_product.som = Path.get_path() + 'Som/MusicNave.wav'

    #    @override
    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNaveBoss.FabricaNaveBoss(self.nave_product.imagem_nave,
                                                                         self.nave_product.imagem_explosao,
                                                                         self.nave_product.som)
