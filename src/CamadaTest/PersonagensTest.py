from src.cdp.Personagens.Jogador import Jogador

__author__ = 'IzabelyFurtado'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_pontuacao_ERRO(self):
        jogador = Jogador.__init__(Jogador, "", "", "")
        val = -2
        resultado = jogador.pontos
        self.assertEqual(resultado, jogador.ganha_pontos(val))

    def test_pontuacao_CERTO(self):
        jogador = Jogador.__init__(Jogador, "", "", "")
        val = 2
        resultado = jogador.pontos + 2
        self.assertEqual(resultado, jogador.ganha_pontos(val))

    def test_fase(self):
        jogador = Jogador.__init__(Jogador, "", "", "")
        resultado = jogador
        resultado.fase += 1
        self.assertEqual(resultado, jogador.avanca_fase())

    def test_vida(self):
        jogador = Jogador.__init__(Jogador, "", "", "")
        resultado = jogador
        resultado.vidas += 1
        self.assertEqual(resultado, jogador.mais_vida())

    def test_dano(self):
        jogador = Jogador.__init__(Jogador, "", "", "")
        resultado = jogador
        resultado.nave.dano = 0
        self.assertEqual(resultado, jogador.restaura())


if __name__ == '__main__':
    unittest.main()
