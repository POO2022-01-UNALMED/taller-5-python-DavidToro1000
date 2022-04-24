from animal import Animal
class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0
    def __init__(self,nombre,edad,habitat,genero, pelaje, patas):
        super().__init__(self,nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    def setPelaje(self,p):
        self._pelaje=p
    def isPelaje(self):
        return self._pelaje
    def setPatas(self,p):
        self._patas=p
    def getPatas(self):
        return self._patas
    @classmethod
    def getListado(cls):
        return(cls._listado)
    @classmethod
    def cantidadMamiferos(cls):
        return(len(cls._listado))
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        c=Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos+=1
        return c
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        l = Mamifero(nombre, edad, "selva", genero, True,4)
        cls.leones += 1
        return l