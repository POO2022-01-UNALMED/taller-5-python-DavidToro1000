from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0
    def __init__(self,nombre,edad,habitat,genero, colorEscamas, largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    def setColorEscamas(self,c):
        self._colorEscamas=c
    def getColorEscamas(self):
        return self._colorEscamas
    def setLargoCola(self,l):
        self._largoCola=l
    def getLargoCola(self):
        return self._largoCola
    @classmethod
    def getListado(cls):
        return(cls._listado)
    @classmethod
    def cantidadReptiles(cls):
        return(len(cls._listado))
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        i=Reptil(nombre,edad,"humedal",genero,"verde", 3)
        cls.iguanas+=1
        return i
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        s = Reptil(nombre, edad, "jungla", genero, "blanco",1)
        cls.serpientes += 1
        return s