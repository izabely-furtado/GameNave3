from util.Build.NaveBossBuilder import NaveBossBuilder
from util.Build.NaveFugaBuilder import NaveFugaBuilder
from util.Build.NaveGrupoBuilder import NaveGrupoBuilder
from util.Build.NaveJogadorBuilder import NaveJogadorBuilder
from util.Build.NavePeaoBuilder import NavePeaoBuilder
from util.Build.NavePerdidaBuilder import NavePerdidaBuilder
from util.Build.NavePersegueBuilder import NavePersegueBuilder

__author__ = 'IzabelyFurtado'

class NaveFlyweightFactory (object):
    def __init__(self):
        self._standardBoss = [0, None]
        self._standardFuga = [0, None]
        self._standardGrupo = [0, None]
        self._standardJogador = [0, None]
        self._standardPeao = [0, None]
        self._standardPerdida = [0, None]
        self._standardPersegue = [0, None]

    def get_Standard_Boss(self, quantNave):
        e = self._standardBoss
        if e[1] == None:
            e[1] = NaveBossBuilder.__init__(NaveBossBuilder)
            self._standardBoss[0] = quantNave
            self._standardBoss[1] = e[1]
        return e

    def get_Standard_Fuga(self, quantNave):
        e = self._standardFuga
        if e[1] == None:
            e[1] = NaveFugaBuilder.__init__(NaveFugaBuilder)
            self._standardFuga[0] = quantNave
            self._standardFuga[1] = e[1]
        return e

    def get_Standard_Grupo(self, quantNave):
        e = self._standardGrupo
        if e[1] == None:
            e[1] = NaveGrupoBuilder.__init__(NaveGrupoBuilder)
            self._standardGrupo[0] = quantNave
            self._standardGrupo[1] = e[1]
        return e

    def get_Standard_Jogador(self, quantNave):
        e = self._standardJogador
        if e[1] == None:
            e[1] = NaveJogadorBuilder.__init__(NaveJogadorBuilder)
            self._standardJogador[0] = quantNave
            self._standardJogador[1] = e[1]
        return e

    def get_Standard_Peao(self, quantNave):
        e = self._standardPeao
        if e[1] == None:
            e[1] = NavePeaoBuilder.__init__(NavePeaoBuilder)
            self._standardPeao[0] = quantNave
            self._standardPeao[1] = e[1]
        return e

    def get_Standard_Perdida(self, quantNave):
        e = self._standardPerdida
        if e[1] == None:
            e[1] = NavePerdidaBuilder.__init__(NavePerdidaBuilder)
            self._standardPerdida[0] = quantNave
            self._standardPerdida[1] = e[1]
        return e

    def get_Standard_Persegue(self, quantNave):
        e = self._standardPersegue
        if e[1] == None:
            e[1] = NavePersegueBuilder.__init__(NavePersegueBuilder)
            self._standardPersegue[0] = quantNave
            self._standardPersegue[1] = e[1]
        return e

