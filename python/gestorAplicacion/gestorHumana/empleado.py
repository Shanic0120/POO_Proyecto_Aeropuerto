from .persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, cedula, edad, sexo,sueldo,cargo,experiencia=0):
        super().__init__(nombre, cedula, edad, sexo)
        self._sueldo = sueldo
        self._cargo = cargo
        self._vuelo=None
        self._experiencia = experiencia
        Persona.aeropuerto.addEmpleado(self)

    def getSueldo(self):
        return self._sueldo

    def setSueldo(self,sueldo):
        self._sueldo = sueldo
	
    def getCargo(self):
        return self._cargo
	
    def setCargo(self, cargo):
        self._cargo = cargo

    def getVuelo(self):
        return self._vuelo
    
    def setVuelo(self, vuelo):
        self._vuelo = vuelo
        if vuelo != None:
            self._vuelo.addEmpleado(self)

    def setExperiencia(self, experiencia):
        self._experiencia = experiencia
	
    def getExperiencia(self):
        return self._experiencia
	