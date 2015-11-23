import pygame
from src.cci.Metricas import Metricas
from src.cdp.Habilidades.Municao import Municao
from src.cdp.Habilidades.Resistencia import Resistencia
from src.src.util.FabricaNaves.FabricaNave import FabricaNave
from src.src.util.FabricaNaves.FabricaNaveFuga import FabricaNaveFuga
from src.src.util.FabricaNaves.FabricaNaveGrupo import FabricaNaveGrupo
from src.src.util.FabricaNaves.FabricaNavePeao import FabricaNavePeao

__author__ = 'IzabelyFurtado'

import unittest
from cgd import Path

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    """---------------------FabricaNave------------------------"""
    def test_som(self):
        val = Path.get_path() + "Som/MusicNave.wav"
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        resultado = pygame.mixer.Sound(val)
        self.assertEqual(resultado, FabricaNave.cria_som(val))

    def test_velocidade(self):
        resultado = {"x": 0, "y": 2}
        self.assertEqual(resultado, FabricaNave.cria_velocidade())

    def test_resistencia(self):
        val1 = 0
        val2 = 0
        resultado = Resistencia(val1, val2)
        self.assertEqual(resultado, FabricaNave.cria_resistencia())

    def test_tiro_ERRO(self):
        val1 = 935 - 60
        resultado = "ERRO"
        self.assertEqual(resultado, FabricaNave.cria_tiro(FabricaNave, val1))

    def test_tiro_CERTO(self):
        nave = FabricaNave.__init__(FabricaNave, "teste", "figteste", "figteste", "somteste")
        val1 = 935 - 30
        resultado = nave.municao.append(Municao(val1))
        self.assertEqual(resultado, nave.cria_tiro(val1))

    """---------------------FabricaNaveFuga------------------------"""
    def test_move_NaveFuga(self):
        nave = FabricaNaveFuga.__init__(FabricaNaveFuga, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        resultado = nave
        resultado.posicao["y"] += 3
        resultado.posicao["x"] += 3
        resultado = resultado.cria_area()
        self.assertEqual(resultado, val1.move())

    """---------------------FabricaNaveGrupo------------------------"""
    def test_move_NaveGrupo_direita(self):
        nave = FabricaNaveGrupo.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "DIREITA"
        val1.posicao["x"] = 1
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["x"] += 1
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.move())

    def test_move_NaveGrupo_esquerda(self):
        nave = FabricaNaveGrupo.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "ESQUERDA"
        val1.posicao["x"] = 1
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["x"] -= 1
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.move())

    def test_move_NaveGrupo_trocaDireita(self):
        nave = FabricaNaveGrupo.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "DIREITA"
        val1.posicao["x"] = Metricas.lim_largura
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["direcao"] = "ESQUERDA"
        resultado.posicao["x"] -= 1
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())

    def test_build_imagem_explosao_NaveGrupo_trocaEsqueda(self):
        nave = FabricaNaveGrupo.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "ESQUERDA"
        val1.posicao["x"] = 0
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["direcao"] = "DIREITA"
        resultado.posicao["x"] += 1
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())

    """---------------------FabricaNavePeao------------------------"""
    def test_build_imagem_explosao_NavePeao_direita(self):
        nave = FabricaNavePeao.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "DIREITA"
        val1.posicao["x"] = 1
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["x"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())


    def test_build_imagem_explosao_NavePeao_esquerda(self):
        nave = FabricaNavePeao.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "ESQUERDA"
        val1.posicao["x"] = 1
        val1.posicao["y"] = 1

        resultado = val1
        resultado.posicao["x"] -= 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())

    def test_build_imagem_explosao_NavePeao_trocaDireita(self):
        nave = FabricaNavePeao.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "DIREITA"
        val1.posicao["x"] = Metricas.lim_largura
        val1.posicao["y"] = 1

        resultado = val1
        val1.posicao["direcao"] = "ESQUERDA"
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())

    def test_build_imagem_explosao_NavePeao_trocaEsquerda(self):
        nave = FabricaNavePeao.__init__(FabricaNaveGrupo, Path.get_path() + "Imagem/Nave/NaveFuga.png", "figteste", "somteste")
        val1 = nave
        val1.posicao["direcao"] = "ESQUERDA"
        val1.posicao["x"] = 0
        val1.posicao["y"] = 1

        resultado = val1
        val1.posicao["direcao"] = "DIREITA"
        resultado.posicao["y"] += 1
        resultado.cria_area()

        self.assertEqual(resultado,val1.build_imagem_explosao())



if __name__ == '__main__':
    unittest.main()
