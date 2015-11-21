from src.util.FabricaItem import FabricaClone
from src.cgd import Path


class FabricaClone2(FabricaClone):
    def __init__(self):
        super(FabricaClone2, self).__init__(Path.get_path() + "Imagem/Item/Clone2.png")
