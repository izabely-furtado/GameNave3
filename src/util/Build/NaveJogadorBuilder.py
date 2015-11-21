from src.util.Build import NaveBuilder
from src.util.FabricaNaves import FabricaNaveJogador
from src.cgd import Path


class NaveJogadorBuilder(NaveBuilder):
    def __init__(self):
        super(NaveJogadorBuilder, self).__init__()
        self.build_dano()
        self.buildimagem_nave()
        self.build_imagem_explosao()
        self.build_som()
        self.build_nave()
        
    # """--------------ATRIBUTO---------------------"""
    #   @override
    @staticmethod
    def build_dano():
        super(NaveBuilder).nave_product.dano = 0
    
    #   @override
    @staticmethod
    def build_imagem_nave():
        super(NaveBuilder).nave_product.imagem_nave = Path.get_path() + 'Imagem/Nave/TieFighter_archigraphs.png'
    
    #   @override
    @staticmethod
    def build_imagem_explosao():
        super(NaveBuilder).nave_product.imagem_explosao = Path.get_path() + "Imagem/Nave/NaveExplode.png"
    
    #   @override
    @staticmethod
    def build_som():
        super(NaveBuilder).nave_product.som = Path.get_path() + "Som/MusicNave.wav"
    
    #    @override
    def build_nave(self):
        super(NaveBuilder).nave_product.nave_fabrica = \
            FabricaNaveJogador.FabricaNaveJogador("Vai na fé", self.nave_product.imagem_nave,
                                                  self.nave_product.imagem_explosao, self.nave_product.som)
