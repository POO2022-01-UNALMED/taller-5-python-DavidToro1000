from animal import Animal
class Ave(Animal):
    _listado=[]
    aguilas=0
    halcones=0
    def __init__(self,nombre,edad,habitat,genero, colorPlumas):
        super().__init__(self,nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    def setColorPlumas(self,color):
        self._colorPlumas=color
    def getColorPlumas(self):
        return self._colorPlumas
    @classmethod
    def getListado(cls):
        return(cls._listado)
    @classmethod
    def cantidadAves(cls):
        return(len(cls._listado))
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        h=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        Ave.halcones+=1
        return h
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        a = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas += 1
        return a