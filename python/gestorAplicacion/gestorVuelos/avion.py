import random
from .asiento import Asiento
class Avion():
    _aeropuerto=None
    def __init__(self,modelo,pesoMaximo,valor,cantidadAsientos=0):
        self._asientos=[]
        if cantidadAsientos==0:
            self.genAsientos(15,20)
        else:
            self.genAsientos(cantidadAsientos,cantidadAsientos)

        self._id=Avion.nuevoID()
        self._modelo=modelo
        self._pesoMaximo=pesoMaximo
        self._valor=valor
        Avion._aeropuerto.addAvion(self)        

    def getId(self):
        return self._id
    def setId(self,id):
        self._id=id

    def getModelo(self):
        return self._modelo
    def setModelo(self,modelo):
        self._modelo=modelo

    def getPesoMaximo(self):
        return self._pesoMaximo
    def setPesoMaximo(self,pesoMaximo):
        self._pesoMaximo=pesoMaximo
    
    def getAsientos(self):
        return self._asientos
    def setAsientos(self,asientos):
        self._asientos=asientos
    def addAsiento(self,asiento):
        self._asientos.append(asiento)

    def getValor(self):
        return self._valor
    def setValor(self,valor):
        self._valor=valor

    @classmethod
    def setAeropuerto(cls,aeropuerto):
        cls._aeropuerto=aeropuerto

    @classmethod
    def nuevoID(cls):
        try:
            return cls._aeropuerto.getAviones()[len(cls._aeropuerto.getAviones())-1].getId()+1
        except:
            return 1

    def genAsientos(self,min,max):
        tipoAsiento=["Turista","Ejecutiva","Primera clase"]
        cantidad=random.randint(min,max)
        for i in range(1,cantidad+1):
            ind=random.randint(0,2)
            self._asientos.append(Asiento(i,tipoAsiento[ind]))

    def buscarAsiento(self,nro):
        for i in self._asientos:
            if i.getNumero()==nro:
                return i
