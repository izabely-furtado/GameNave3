from src.util.FabricaNaves import FabricaNave
from src.cgd import Path


class NaveProduct(object):
    def __init__(self):
        self.dano = 0
        self.nave_fabrica = FabricaNave.FabricaNave('nome', Path.get_path() + '/Imagem/X Wing.png',
                                                    Path.get_path() + '/Imagem/Item/Clone0.png',
                                                    Path.get_path() + '/Som/MusicNave.wav')      # tipo : FabricaNaves
        self.imagem_nave = Path.get_path() + '/Imagem/X Wing.png'                                # endereco imagem
        self.imagem_explosao = Path.get_path() + '/Imagem/Item/Clone0.png'
        self.som = Path.get_path() + '/Som/MusicNave.wav'
        
    def get_dano(self):
        return self.dano
    
    def set_dano(self, dano):
        if dano >= 0:
            self.dano = dano
    
    def get_nave(self):
        return self.nave_fabrica
    
    def sofre_dano(self, dano):
        if dano > 0:
            self.dano += dano
    
    def set_imagem_nave(self, imagem):
        self.imagem_nave = imagem
