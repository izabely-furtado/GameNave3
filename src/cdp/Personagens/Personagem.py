from src.util.Build import NaveJogoDirector


class Personagem(object):
    def __init__(self, nave):
        self.veiculo = Personagem.criando_nave(nave)

    @staticmethod
    def criando_nave(nave_builder):
        nave_jogador = NaveJogoDirector.NaveJogoDirector(nave_builder)
        nave_jogador.contruir_nave()
        nave = nave_jogador.get_nave()
        return nave

    def get_area(self):
        return self.veiculo.nave.get_area()

    def armamento(self):
        return self.veiculo.nave.municao

    def remove_tiro(self, tiro):
        assert isinstance(self.veiculo, object)
        self.veiculo.nave.municao.remove(tiro)

    def get_posicao_y(self):
        return self.veiculo.nave.posicao["y"]

    def get_posicao_x(self):
        return self.veiculo.nave.posicao["x"]

    def set_posicao_y(self, valor):
        self.veiculo.nave.posicao["y"] = valor

    def set_posicao_x(self, valor):
        self.veiculo.nave.posicao["x"] = valor

    def start_area(self):
        return self.veiculo.nave.cria_area()

    def atira(self):
        self.veiculo.nave.atira()

    def figura(self):
        return self.veiculo.imagem_nave

    def atingido(self):
        return self.veiculo.nave.atingido

    def foi_atingido(self):
        self.veiculo.nave.atingido = True

    def move(self):
        self.veiculo.nave.move()
