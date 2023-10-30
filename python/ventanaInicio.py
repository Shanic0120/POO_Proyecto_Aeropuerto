from tkinter import *
from tkinter import messagebox
from ventanaPrincipal import VentanaUsuario

class ventanaInicio(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # Configuración parámetros de la ventana
        self.geometry("1000x600")
        self.resizable(False,False)
        self.title("Inicio")
        self.option_add("*tearOff", False)  #Eliminar underline
        self.iconbitmap('./imagenes/icono.ico')
        # Configuración texto hoja de vida desarrolladores
        self.HDV = StringVar()
        # Configuración menú
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion",command=self.descripcion)
        self.menuInicio.add_command(label="Salir")
        self["menu"] = self.menubar

        # Configuración zona frames
        # Se crea las 6 zonas 

        self.P1 = Frame(self, width=500, height=600,bg="#889C9B")
        self.P1.pack(side=LEFT)

        self.P3 = Frame(self.P1, width=500, height=150,bg="#889C9B")
        self.P3.grid(row=0, column=0)

        self.bienvenida = Label(self.P3, text="Bienvenido al sistema de administración de vuelos\n""Hacer click en la imagen para comenzar", 
                        font=("Courier", 10), highlightthickness=2, highlightbackground = "black", highlightcolor= "black")
        self.P4 = Frame(self.P1, width=500, height=450)
        self.P4.grid(row = 1, column = 0)

        self.P2 = Frame(self, width=500, height=600)
        self.P2.pack(side=RIGHT)

        self.P5 = Frame(self.P2, width=500, height=150, bg="#B2BEBF")
        self.P5.grid(row=0, column=0)

        self.botonHDV = Button(self.P5,text='Haga click para conocer a los desarrolladores', command=lambda:self.cambioHDV(0))
        self.botonHDV.place(relx=0.5,rely=0.5,anchor="center")

        self.P6 = Frame(self.P2, width=500, height=450, bg="Gray")
        self.P6.grid(row = 1, column = 0)

        self.bienvenida.place(relx=0.5, rely=0.5, anchor="center")

        # Espacios para poner imagenes de los desarrolladores son 4
        self.F1 = Frame(self.P6, width=250, height=220)
        self.F1.place(x=0, y=0)
        self.F2 = Frame(self.P6, width=250, height=220)
        self.F2.place(x=250, y=0)
        self.F3 = Frame(self.P6, width=250, height=220)
        self.F3.place(x=0, y=225)
        self.F4 = Frame(self.P6, width=250, height=220)
        self.F4.place(x=250, y=225)

        # Lista imagenes de los desarrolladores
        self.desarrolladores = ['./imagenes/cami1.png', './imagenes/cami2.png', './imagenes/cami3.png', './imagenes/cami4.png','./imagenes/camilo1.png','./imagenes/camilo2.png','./imagenes/camilo3.png','./imagenes/camilo4.png','./imagenes/JuanZapata1.png','./imagenes/JuanZapata2.png','./imagenes/JuanZapata3.png','./imagenes/JuanZapata4.png','./imagenes/juandi1.png','./imagenes/juandi2.png','./imagenes/juandi3.png','./imagenes/juandi4.png','./imagenes/sf.png']
        self.posiciones = []

        # Lista imagenes relacionadas al sistema
        self.imaSistema = ['./imagenes/a1.png', './imagenes/a2.png', './imagenes/a3.png','./imagenes/a4.png', './imagenes/a5.png']
        self.sistemaPosicion = []

         # Contadores para poder cambiar las imagenes tanto las de los desarrollares como la del sistema
        self.acumuladorSistema = 0
        self.clicks = 0

        # Recorrido lista de las imagenes de los desarrolladores 
        for i in self.desarrolladores:
            imagen = PhotoImage(file=i)
            self.posiciones.append(imagen)

        self.E1 = Label(self.F1)
        self.E2 = Label(self.F2)
        self.E3 = Label(self.F3)
        self.E4 = Label(self.F4)
        self.E1["image"] = self.posiciones[16]
        self.E1.pack()
        self.E2["image"] = self.posiciones[16]
        self.E2.pack()
        self.E3["image"] = self.posiciones[16]
        self.E3.pack()
        self.E4["image"] = self.posiciones[16]
        self.E4.pack()
        self.contador = 0

        # Recorrido lista fotos sistema para abrir determinada imagen segun la referencia
        for i in self.imaSistema:
            imagen = PhotoImage(file=i)
            self.sistemaPosicion.append(imagen)

        # Configuracion boton apertura de la ventana principal
        self.ventanaSis = Button(self.P4, image=self.sistemaPosicion[0],command=self.abrirVentanaSecundaria)
        self.ventanaSis.pack()
        self.ventanaSis.bind('<Enter>', self.sistema)

    # Genera el texto de la descripcion
    def descripcion(self):
        messagebox.showinfo("Descripcion del sistema", "La principal utilidad de la aplicación de gestión del aeropuerto es la administración de los aspectos principales de esta misma, en donde se guardará la información de los pasajeros, de los vuelos, aviones, empleados y finanzas, también se implementan funcionalidades para la gestión, modificación y adición de estos elementos.")

    # Informacion desarrolladores y asignacion de sus respectivas imagenes atraves del metodo asignar
    def cambioHDV(self,relleno):
        self.clicks += 1
        self.botonHDV.place_forget()
        self.textoHDV = Label(self.P5, textvariable=self.HDV, font = ("Courier", 10), highlightthickness=2, highlightbackground = "black", highlightcolor= "black")
        self.textoHDV.bind('<ButtonPress-1>', self.cambioHDV)
        self.textoHDV.place(x=250, y=75, anchor="center")
        if (self.clicks == 1):
            self.HDV.set("Nombre: Maria Camila Zapata Arrubla \n""Edad: 20 años \n""Programa: Ingenieria de sistemas e informatica\n")
            self.asignar()
        elif (self.clicks == 2):
            self.HDV.set("Nombre: Juan Camilo Molina Roncancio \n""Edad: 20 años \n" "Programa: Ingenieria de sistemas e informatica\n")
            self.asignar()
        elif (self.clicks == 3):
            self.HDV.set("Nombre: Juan Jose Zapata Cadavid \n""Edad: 19 años \n""Programa: Ingenieria de sistemas e informatica\n")
            self.asignar()
        elif (self.clicks == 4):
            self.HDV.set("Nombre: Juan Diego Giraldo Jaramillo \n""Edad: 19 años \n""Programa: Ingenieria de sistemas e informatica\n")
            self.asignar()
            self.clicks = 0

    # Genera el indice de las imagenes segun sea el caso
    def asignar(self):
        #posiciones en el frame p6 son 4 imagenes por lo tanto hay cuatro variables
        d1 = 0
        d2 = 0
        d3 = 0
        d4 = 0
        self.contador += 1
        if self.contador == 1:
            #las 4 primeras imagenes
            d1 = 0 
            d2 = 1     
            d3 = 2 
            d4 = 3 
        elif self.contador == 2:
            d1 = 4  
            d2 = 5  
            d3 = 6 
            d4 = 7  
        elif self.contador == 3:
            d1 = 8  
            d2 = 9 
            d3 = 10  
            d4 = 11  
        elif self.contador == 4:
            d1 = 12  
            d2 = 13 
            d3 = 14 
            d4 = 15 

        # ubica las imagenes en su respectivo espacio
        self.E1.config(image=self.posiciones[d1])
        self.E2.config(image=self.posiciones[d2])
        self.E3.config(image=self.posiciones[d3])
        self.E4.config(image=self.posiciones[d4])

        # se inicializa el contador
        if self.contador == 4:
            self.contador = 0

    # Cambia las imagenes del sistema
    def sistema(self,relleno):
        self.acumuladorSistema += 1
        if self.acumuladorSistema == 5:
            self.acumuladorSistema = 0
        self.ventanaSis.config(image=self.sistemaPosicion[self.acumuladorSistema])

    # Ventana principal
    def abrirVentanaSecundaria(self):
        ventana_inicios.withdraw()
        VentanaUsuario().ventanaInicio = self
            

if __name__ == "__main__":
    ventana_inicios = ventanaInicio()
    ventana_inicios.mainloop()