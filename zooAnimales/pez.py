from zooAnimales.animal import Animal
class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0
    def __init__(self,nombre,edad,habitat,genero, colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    def setColorEscamas(self,c):
        self._colorEscamas=c
    def getColorEscamas(self):
        return self._colorEscamas
    def setCantidadAletas(self,c):
        self._cantidadAletas=c
    def getCantidadAletas(self):
        return self._cantidadAletas
    @classmethod
    def getListado(cls):
        return(cls._listado)
    @classmethod
    def cantidadPeces(cls):
        return(len(cls._listado))
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        s=Pez(nombre,edad,"oceano",genero,"rojo",6)
        cls.salmones+=1
        return s
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        b = Pez(nombre, edad, "oceano", genero, "gris",6)
        cls.bacalaos += 1
        return b