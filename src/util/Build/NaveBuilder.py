from src.util.Build import NaveProduct


class NaveBuilder(object):
    def __init__(self):
        self.nave_product = NaveProduct.NaveProduct()        # tipo : naveProduct

    def get_nave(self):
        return self.nave_product
    
    #   @abc.abstractmethod
    def build_dano(self):
        pass
    
    #    @abc.abstractmethod
    def build_nave(self):
        pass
    
    #   @abc.abstractmethod
    def buildimagem_nave(self):
        pass
    
    #   @abc.abstractmethod
    def build_imagem_explosao(self):
        pass
    
    #   @abc.abstractmethod
    def build_som(self):
        pass
