# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "20121bsi0040"
__date__ = "$20/11/2015 09:10:50$"
from enum import Enum;

class Metricas(Enum):
    largura = 1000
    altura = 600
    lim_largura = self.largura - 65
    lim_altura = self.altura - 50
    color_white = (255, 255, 255)
    fps = 60
    