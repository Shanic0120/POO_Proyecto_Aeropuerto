class Aeropuerto:
    def __init__(self,nombre=None):
        self._nombre=nombre
        self._vuelos=[]
        self._pasajeros=[]
        self._empleados=[]
        self._aviones=[]
        self._transaccionesKeys=[]
        self._transaccionesValues=[]
        self._dinero=0

    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre):
        self._nombre=nombre

    def getVuelos(self):
        return self._vuelos

    def setVuelos(self,vuelos):
        self._vuelos=vuelos

    def addVuelo(self,vuelo):
        self._vuelos.append(vuelo)

    def getPasajeros(self):
        return self._pasajeros

    def setPasajeros(self,pasajeros):
        self._pasajeros=pasajeros

    def addPasajero(self,pasajeros):
        self._pasajeros.append(pasajeros)

    def getEmpleados(self):
        return self._empleados

    def setEmpleados(self,empleados):
        self._empleados=empleados

    def addEmpleado(self,empleados):
        self._empleados.append(empleados)

    def getAviones(self):
        return self._aviones

    def setAviones(self,aviones):
        self._aviones=aviones

    def addAvion(self,aviones):
        self._aviones.append(aviones)

    def getTransaccionesKeys(self):
        return self._transaccionesKeys

    def setTransaccionesKeys(self,transaccionesKeys):
        self._transaccionesKeys=transaccionesKeys

    def addTransaccionesKeys(self,transaccionesKeys):
        self._transaccionesKeys.append(transaccionesKeys)

    def getTransaccionesValues(self):
        return self._transaccionesValues

    def setTransaccionesValues(self,transaccionesValues):
        self._transaccionesValues=transaccionesValues

    def addTransaccionesValues(self,transaccionesValues):
        self._transaccionesValues.append(transaccionesValues)

    def getDinero(self):
        return self._dinero

    def setDinero(self,dinero):
        self._dinero=dinero

    def buscarEmpleado(self,id):
        for i in self._empleados:
            if i.getCedula()==id:
                return i
    def buscarPasajero(self,id):
        for i in self._pasajeros:
            if i.getCedula()==id:
                return i
    def ingresarDinero(self, pago):
        self._dinero += pago

    def transaccion(self, concepto, valor):
        self._transaccionesKeys.append(concepto)
        self._transaccionesValues.append(valor)
        self.ingresarDinero(valor)

    def buscarVuelo(self,sala,modelo,destino):
        for i in self._vuelos:
            if i.getDestino()==destino and i.getAvion().getModelo()==modelo and i.getSalaEmbarque()==sala:
                return i

    def buscarAvion(self,modelo):
        for i in self._aviones:
            if i.getModelo()==modelo:
                return i

    def despedirEmpleado(self,empleado):
        for i in self._empleados:
            if i==empleado:
                try:
                    empleado.getVuelo().remove(empleado)
                except:
                    pass
                self._empleados.remove(empleado)

    def eliminarPasajero(self,pasajero):
        for i in self._pasajeros:
            if i==pasajero:
                try:
                    pasajero.getVuelo().remove(pasajero)
                except:
                    pass
                self._pasajeros.remove(pasajero)

    def cancelarVuelo(self,vuelo):
        for i in self._vuelos:
            if i==vuelo:
                try:
                    vuelo.getAvion().remove(vuelo)
                except:
                    pass
                self._vuelos.remove(vuelo)

    def cancelarAvion(self,avion):
        for i in self._aviones:
            if i==avion:
                try:
                    avion.getvuelo().remove(avion)
                except:
                    pass
                self._aviones.remove(avion)
