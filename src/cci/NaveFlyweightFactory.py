#!/usr/local/bin/python

from src.util.Build import NaveBossBuilder
from src.util.Build import NaveFugaBuilder
from src.util.Build import NaveGrupoBuilder
from src.util.Build import NaveJogadorBuilder
from src.util.Build import NavePeaoBuilder
from src.util.Build import NavePerdidaBuilder
from src.util.Build import NavePersegueBuilder

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 3.1
# Author:      Gislaine e Izabely
# Created:     x/x/x
# Copyright:   (c) Gislaine e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------

__author__ = 'Gislaine  e Izabely'


class NaveFlyweightFactory (object):
    def __init__(self):
        self._standard_boss = [0, None]
        self._standard_fuga = [0, None]
        self._standard_grupo = [0, None]
        self._standard_jogador = [0, None]
        self._standard_peao = [0, None]
        self._standard_perdida = [0, None]
        self._standard_persegue = [0, None]

    def get_standard_boss(self, quant_nave):
        e = self._standard_boss
        if e[1] == None:
            e[1] = NaveBossBuilder.NaveBossBuilder()
            self._standard_boss[1] = e[1]
        self._standard_boss[0] += quant_nave
        return e

    def get_standard_fuga(self, quantNave):
        e = self._standard_fuga
        if e[1] == None:
            e[1] = NaveFugaBuilder.NaveFugaBuilder()
            self._standard_fuga[1] = e[1]
        self._standard_boss[0] += quantNave
        return e

    def get_standard_grupo(self, quantNave):
        e = self._standard_grupo
        if e[1] == None:
            e[1] = NaveGrupoBuilder.NaveGrupoBuilder()
            self._standard_grupo[1] = e[1]
        self._standard_boss[0] += quantNave
        return e

    def get_standard_jogador(self, quantNave):
        e = self._standard_jogador
        if not e[1]:
            print("jkioi")
            e[1] = NaveJogadorBuilder.NaveJogadorBuilder()
            self._standard_jogador[1] = e[1]
        self._standard_boss[0] += quantNave
        return e

    def get_standard_peao(self, quantNave):
        e = self._standard_peao
        if not e[1]:
            e[1] = NavePeaoBuilder.NavePeaoBuilder()
            self._standard_peao[1] = e[1]
        self._standard_boss[0] += quantNave
        return e

    def get_standard_perdida(self, quantNave):
        e = self._standard_perdida
        if not e[1]:
            e[1] = NavePerdidaBuilder.NavePerdidaBuilder()
            self._standard_perdida[1] = e[1]
        self._standard_boss[0] += quantNave
        return e

    def get_standard_persegue(self, quantNave):
        e = self._standard_persegue
        if not e[1]:
            e[1] = NavePersegueBuilder.NavePersegueBuilder()
            self._standard_persegue[1] = e[1]
        self._standard_boss[0] += quantNave
        return e
