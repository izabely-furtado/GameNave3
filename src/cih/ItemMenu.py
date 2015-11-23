#!/usr/local/bin/python
import pygame
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 2.1
# Author:      Gislaine  e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine  e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
from src.cci.Metricas import Metricas

__author__ = 'Gislaine  e Izabely'


pygame.init()

class ItemMenu(pygame.font.Font):

    def __init__(self, text, font=None, fonte_size=30, fonte_cor=Metricas.color_white, pos_x=0, pos_y=0):

        pygame.font.Font.__init__(self, font, fonte_size)
        self.text = text
        self.fonte_size = fonte_size
        self.fonte_cor = fonte_cor
        self.label = self.render(self.text, 1, self.fonte_cor)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_posicao(self, x, y):

        self.pos_x = x
        self.pos_y = y

    def set_fonte_cor(self, cor):

        self.fonte_cor = cor
        self.label = self.render(self.text, 1, self.fonte_cor)

    def mouse_selecionado(self, posx, posy):

        if self.pos_x <= posx <= self.pos_x + self.width:

            if self.pos_y + self.height >= posy >= self.pos_y:

                    return True

        return False
