from src.cdp.Habilidades import Resistencia
from src.cdp.Personagens import Personagem


class Jogador(Personagem):
    def __init__(self, nome, imagem_id, nave_escolhida):
        super(Jogador.criando_nave_jogador(nave_escolhida))
        self.nome = nome
        self.imagem_id = imagem_id
        self.fase = 1
        self.pontos = 0
        self.vidas = 3

    def ganha_pontos(self, pontos):
        if pontos > 0:
            self.pontos += pontos
    
    def compra_item(self, item):
        if self.pontos >= item.preco:
            self.pontos -= item.preco
            item.modificacoes(self)
        
    def avanca_fase(self):
        self.fase += 1
    
    def mais_vida(self):
        self.vida += 1
        
    def troca_nave(self, nave_escolhida):
        # self.nave = self.criando_navegador(nave_escolhida)
        pass
        
    def restaura(self):
        self.nave.set_dano(0)
    
    def clone(self):
        self.nave.nave.resistencia = Resistencia.Resistencia(10, 20)
