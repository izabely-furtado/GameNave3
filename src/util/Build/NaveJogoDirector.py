

class NaveJogoDirector(object):
    def __init__(self, nave_builder):
        self.montadora = nave_builder
        
    def contruir_nave(self):
        self.montadora.build_dano()
        self.montadora.build_imagem_nave()
        self.montadora.build_imagem_explode()
        self.montadora.build_som()
        self.montadora.build_nave()

    def get_nave(self):
        return self.montadora.nave
