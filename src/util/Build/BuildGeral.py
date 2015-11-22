__author__ = 'IzabelyFurtado'

class BuildGeral(object):
    @staticmethod
    def criar(name):
        path = 'util.Build.Nave'+ name + 'Builder'
        #'util.Build.NavesGrupoBuilder'
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod.criar()

#BuildGeral.criar('Grupo')