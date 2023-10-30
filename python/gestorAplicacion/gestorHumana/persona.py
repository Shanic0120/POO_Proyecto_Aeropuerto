class Persona:
    aeropuerto=None
    def __init__(self,nombre,cedula,edad,sexo):
        self._nombre = nombre
        self._cedula = cedula
        self._edad = edad
        self._sexo = sexo

    def __str__(self):
        return "Nombre: "+self._nombre+" Cedula: "+str(self._cedula)

    @classmethod
    def setAeropuerto(cls,aeropuerto):
        cls.aeropuerto=aeropuerto

    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad

    def getSexo(self):
        return self._sexo
    
    def setSexo(self,sexo):
        self._sexo=sexo

    def getCedula(self):
        return self._cedula