from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self,nombre,edad,habitat,genero, colorPiel, venenoso):
        super().__init__(self,nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    def setColorPiel(self, color):
        self._colorPiel=color
    def getColorPiel(self):
        return self._colorPiel
    def setVenenoso(self, venenoso):
        self._venenoso=venenoso
    def isVenenoso(self):
        return self._venenoso
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def crearRana(cls, nombre, edad, genero):
        r = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1
        return r

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        s = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
        return s