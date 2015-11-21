#!/usr/local/bin/python
import pygame

# -------------------------------------------------------------------------------
# Name:        Nave Maluca 2.1
# Author:      Gislaine
# Created:     09/29/2015
# Copyright:   (c) Gislaine  e Izabely 2015
# Licence:     GIZ
# -------------------------------------------------------------------------------
__author__ = 'Gislaine  e Izabely'

WIDTH = 1000
HEIGTH = 600
LIM_WIDTH = WIDTH - 65
LIM_HEIGTH = HEIGTH - 50


pygame.init()
pygame.font.init()


class Impressao(object):

    def __init__(self):
        self.telao = self.imprime_tela_inicial()
        self.figura = None

    @staticmethod
    def imprime_instrucao():
        titulo = " - Nave maluca -Instrução"

        tela = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
        pygame.display.set_caption(titulo)
        imagem = pygame.image.load("/home/gislaine/Dropbox/"
                                   "GameNave2.8-master/src/cgd/Imagem/instrucao.png").convert_alpha()

        tela.blit(imagem, (0, 0))

        return tela

    @staticmethod
    def imprime_tela_inicial():

        titulo = " - Nave maluca - Let's Play"

        tela = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
        pygame.display.set_caption(titulo)
        imagem = pygame.image.load("/home/gislaine/Dropbox/"
                                   "GameNave2.8-master/src/cgd/Imagem/tela_espaco2.jpg").convert()

        tela.blit(imagem, (0, 0))

        return tela

    @staticmethod
    def start_tela_menu():

        titulo = " - Nave maluca - Menu"

        tela = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
        pygame.display.set_caption(titulo)
        imagem = pygame.image.load("/home/gislaine/Dropbox/GameNave2.8-master/src/cgd/Imagem/tela_menu3.jpg").convert()

        tela.blit(imagem, (0, 0))

        pygame.display.update()

        return tela

    @staticmethod
    def imprime_texto_fim():

        tela = pygame.display.set_mode((WIDTH, HEIGTH), 0, 32)
        titulo = " - Nave maluca - Game over"
        pygame.display.set_caption(titulo)

        imagem = pygame.image.load("/home/gislaine/Dropbox/GameNave2.8-master/src/cgd/Imagem/tela_menu5.jpg").convert()
        tela.blit(imagem, (0, 0))
        font_name = pygame.font.get_default_font()
        game_font = pygame.font.SysFont(font_name, 70)

        text = game_font.render("GAME OVER", True, (255, 0, 0))
        tela.blit(text, (350, 175))

        return tela
