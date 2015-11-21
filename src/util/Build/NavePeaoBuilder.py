from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNavePeao
from src.cgd import Path


class NavePeaoBuilder(NaveBuilder):
    def __init__(self):
        super(NavePeaoBuilder, self).__init__()
        self.build_dano()
        self.buildimagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()
        
    # """--------------ATRIBUTO------------------"""
    #  @override
    def build_dano(self):
        self.nave_product.dano = 0
    
    #   @override
    def build_imagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + "Imagem/Nave/NavePeao.png"
    
    #  @override
    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + "Imagem/Nave/NaveExplode.png"
    
    #   @override
    def build_som(self):
        self.nave_product.som = "Som/MusicNave.wav"
    
    #   @override
    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNavePeao.FabricaNavePeao(self.nave_product.imagem_nave,
                                                                         self.nave_product.imagem_explosao,
                                                                         self.nave_product.som)
