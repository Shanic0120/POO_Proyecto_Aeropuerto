class Equipaje():
    def __init__(self,peso):
        self._peso=peso
        self._propietario=None

    def getPeso(self):
        return self._peso
    def setPeso(self,peso):
        self._peso=peso

    def getPropietario(self):
        return self._propietario
    def setPropietario(self,propietario):
        self._propietario=propietario