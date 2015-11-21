from src.util.FabricaItem import FabricaMunicao
from src.cgd import Path


class FabricaMunicao1(FabricaMunicao):
    def __init__(self):
        super(FabricaMunicao1, self).__init__(Path.get_path() + "Imagem/Item/Municao1.png", 200, 5)
