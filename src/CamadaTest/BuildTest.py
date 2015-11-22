from util.Build.NaveProduct import NaveProduct

__author__ = 'IzabelyFurtado'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_dano_ERRO(self):
        nave = NaveProduct.__init__(NaveProduct)
        nave.dano = 0
        val = -1
        resultado = nave
        self.assertEqual(resultado, nave.set_dano(val))

    def test_dano_CERTO(self):
        nave = NaveProduct.__init__(NaveProduct)
        nave.dano = 0
        val = 2
        resultado = nave
        resultado.dano = 2
        self.assertEqual(resultado, nave.set_dano(val))


if __name__ == '__main__':
    unittest.main()
