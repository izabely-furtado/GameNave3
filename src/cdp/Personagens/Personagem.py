from src.util.Build import NaveJogoDirector


class Personagem(object):
    def __init__(self, nave):
        self.veiculo = Personagem.criando_nave(nave)

    @staticmethod
    def criando_nave(nave_builder):
        nave_jogador = NaveJogoDirector.NaveJogoDirector(nave_builder)
        nave_jogador.contruir_nave()
        nave = nave_jogador.get_nave()
        nave = nave.nave_fabrica
        return nave

    def get_area(self):
        return self.veiculo.get_area()

    def municao(self):
        return self.veiculo.municao

    def remove_tiro(self, tiro):
        assert isinstance(self.veiculo, object)
        self.veiculo.municao.remove(tiro)

    def get_posicao_y(self):
        return self.veiculo.posicao["y"]

    def get_posicao_x(self):
        return self.veiculo.posicao["x"]

    def set_posicao_y(self, valor):
        self.veiculo.posicao["y"] = valor

    def set_posicao_x(self, valor):
        self.veiculo.posicao["x"] = valor

    def start_area(self):
        return self.veiculo.cria_area()

    def atira(self):
        self.veiculo.atira()

    def figura(self):
        return self.veiculo.imagemObjeto

    def atingido(self):
        return self.veiculo.atingido

    def foi_atingido(self):
        self.veiculo.atingido = True

    def move(self):
        self.veiculo.move()
