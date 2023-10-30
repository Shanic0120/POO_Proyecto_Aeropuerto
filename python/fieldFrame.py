from tkinter import *
from tkinter import messagebox
from excepciones.excepcionTipo import *

class FieldFrame(Frame):
    
    def __init__(self, ventana, tituloCriterios, criterios, tituloValores, valores, habilitado,pack=True):
        super().__init__(ventana)
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        if pack:
            self.pack()
        self.config(relief = "groove") 
        self.config(bd=20)
        self.config(borderwidth=2) 

        # Lista de elementos
        self._elementos = []

        # Crear y colocar titulo de los criterios
        labelTituloCriterios = Label(self, text = tituloCriterios, font= ("Courier", 14))
        labelTituloCriterios.grid(column=0, row=0, padx = (5,5), pady = (5,5))

        # Crear y colocar titulo de los valores
        labelTituloValores = Label(self, text = tituloValores, font= ("Courier", 14))
        labelTituloValores.grid(column=1, row=0, padx = (5,5), pady = (5,5))

        # Crear cada uno de los criterios
        for  i in range(len(criterios)):
            # Crear y colocar nombre de cada criterio
            labelCriterio = Label(self, text = criterios[i], font = ("Courier", 12))
            labelCriterio.grid(column=0, row=i+1, padx = (5,5), pady = (5,5))

            # Crear y colocar entrada de cada criterio
            global entryValor
            entryValor = Entry(self, font = ("Courier", 12))
            entryValor.grid(column=1, row=i+1, padx = (5,5), pady = (5,5))

            # Colocar el valor inicial si lo hay
            if valores is not None:
                entryValor.insert(0, valores[i])

            # Si el campo es no-editable, deshabilitarlo
            if habilitado is not None and not habilitado[i]:
                entryValor.configure(state = DISABLED)
            
            # Anadir a la lista de elementos
            self._elementos.append(entryValor)

    # GetValue
    # criterio: El criterio cuyo valor se quiere obtener

    def getValue(self, criterio):
        indice = self._criterios.index(criterio)
        return self._elementos[indice].get()

    def crearBotones(self, comando1,comando2):
        aceptar = Button(self, text="Aceptar", font = ("Courier", 12), fg = "black", command=comando1).grid(padx= 50,pady = 20, column = 0, row = len(self._criterios)+1)
        cancelar= Button(self, text="Cancelar", font = ("Courier", 12), fg = "black", command=comando2).grid(pady = 20, column = 1, row = len(self._criterios)+1)

    def getValorEntry():
        return entryValor.get()

    def isfloat(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    