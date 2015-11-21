from src.util.FabricaItem import FabricaClone
from src.cgd import Path


class FabricaClone1(FabricaClone):
    def __init__(self):
        super(FabricaClone1, self).__init__(Path.get_path() + "Imagem/Item/Clone1.png")
