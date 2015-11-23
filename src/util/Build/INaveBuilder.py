__author__ = 'IzabelyFurtado'

from abc import (ABCMeta, abstractmethod)


class INaveBuilder(metaclass=ABCMeta):

    @abstractmethod
    def get_nave(self):
        pass

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
