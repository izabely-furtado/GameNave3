from src.cdp.Habilidades.Municao import Municao

__author__ = 'IzabelyFurtado'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_posicao_municao_ERRO1(self):
        val = 905
        resultado = {}
        self.assertEqual(resultado, Municao.cria_posicao(val))

    def test_posicao_municao_ERRO2(self):
        val = 535
        resultado = {}
        self.assertEqual(resultado, Municao.cria_posicao(val))

    def test_posicao_municao_CERTO(self):
        val = 1
        resultado = 1
        self.assertEqual(resultado, Municao.cria_posicao(val))


if __name__ == '__main__':
    unittest.main()
