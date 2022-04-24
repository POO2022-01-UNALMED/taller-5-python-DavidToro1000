class Zoologico():
    def __init__(self,nombre,ubicacion,zonas=[]):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=zonas
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    def setNombre(self, nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    def getZona(self):
        return self._zonas
    def setUbicacion(self, ubicacion):
        self._ubicacion=ubicacion
    def getUbicacion(self):
        return self._ubicacion
    def cantidadTotalAnimales(self):
        return sum([x.cantidadAnimales() for x in self._zonas])