from .persona import Persona
class Pasajero(Persona):
    def __init__(self, nombre, cedula, edad, sexo,inversion=0):
        super().__init__(nombre, cedula, edad, sexo)
        self._inversion=inversion
        self._asiento=None
        self._vuelo=None
        self._equipajes=[]
        Persona.aeropuerto.addPasajero(self)
        
    def getInversion(self):
        return self._inversion

    def setInversion(self,inversion):
        self._inversion=inversion

    def getAsiento(self):
        return self._asiento

    def setAsiento(self,asiento):
        self._asiento=asiento

    def getVuelo(self):
        return self._vuelo

    def setVuelo(self,vuelo):
        self._vuelo=vuelo
        self._vuelo.addPasajero(self)

    def getEquipajes(self):
        return self._equipajes

    def addEquipaje(self,equipaje):
        self._equipajes.append(equipaje)
        equipaje.setPropietario(self)

    def setEquipaje(self,equipaje):
        self._equipaje=equipaje