from src.util.Build.NaveBuilder import NaveBuilder
from src.util.FabricaNaves.FabricaNaveGrupo import FabricaNaveGrupo
from src.cgd import Path


class NaveGrupoBuilder(NaveBuilder):
    def __init__(self):
        super(NaveGrupoBuilder, self).__init__()
        self.buildimagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()
        self.build_dano()
        
    # """--------------ATRIBUTO---------------"""
    #   @override
    def build_dano(self):
        self.nave_product.dano = 0
    
    #    @override
    def buildimagem_nave(self):
        self.nave_product.imagem_nave = Path.get_path() + "Imagem/Nave/NaveGrupo.png"
    
    #   @override
    def build_imagem_explosao(self):
        self.nave_product.imagem_explosao = Path.get_path() + "Imagem/Nave/NaveExplode.png"
    
    #  @override
    def build_som(self):
        self.nave_product.som = Path.get_path() + "Som/MusicNave.wav"
    
    #  @override
    def build_nave(self):
        self.nave_product.nave_fabrica = FabricaNaveGrupo(self.nave_product.imagem_nave,
                                                          self.nave_product.imagem_explosao,
                                                          self.nave_product.som)
