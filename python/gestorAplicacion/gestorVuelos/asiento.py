class Asiento():
    def __init__(self,numero,clase):
        self._numero=numero
        self._ocupado=False
        self._clase=clase

    def getNumero(self):
        return self._numero

    def setNumero(self,numero):
        self._numero=numero

    def isOcupado(self):
        return self._ocupado

    def setOcupado(self,ocupado):
        self._ocupado=ocupado

    def getClase(self):
        return self._clase

    def setClase(self,clase):
        self._clase=clase