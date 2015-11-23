#!/usr/local/bin/python
import pygame
from src.cci.Metricas import Metricas
from src.cih import ItemMenu
# -------------------------------------------------------------------------------
# Name:        Nave Maluca 1.1
# Author:      Gislaine  e Izabely
# Created:     09/29/2015
# Copyright:   (c) Gislaine  e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------


__author__ = 'Gislaine  e Izabely'

pygame.init()

class JanelaMenu(object):

    def __init__(self, tela, itens, funcoes, font, fonte_size, fonte_cor):
        self.tela = tela
        self.tela_width = self.tela.get_rect().width
        self.tela_heigth = self.tela.get_rect().height
        self.funcoes = funcoes
        self.itens = []
        self.start_itens(itens, font, fonte_size, fonte_cor)
        self.mouse_visivel = True
        self.item_atual = None

    def start_itens(self, itens, fonte, fonte_size, fonte_cor):

        for index, item in enumerate(itens):

            item_menu = ItemMenu.ItemMenu(itens[index], fonte, fonte_size, fonte_cor)
            tamanho_max_texto_bloco = len(itens) * item_menu.height

            pos_x = (self.tela_width / 2) - (item_menu.width / 2)
            pos_y = (self.tela_heigth / 2) - (tamanho_max_texto_bloco / 2) + ((index * 2) + index * item_menu.height)

            item_menu.set_posicao(pos_x, pos_y)

            self.itens.append(item_menu)

    def set_visibilidade_mouse(self):

        if self.mouse_visivel:

            pygame.mouse.set_visible(True)

        else:

            pygame.mouse.set_visible(False)

    def set_selecao_teclado(self, key):

        """ Marca o item do menu que foi escolhido pela teclas up ou down.
        """

        for item in self.itens:

            item.set_italic(False)
            item.set_fonte_cor(Metricas.color_white)

        if self.item_atual is None:

            self.item_atual = 0

        else:

            # Achar o item que foi escolhido
            if key == pygame.K_UP and self.item_atual > 0:

                self.item_atual -= 1

            elif key == pygame.K_UP and self.item_atual == 0:

                self.item_atual = len(self.itens) - 1

            elif key == pygame.K_DOWN and self.item_atual < len(self.itens) - 1:

                self.item_atual += 1

            elif key == pygame.K_DOWN and self.item_atual == len(self.itens) - 1:

                self.item_atual = 0

            self.itens[self.item_atual].set_italic(True)
            self.itens[self.item_atual].set_fonte_cor(Metricas.color_red)

        if key == pygame.K_SPACE or key == pygame.K_RETURN:

            texto = self.itens[self.item_atual].text
            self.funcoes[texto]()

    @staticmethod
    def set_selecao_mouse(item, mpos1, mpos2):

        """ Marca no menu o item que o mouse passou. """

        if item.mouse_selecionado(mpos1, mpos2):

            item.set_fonte_cor(Metricas.color_red)
            item.set_italic(True)

        else:

            item.set_fonte_cor(Metricas.color_white)
            item.set_italic(False)
