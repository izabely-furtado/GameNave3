from abc import (ABCMeta, abstractmethod)


class FabricaAtributoNave(metaclass=ABCMeta):
    
    # ACOES
    @abstractmethod
    def move(self):
        pass
        
    # ATRIBUTOS
    @abstractmethod
    def cria_figura(self, figura):
        pass
    
    @abstractmethod
    def cria_posicao(self):
        pass
    
    @abstractmethod
    def cria_area(self):
        pass
    
    @abstractmethod
    def cria_velocidade(self):
        pass
