from src.util.Build import NaveProduct
from src.util.Build import INaveBuilder
from abc import (abstractmethod)


class NaveBuilder(INaveBuilder.INaveBuilder):
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
    def build_imagem_nave(self):
        pass

    @abstractmethod
    def build_imagem_explosao(self):
        pass

    @abstractmethod
    def build_som(self):
        pass
