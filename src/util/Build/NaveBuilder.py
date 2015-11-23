from util.Build import NaveProduct
from util.Build.INaveBuilder import INaveBuilder
from abc import (abstractmethod)

class NaveBuilder(INaveBuilder):
    def __init__(self):
        self.nave_product = NaveProduct.NaveProduct()        # tipo : naveProduct

    def get_nave(self):
        return self.nave_product

    @abstractmethod
    def build_dano(self):
        pass

    @abstractmethod
    def build_nave(self):
        pass

    @abstractmethod
    def buildimagem_nave(self):
        pass

    @abstractmethod
    def build_imagem_explosao(self):
        pass

    @abstractmethod
    def build_som(self):
        pass
