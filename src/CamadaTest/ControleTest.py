from src.cdp.Habilidades.Municao import Municao
import unittest


class MyTestCase(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)
    """
    def cria_posicao_valido(self):
        val = {}
        resultado = {"x": val["x"] + 30, "y": val["y"] + 15}
        self.assertEqual(resultado, Municao.cria_posicao(val))

    def cria_posicao_invalid0(self):
        val = 100000
        resultado = {}
        self.assertEqual(resultado, Municao.cria_posicao(val))


if __name__ == '__main__':
    unittest.main()
