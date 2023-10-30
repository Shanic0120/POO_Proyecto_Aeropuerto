from tkinter import *
from tkinter import messagebox, Menu, ttk
from tkinter.font import Font

import tkinter as tk

from fieldFrame import FieldFrame

from datetime import datetime

from gestorAplicacion.gestorVuelos.aeropuerto import Aeropuerto
from gestorAplicacion.gestorVuelos.asiento import Asiento
from gestorAplicacion.gestorVuelos.equipaje import Equipaje
from gestorAplicacion.gestorVuelos.vuelo import Vuelo
from gestorAplicacion.gestorVuelos.avion import Avion

from gestorAplicacion.gestorHumana.cargos import Cargos
from gestorAplicacion.gestorHumana.empleado import Empleado
from gestorAplicacion.gestorHumana.pasajero import Pasajero
from gestorAplicacion.gestorHumana.persona import Persona

from baseDatos.deserializador import deserializar
from baseDatos.serializador import serializar

from excepciones.excepcionTipo import *
from excepciones.excepcionImposibilidades import *

class VentanaUsuario(Tk):
    VSabierta = False

    def __init__(self):
        super().__init__()
        self.title("Sistema de administracion de aeropuertos")
        self.option_add("*tearOff", False)
        self.geometry("1280x720")
        self.ventanaInicio = None
        self.resizable(0, 0)
        self.iconbitmap('./imagenes/icono.ico')
        self.widgetsActuales = []
        self.aeropuerto = Aeropuerto()
        Persona.setAeropuerto(self.aeropuerto)
        Avion.setAeropuerto(self.aeropuerto)
        Vuelo.setAeropuerto(self.aeropuerto)
        #self.valoresIniciales()
        deserializar(self.aeropuerto)

        # Funciones
        def prueba():
            pass

        self.bind('<Destroy>', lambda x: serializar(self.aeropuerto))

        def descripcion():
            messagebox.showinfo("Descripcion del sistema",
                                "La principal utilidad de la aplicación de gestión del aeropuerto es la administración de los aspectos principales de esta misma, en donde se guardará la información de los pasajeros, de los vuelos, aviones, empleados y finanzas, también se implementan funcionalidades para la gestión, modificación y adición de estos elementos.")

        def info():
            messagebox.showinfo("Desarrolladores del aplicativo",
                                "Maria Camila Zapata Arrubla\nJuan Camilo Molina Roncancio\nJuan Jose Zapata Cadavid\nJuan Diego Giraldo Jaramillo")

        def borrarElementos():
            for i in self.widgetsActuales:
                i.destroy()
            self.widgetsActuales = []
            try:
                del self.formulario
            except:
                pass

        # Pantallas
        def pantallaPrincipal():
            borrarElementos()
            self.lp = Label(self.fp, text="Pantalla principal", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd, text="Descripción de funcionalidades", font=("Courier", 10))
            self.ld.pack()
            descripcion = '''Bienvenidos a la aplicacion de gestion y modificacion de aeropuerto, aqui podra realizar diferentes funciones
            relacionadas a la administracion del aeropuerto.

             En la parte superior en el menu de procesos y consultas se listan Las principales funcionalidades, las cuales son:


            1. Reserva de vuelo
            En esta opcion esta disponible lo necesario para agendar un vuelo a determinado pasajero, se muestran en pantalla
            todos los vuelos disponibles que se dirijan hacia la ciudad de destino deseada, luego se muestran los diferentes
            vuelos disponibles. En el mismo apartado se implementa un pequeño formulario de datos personales para la
            identificación del pasajero y así mismo la cantidad de equipajes que desea transportar. Tambien se le da la
            posibilidad de elegir el asiento que desea, los cuales están separados por turista, ejecutiva y primera clase, 
            esta elección influirá directamente en el costo del tiquete.
        

            2. Programar vuelos
            Esta funcionalidad permite programar nuevos vuelos que se llevarán a cabo en el aeropuerto, para posteriormente
            interactuar con ellos mediante otras funcionalidades, además de que implementa un sistema de recomendación de
            empleados asignados al vuelo seguidamente de su creación, basándose en la experiencia del empleado.


            3. Gestionar empleados
            Esta funcionalidad imprime los múltiples empleados que trabajan en el aeropuerto, junto a su cédula para poder 
            seleccionarlo y elegir entre opciones como cambiar de cargo, cambiar sueldo, asignar un vuelo y despedir empleados.
            

            4. Informacion sobre finanzas
            Esta funcionalidad muestra el saldo actual del aeropuerto y reúne las siguientes opciones, pagar nomina, consultar
            el historial de transacciones, contratar nuevos empleados e ingresar fondos al aeropuerto.


            5. Modificaciones generales
            Esta funcionalidad agrupa ciertas modificaciones posibles en dentro del sistema tales como cambiar de asiento de un
            pasajero, cancelar un vuelo, eliminar un avion e ingresar nuevos aviones al aeropuerto.
            '''

            self.label = Label(self.ventanaOpera, text=descripcion, font=("Courier", 10))
            self.label.pack(ipadx=8, padx=8, ipady=8, pady=8, fill=X, anchor="w")
            self.widgetsActuales.extend([self.lp, self.ld, self.label])

        def pantallaReservaDeVuelo():
            borrarElementos()
            self.lp = Label(self.fp, text="Reserva de vuelo", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd,
                            text="En este apartado puede realizar el agendamiento de un vuelo para un pasajero",
                            font=("Courier", 10))
            self.ld.pack()

            self.destino = Label(self.ventanaOpera, text="Ingrese el destino deseado", font=("Courier", 10))
            self.destino.grid(ipadx=8, padx=8, ipady=8, pady=8, row=0, column=0)

            destinos = []
            for vuelo in self.aeropuerto.getVuelos():
                destino = vuelo.getDestino()
                if destino not in destinos: destinos.append(destino)

            self.listaDestinos = ttk.Combobox(self.ventanaOpera, values=destinos, textvariable=StringVar(value=""), state="readonly")
            self.listaDestinos.grid(ipadx=8, padx=8, row=0, column=1, columnspan=10, sticky="w")
            self.vuelo = Label(self.ventanaOpera, text = "Vuelos al destino seleccionado", font = ("Courier", 10))
            self.vuelo.grid(ipadx=8, padx=8, ipady=8, pady=8, row=1, column=0)

            self.listaVuelos = ttk.Combobox(self.ventanaOpera, values=[], textvariable=StringVar(value=""), state="readonly", width=50)
            self.listaVuelos.grid(ipadx=8, padx=8, row=1, column=1, sticky="w")

            def seleccionDestino(Event):
                sel = self.listaDestinos.get()
                vuelos = []
                for vuelo in self.aeropuerto.getVuelos():
                    v = "ID: "+str(vuelo.getId())+" - Precio: "+str(vuelo.getCosto())+" - Fecha: "+str(vuelo.getFecha())
                    if vuelo not in vuelos and vuelo.getDestino()==sel:
                        vuelos.append(v)
                self.listaVuelos.config(textvariable=StringVar(value=""))
                self.listaVuelos.config(values=vuelos)

            self.listaDestinos.bind("<<ComboboxSelected>>", seleccionDestino)

            def seleccionVuelo(Event):
                sel1 = self.listaVuelos.get().split(" - ")[0][4:]
                for vuelo in self.aeropuerto.getVuelos():
                    if vuelo.getId() == int(sel1):
                        global vueloActual 
                        vueloActual = vuelo
                        asientos = []
                        for asiento in vuelo.getAvion().getAsientos():
                            a = "Numero: "+str(asiento.getNumero())+" - Clase: "+str(asiento.getClase())
                            if not asiento.isOcupado(): asientos.append(a)
                        self.listaAsientos.config(textvariable=StringVar(value=""))
                        self.listaAsientos.config(values=asientos)
                    break
                    
            self.listaVuelos.bind("<<ComboboxSelected>>", seleccionVuelo)

            self.form = Label(self.ventanaOpera, text="Formulario", font=("Courier", 10))
            self.form.grid(ipadx=8, padx=8, row=2, column=0)
            self.formulario = FieldFrame(self.ventanaOpera, "Datos personales", ["Nombre","Documento", "Edad", "Genero", "Equipajes", "Peso total"], None, None, None, pack=False)
            self.formulario.grid(ipadx=8, padx=8, row=2, column=1, sticky="w")

            self.asiento = Label(self.ventanaOpera, text="Asientos disponibles", font=("Courier", 10))
            self.asiento.grid(ipadx=8, padx=8, ipady=8, pady=8, row=3, column=0)

            self.listaAsientos = ttk.Combobox(self.ventanaOpera, values=[], textvariable=StringVar(value=""), state="readonly", width=50)
            self.listaAsientos.grid(ipadx=8, padx=8, row=3, column=1, sticky="w")

            def reserva():
                try:
                    NuevoPasajero = Pasajero(self.formulario.getValue("Nombre"), self.formulario.getValue("Documento"), 
                                            self.formulario.getValue("Edad"),self.formulario.getValue("Genero"))

                    NuevoPasajero.addEquipaje(Equipaje(int(self.formulario.getValue("Peso total"))))
                    vueloActual.agregarPasajero(NuevoPasajero, int(self.listaAsientos.get().split(" - ")[0][7:]))
                    self.asiento = Label(self.ventanaOpera, text="El vuelo ha sido registrado\n exitosamente!", font=("Courier", 20))
                    self.asiento.grid(ipadx=8, padx=8, ipady=8, pady=8, row=2, column=2)
                except:
                    messagebox.showwarning(title="Advertencia", message=f"Por favor rellene todos los apartados.")

            self.ingresar = Button(self.ventanaOpera, text="Reservar vuelo", command=reserva)
            self.ingresar.grid(ipadx=8, padx=8, ipady=8, pady=8, row=4, column=0, columnspan=2)

            self.widgetsActuales.extend([self.lp, self.ld, self.destino, self.listaDestinos,self.form, self.vuelo, self.listaVuelos, self.formulario, self.asiento, self.listaAsientos, self.ingresar])

        def pantallaEmpleados():
            def limpiarFrame():
                for widget in self.of.winfo_children():
                    widget.destroy()

            def nuevoEmpleado():
                limpiarFrame()

                def checkbox_clicked():
                    try:
                        ExcepcionVacio.valorVacio(self.cc.get())
                        if self.suevalue.get():
                            self.suee.delete(0, tk.END)
                            self.suee.insert(0, Cargos.buscarCargo(self.cc.get()).getSueldoBase())
                            self.cc.config(state='disable')
                            self.suee.config(state='disabled')
                        else:
                            self.cc.config(state='normal')
                            self.suee.config(state='normal')
                            self.suee.delete(0, tk.END)
                    except:
                        fallo = True
                        self.suevalue.set(False)
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Cargo está vacía, por favor completarla.")
                    

                def ingresarNuevoEmpleado():
                    fallo = False
                    try:
                        ExcepcionString.tipoString(self.ne.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada {self.ne.get()} contiene al menos un número, debería ser completamente texto, por favor modificar.")

                    try:
                        ExcepcionEntero.tipoInt(self.ee.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada {self.ee.get()} debe ser un número, por favor modificar.")

                    try:
                        ExcepcionEntero.tipoInt(self.cce.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada {self.cce.get()} debe ser un número, por favor modificar.")

                    try:
                        ExcepcionEntero.tipoInt(self.suee.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada {self.suee.get()} debe ser un número, por favor modificar.")

                    try:
                        ExcepcionVacio.valorVacio(self.ne.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Nombre está vacía, por favor completarla.")

                    try:
                        ExcepcionVacio.valorVacio(self.ee.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Edad está vacía, por favor completarla.")

                    try:
                        ExcepcionVacio.valorVacio(self.cce.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Cedula está vacía, por favor completarla.")

                    try:
                        ExcepcionVacio.valorVacio(self.cc.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Cargo está vacía, por favor completarla.")

                    try:
                        ExcepcionVacio.valorVacio(self.sc.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Sexo está vacía, por favor completarla.")

                    try:
                        ExcepcionVacio.valorVacio(self.suee.get())
                    except:
                        fallo = True
                        messagebox.showwarning(title="Advertencia",
                                               message=f"La entrada Sueldo está vacía, por favor completarla.")

                    if not fallo:
                        e = Empleado(self.ne.get(), int(self.cce.get()), int(self.ee.get()), self.sc.get(),
                                     int(self.suee.get()), self.cc.get())
                        self.lb.insert(tk.END, "Cedula: " + str(e.getCedula()) + " " * (
                                    15 - len(str(e.getCedula()))) + "Nombre: " + e.getNombre())
                        self.lb.selection_set(tk.END)
                        verDatos()

                self.tl = Label(self.of, text="Ingrese los datos del nuevo empleado",
                                font=Font(family='Courier', size=100))
                self.tl.grid(row=0, column=0, padx=0, pady=5, sticky="w", columnspan=2)

                self.nl = Label(self.of, text="Nombre:", font=Font(family='Courier', size=100))
                self.nl.grid(row=1, column=0, padx=0, pady=5, sticky="w")
                self.ne = Entry(self.of, width=20)
                self.ne.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")

                self.el = Label(self.of, text="Edad:", font=Font(family='Courier', size=100))
                self.el.grid(row=2, column=0, padx=0, pady=5, sticky="w")
                self.ee = Entry(self.of, width=20)
                self.ee.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")

                self.ccl = Label(self.of, text="Cedula:", font=Font(family='Courier', size=100))
                self.ccl.grid(row=3, column=0, padx=0, pady=5, sticky="w")
                self.cce = Entry(self.of, width=20)
                self.cce.grid(row=3, column=1, padx=0, pady=5, sticky="nsew")

                self.cl = Label(self.of, text="Cargo:", font=Font(family='Courier', size=100))
                self.cl.grid(row=4, column=0, padx=0, pady=5, sticky="w")
                self.cc = ttk.Combobox(self.of, state="readonly", values=Cargos.getTodosLosCargos(), width=20)
                self.cc.grid(row=4, column=1, padx=0, pady=5, sticky="nsew")

                self.sl = Label(self.of, text="Sexo:", font=Font(family='Courier', size=100))
                self.sl.grid(row=5, column=0, padx=0, pady=5, sticky="w")
                self.sc = ttk.Combobox(self.of, state="readonly", values=["M", "F"], width=20)
                self.sc.grid(row=5, column=1, padx=0, pady=5, sticky="nsew")

                self.suevalue = BooleanVar(self.of)
                self.suel = Label(self.of, text="Sueldo:", font=Font(family='Courier', size=100))
                self.suel.grid(row=6, column=0, padx=0, pady=5, sticky="w")
                self.suee = Entry(self.of, width=20)
                self.suee.grid(row=6, column=1, padx=0, pady=5, sticky="nsew")
                self.suec = ttk.Checkbutton(self.of, text="Asignar valor predeterminado por el cargo",
                                            variable=self.suevalue, command=checkbox_clicked)
                self.suec.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")

                self.ingresar = Button(self.of, text="Ingresar nuevo empleado", command=ingresarNuevoEmpleado)
                self.ingresar.grid(row=7, column=0, padx=0, pady=5, sticky="nsew", columnspan=3)

            def verDatos():
                limpiarFrame()
                if len(self.lb.curselection()) != 0:

                    empleado = self.aeropuerto.buscarEmpleado(int(self.lb.get(self.lb.curselection()[0]).split()[1]))

                    self.nl = Label(self.of, text=empleado.getNombre() + ", " + str(empleado.getEdad()) + " años",
                                    font=Font(family='Courier', size=60))
                    self.nl.grid(row=0, column=0, padx=5, pady=5, sticky="w")

                    self.cl = Label(self.of, text="Numero de cedula: " + str(empleado.getCedula()),
                                    font=Font(family='Courier', size=35))
                    self.cl.grid(row=1, column=0, padx=5, pady=5, sticky="w")

                    self.sl = Label(self.of, text="Sueldo actual: " + str(empleado.getSueldo()),
                                    font=Font(family='Courier', size=35))
                    self.sl.grid(row=2, column=0, padx=5, pady=5, sticky="w")

                    self.carl = Label(self.of, text="Cargo: " + str(empleado.getCargo()),
                                      font=Font(family='Courier', size=35))
                    self.carl.grid(row=3, column=0, padx=5, pady=5, sticky="w")

                    try:
                        self.v1l = Label(self.of,
                                         text="Destino del vuelo asignado: " + str(empleado.getVuelo().getDestino()),
                                         font=Font(family='Courier', size=35))
                        self.v2l = Label(self.of, text="Fecha: " + str(empleado.getVuelo().getFecha()),
                                         font=Font(family='Courier', size=35))
                        self.v2l.grid(row=5, column=1, padx=5, pady=5, sticky="w")

                        self.val = Label(self.of,
                                         text="Avión del vuelo: " + str(empleado.getVuelo().getAvion().getModelo()),
                                         font=Font(family='Courier', size=35))
                        self.val.grid(row=6, column=0, padx=5, pady=5, sticky="w")

                        self.vpal = Label(self.of,
                                          text="Peso actual: " + str(empleado.getVuelo().getPesoActual()) + "/" + str(
                                              empleado.getVuelo().getAvion().getPesoMaximo()),
                                          font=Font(family='Courier', size=35))
                        self.vpal.grid(row=7, column=0, padx=5, pady=5, sticky="w")
                    except:
                        self.v1l = Label(self.of, text="Este empleado aún no tiene un vuelo asignado",
                                         font=Font(family='Courier', size=35))
                    self.v1l.grid(row=5, column=0, padx=5, pady=5, sticky="w")

            def cambiarSaldo():
                limpiarFrame()

                def cambioValor(op):
                    if op == "+":
                        val=empleado.getSueldo() + 100
                        try:
                            ExcepcionValorMaximo.menorQue(val,3000)
                            empleado.setSueldo(val)
                        except:
                            messagebox.showwarning("Valor incorrecto",message="El sueldo no puede ser mayor que 4000")
                    elif op == "-":
                        val=empleado.getSueldo() - 100
                        try:
                            ExcepcionPositivo.valorPositivo(val)
                            empleado.setSueldo(val)
                        except:
                            messagebox.showwarning("Valor incorrecto",message="El sueldo no puede ser menor que 0")
                    self.sueldo["text"] = empleado.getSueldo()

                if len(self.lb.curselection()) != 0:
                    empleado = self.aeropuerto.buscarEmpleado(int(self.lb.get(self.lb.curselection()[0]).split()[1]))

                    self.sl = Label(self.of,
                                    text="El sueldo de " + empleado.getNombre() + ", que es " + empleado.getCargo() + " actualmente es de: ")
                    self.sl.grid(row=0, column=0, sticky="nsew", columnspan=3)

                    self.sueldo = Label(self.of, text=empleado.getSueldo(), font=Font(family="Courier", size=80))
                    self.sueldo.grid(row=1, column=1, sticky="w", columnspan=2)

                    self.restab = Button(self.of, text="-", command=lambda: cambioValor("-"))
                    self.restab.grid(row=1, column=0, sticky="nsew")
                    self.sumab = Button(self.of, text="+", command=lambda: cambioValor("+"))
                    self.sumab.grid(row=1, column=2, sticky="nsew")

                    r=0
                    for i in Cargos:
                        Label(self.of,text=i.getCargo()+": "+str(i.getSueldoBase())).grid(row=r,column=3, sticky="w",padx=15)
                        r=r+1

            def despedir():
                limpiarFrame()
                if len(self.lb.curselection()) != 0:
                    curr = self.lb.curselection()[0]
                    empleado = self.aeropuerto.buscarEmpleado(int(self.lb.get(curr).split()[1]))
                    desp = messagebox.askyesno(
                        message="¿Está seguro que desea despedir a " + empleado.getNombre() + "?", title="Despedir")
                    if desp:
                        self.aeropuerto.despedirEmpleado(empleado)
                        self.lb.delete(curr)

            def cambiarCargo():
                limpiarFrame()

                def cambio():
                    if len(self.cargos.curselection()) != 0:
                        empleado.setCargo(self.cargos.get(self.cargos.curselection()[0]))
                        self.lb.selection_set(curr)
                        cambiarCargo()

                if len(self.lb.curselection()) != 0:
                    curr = self.lb.curselection()[0]
                    empleado = self.aeropuerto.buscarEmpleado(int(self.lb.get(self.lb.curselection()[0]).split()[1]))
                    self.carg = Label(self.of, text="El cargo actual de " + empleado.getNombre() + " es " + str(
                        empleado.getCargo()))
                    self.carg.grid(row=0, column=0, sticky="nsew")

                    self.cargos = Listbox(self.of, font='Courier', width=40, height=4)
                    self.cargos.grid(row=1, column=0, sticky="n")

                    for i in Cargos.getTodosLosCargos():
                        if i != empleado.getCargo():
                            self.cargos.insert(tk.END, i)

                    self.cambiar = Button(self.of, text="Cambiar cargo", command=cambio)
                    self.cambiar.grid(row=1, column=1, rowspan=2, padx=15)

            def cambiarVuelo():
                limpiarFrame()
                if len(self.lb.curselection()) != 0:
                    curr = self.lb.curselection()[0]
                    empleado = self.aeropuerto.buscarEmpleado(int(self.lb.get(self.lb.curselection()[0]).split()[1]))
                    try:
                        self.carg = Label(self.of, text="El vuelo actual de " + empleado.getNombre() + " es:")
                        self.vuelo = Label(self.of,
                                           text="Sala " + empleado.getVuelo().getSalaEmbarque() + " - Destino: " + empleado.getVuelo().getDestino() + " - Avión: " + empleado.getVuelo().getAvion().getModelo())
                        self.vuelo.grid(row=1, column=0)
                    except:
                        self.carg = Label(self.of, text="Este empleado aún no tiene un vuelo asignado")

                    self.carg.grid(row=0, column=0, sticky="nsew")

                    self.scroll2 = Scrollbar(self.of, orient='vertical')

                    self.vuelos = Listbox(self.of, yscrollcommand=self.scroll2.set, font='Courier', width=40, height=20)
                    self.vuelos.grid(row=2, column=0, columnspan=4, sticky="snew", padx=5, pady=5)

                    self.scroll2.configure(command=self.vuelos.yview)
                    self.scroll2.grid(column=4, row=2, sticky='NS')

                    for i in self.aeropuerto.getVuelos():
                        if i != empleado.getVuelo():
                            self.vuelos.insert(tk.END,
                                               i.getSalaEmbarque() + " - " + i.getAvion().getModelo() + " - " + i.getDestino())

                    def cambiar():
                        try:
                            if self.vuelos.curselection() != 0:
                                lista = self.vuelos.get(self.vuelos.curselection()[0]).split(" - ")
                                vuelo = self.aeropuerto.buscarVuelo(lista[0], lista[1], lista[2])
                                empleado.setVuelo(vuelo)
                                self.lb.selection_set(curr)
                                cambiarVuelo()
                        except:
                            messagebox.showwarning("Sin selección","No seleccionaste ningún vuelo, vuelva a intentarlo.")

                    def borrarVuelo():
                        if empleado.getVuelo()!= None:
                            empleado.getVuelo().getEmpleados().remove(empleado)
                        empleado.setVuelo(None)
                        self.lb.selection_set(curr)
                        cambiarVuelo()
                    self.cambiar = Button(self.of, text="Cambiar vuelo", command=cambiar)
                    self.cambiar.grid(column=0, row=3, columnspan=4, sticky="nsew")

                    self.borrar = Button(self.of, text="Borrar vuelo", command=borrarVuelo)
                    self.borrar.grid(column=0, row=4, columnspan=4, sticky="nsew")

            borrarElementos()
            self.lp = Label(self.fp, text="Gestor de empleados", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd,
                            text="En este apartado puede visualizar los datos de los empleados y gestionar los mismos",
                            font=("Courier", 10))
            self.ld.pack()

            self.scroll = Scrollbar(self.ventanaOpera, orient='vertical')

            self.lb = Listbox(self.ventanaOpera, yscrollcommand=self.scroll.set, font='Courier', width=40, height=20)
            self.lb.grid(row=0, column=0, columnspan=4, sticky="snew", padx=5, pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=4, row=0, sticky='NS')

            for i in self.aeropuerto.getEmpleados():
                self.lb.insert(tk.END, "Cedula: " + str(i.getCedula()) + " " * (
                            15 - len(str(i.getCedula()))) + "Nombre: " + i.getNombre())

            self.of = Frame(self.ventanaOpera)
            self.of.grid(row=0, column=5, rowspan=4, sticky='nsew', padx=30, pady=30)

            self.datosButton = Button(self.ventanaOpera, text="Ver datos", command=verDatos)
            self.datosButton.grid(row=1, columnspan=4, padx=5, pady=5, sticky="nsew")
            self.nuevoEmpleadoButton = Button(self.ventanaOpera, text="Crear nuevo empleado", command=nuevoEmpleado)
            self.nuevoEmpleadoButton.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
            self.cambiarSaldo = Button(self.ventanaOpera, text="Cambiar saldo", command=cambiarSaldo)
            self.cambiarSaldo.grid(row=2, column=2, padx=5, pady=5, sticky="nsew", columnspan=2)
            self.cambiarCargo = Button(self.ventanaOpera, text="Cambiar cargo", command=cambiarCargo)
            self.cambiarCargo.grid(row=3, column=2, padx=5, pady=5, sticky="nsew", columnspan=2)
            self.cambiarVuelo = Button(self.ventanaOpera, text="Cambiar vuelo", command=cambiarVuelo)
            self.cambiarVuelo.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
            self.despedir = Button(self.ventanaOpera, text="Despedir", command=despedir)
            self.despedir.grid(row=4, column=0, padx=5, pady=5, sticky="nsew", columnspan=4)

            self.widgetsActuales.extend(
                [self.lp, self.despedir, self.cambiarVuelo, self.cambiarCargo, self.datosButton, self.ld, self.lb,
                 self.scroll, self.of, self.cambiarSaldo, self.nuevoEmpleadoButton])

        def pantallaCambiarAsiento():
            borrarElementos()
            def limpiarFrame():
                for widget in self.of.winfo_children():
                    widget.destroy()
            self.lp = Label(self.fp,text= "Cambiar silla", font = ("Courier", 12),height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd, text = "En este apartado puede realizar el cambio de silla a un determinado pasajero", font = ("Courier", 10))
            self.ld.pack()            

            self.scroll=Scrollbar(self.ventanaOpera,orient='vertical')           

            self.lb=Listbox(self.ventanaOpera,yscrollcommand=self.scroll.set,font='Courier',width=40,height=20)
            self.lb.grid(row=0,column=0,columnspan=4,sticky="snew",padx=5,pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=4, row=0, sticky='NS')    

            for i in self.aeropuerto.getPasajeros():
                self.lb.insert(tk.END,"Cedula: "+str(i.getCedula())+" "*(15-len(str(i.getCedula()))) +"Nombre: "+i.getNombre())

            self.of=Frame(self.ventanaOpera)
            self.of.grid(row=0,column=5,rowspan=4,sticky='nsew',padx=30,pady=30)

            def verDatos():
                limpiarFrame()
                global pasajero
                if len(self.lb.curselection())!=0:

                    pasajero=self.aeropuerto.buscarPasajero(int(self.lb.get(self.lb.curselection()[0]).split()[1]))

                    self.cl=Label(self.of,text="Numero de cedula: "+str(pasajero.getCedula()),font=Font(family='Courier',size=35))
                    self.cl.grid(row=1,column=0,padx=5,pady=5,sticky="w")

                    self.sl=Label(self.of,text="Silla actual: "+str(pasajero.getAsiento().getNumero()),font=Font(family='Courier',size=35))
                    self.sl.grid(row=2,column=0,padx=5,pady=5,sticky="w")

                    self.clasel=Label(self.of,text="Clase: "+str(pasajero.getAsiento().getClase()),font=Font(family='Courier',size=35))
                    self.clasel.grid(row=3,column=0,padx=5,pady=5,sticky="w")

                    self.vl=Label(self.of,text="Destino: "+str(pasajero.getVuelo().getDestino()),font=Font(family='Courier',size=35))
                    self.vl.grid(row=4,column=0,padx=5,pady=5,sticky="w")

                    self.sala=Label(self.of,text="Sala de embarque: "+str(pasajero.getVuelo().getSalaEmbarque()),font=Font(family='Courier',size=35))
                    self.sala.grid(row=5,column=0,padx=5,pady=5,sticky="w")

                    self.costol=Label(self.of,text="Costo: "+str(pasajero.getInversion()),font=Font(family='Courier',size=35))
                    self.costol.grid(row=6,column=0,padx=5,pady=5,sticky="w")

            def verAsientos():
                limpiarFrame()
                self.scrollpa=Scrollbar(self.ventanaOpera,orient='vertical')           

                self.lp=Listbox(self.ventanaOpera,yscrollcommand=self.scroll.set,font='Courier',width=40,height=20)
                self.lp.grid(row=0,column=0,columnspan=4,sticky="snew",padx=5,pady=5)

                self.scrollpa.configure(command=self.lb.yview)         
                self.scrollpa.grid(column=4, row=0, sticky='NS')    

                for i in pasajero.getVuelo().getAvion().getAsientos():
                    self.lp.insert(tk.END,"Número: "+str(i.getNumero())+" "*(10-len(str(i.getNumero()))) +"Clase: "+i.getClase())

                self.ofp=Frame(self.ventanaOpera)
                self.ofp.grid(row=0,column=5,rowspan=4,sticky='nsew',padx=30,pady=30)

                def cambiar():
                    valorInicial = pasajero.getInversion()
                    if len(self.lp.curselection())!=0:
                        asiento=pasajero.getVuelo().getAvion().buscarAsiento(int(self.lp.get(self.lp.curselection()[0]).split()[1]))
        
                        pasajero.setAsiento(asiento)

                        if asiento.getClase() == "Primera clase":
                            pasajero.setInversion(3*pasajero.getVuelo().getCosto())
                        elif asiento.getClase() == "Ejecutiva":
                            pasajero.setInversion(2*pasajero.getVuelo().getCosto())
                        else:
                            pasajero.setInversion(pasajero.getVuelo().getCosto())

                        self.tiquete=Label(self.ofp,text=pasajero.getVuelo().tiquete(pasajero),font=Font(family='Courier',size=20))
                        self.tiquete.grid(row=3,column=9,padx=5,pady=5,sticky="w")

                        if valorInicial < pasajero.getInversion():
                            self.ex=Label(self.ofp,text="Por favor pagar un excedente de: "+str(pasajero.getInversion()- valorInicial),font=Font(family='Courier',size=35))
                            self.ex.grid(row=8,column=9,padx=5,pady=5,sticky="w")
                            self.aeropuerto.transaccion("Excedente cambio de asiento",pasajero.getInversion()-valorInicial)
                        else:
                            self.de=Label(self.ofp,text="Devolución: $ "+str(valorInicial - pasajero.getInversion()),font=Font(family='Courier',size=35))
                            self.de.grid(row=8,column=9,padx=5,pady=5,sticky="w")
                            self.aeropuerto.transaccion("Devolución cambio de asiento",valorInicial-pasajero.getInversion())

                        self.widgetsActuales.extend([self.tiquete])

                self.cambiarButton = Button(self.ventanaOpera,text="Cambiar",command=cambiar)
                self.cambiarButton.grid(row=1,column=3,padx=5,pady=5)
                self.widgetsActuales.extend([self.lp,self.scrollpa,self.ofp,self.cambiarButton])


            self.datosButton=Button(self.ventanaOpera,text="Ver datos",command=verDatos)
            self.datosButton.grid(row=1,padx=5,pady=5)

            self.asientosDisponibles=Button(self.ventanaOpera,text="Asientos disponibles",command=verAsientos)
            self.asientosDisponibles.grid(row=1,column=2,padx=5,pady=5)

            self.widgetsActuales.extend([self.lp,self.ld,self.lb,self.scroll,self.of,self.datosButton,self.asientosDisponibles])

        def pantallaCancelarVuelo():
            borrarElementos()
            def limpiarFrame():
                for widget in self.of.winfo_children():
                    widget.destroy()
            self.lp = Label(self.fp, text="Cancelar vuelo", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd, text="En este apartado puede cancelar un determinado vuelo", font=("Courier", 10))
            self.ld.pack()

            self.scroll = Scrollbar(self.ventanaOpera, orient='vertical')

            self.lb = Listbox(self.ventanaOpera, yscrollcommand=self.scroll.set, font='Courier', width=20, height=20)
            self.lb.grid(row=0, column=0, columnspan=4, sticky="snew", padx=5, pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=4, row=0, sticky='NS')

            for i in self.aeropuerto.getVuelos():
                self.lb.insert(tk.END, "Destino: " + str(i.getDestino()))

            self.of = Frame(self.ventanaOpera)
            self.of.grid(row=0, column=5, rowspan=4, sticky='nsew', padx=30, pady=30)

            def cancelar():
                limpiarFrame()
                if len(self.lb.curselection()) != 0:
                    curr = self.lb.curselection()[0]
                    vuelo = self.aeropuerto.buscarVuelo(self.aeropuerto.getVuelos()[curr].getSalaEmbarque(),self.aeropuerto.getVuelos()[curr].getAvion().getModelo(),self.lb.get(curr).split()[1])
                    desp = messagebox.askyesno(
                        message="¿Está seguro que desea cancelar el " + vuelo.getDestino() + "?", title="Cancelar")
                    if desp:
                        for pasa in self.aeropuerto.getVuelos()[curr].getPasajeros():
                            self.aeropuerto.eliminarPasajero(self.aeropuerto.buscarPasajero(pasa.getCedula()))
                        self.aeropuerto.getVuelos()[curr].getPasajeros().clear()
                        self.aeropuerto.cancelarVuelo(vuelo)
                        self.lb.delete(curr)

            self.cancelar = Button(self.ventanaOpera, text="Cancelar", command=cancelar)
            self.cancelar.grid(row=4, column=0, padx=5, pady=5, sticky="nsew", columnspan=4)

            self.widgetsActuales.extend([self.lp, self.ld, self.lb, self.scroll, self.of,self.cancelar])

        def pantallaEliminarAvion():
            borrarElementos()
            def limpiarFrame():
                for widget in self.of.winfo_children():
                    widget.destroy()
            self.lp = Label(self.fp, text="Eliminar avión", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd, text="En este apartado puede eliminar un avión con la referencia del modelo.",
                            font=("Courier", 10))
            self.ld.pack()

            self.scroll = Scrollbar(self.ventanaOpera, orient='vertical')

            self.lb = Listbox(self.ventanaOpera, yscrollcommand=self.scroll.set, font='Courier', width=20, height=20)
            self.lb.grid(row=0, column=0, columnspan=4, sticky="snew", padx=5, pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=4, row=0, sticky='NS')

            for i in self.aeropuerto.getAviones():
                self.lb.insert(tk.END, "Modelo: " + str(i.getModelo()))

            self.of = Frame(self.ventanaOpera)
            self.of.grid(row=0, column=5, rowspan=4, sticky='nsew', padx=30, pady=30)

            def cancelar():
                limpiarFrame()
                vuelo = None
                if len(self.lb.curselection()) != 0:
                    curr = self.lb.curselection()[0]
                    avion = self.aeropuerto.buscarAvion(self.aeropuerto.getAviones()[curr].getModelo())
                    for i in self.aeropuerto.getVuelos():
                        if i.getAvion().getModelo() ==  self.aeropuerto.getAviones()[curr].getModelo():
                            vuelo = i
                    #vuelo = self.aeropuerto.buscarVuelo(self.aeropuerto.getVuelos()[curr].getSalaEmbarque(),self.aeropuerto.getVuelos()[curr].getAvion().getModelo(),self.aeropuerto.getVuelos()[curr].getDestino())

                    desp = messagebox.askyesno(
                        message="¿Está seguro que desea retirar el " + self.aeropuerto.getAviones()[curr].getModelo() + "?", title="Cancelar")
                    if desp:
                        antesAvion = self.aeropuerto.getAviones()[curr].getModelo()
                        self.aeropuerto.cancelarAvion(avion)
                        self.lb.delete(curr)

                        if vuelo.getAvion().getModelo()== antesAvion:
                            pVuelo = messagebox.askyesno(
                                    message="¿Desea agregar un avion al vuelo " + vuelo.getDestino() + "?", title="Cancelar")
                            if pVuelo:
                                pantallaEliminarAvion()
                                
                                self.tl = Label(self.of, text="Ingrese los datos del nuevo avion",
                                                font=Font(family='Courier', size=100))
                                self.tl.grid(row=0, column=0, padx=0, pady=5, sticky="w", columnspan=2)
                    
                                def check():
                                    if self.suevalue.get():
                                        self.suee.delete(0, tk.END)
                                        self.suee.insert(0, 20)
                                        self.suee.config(state='disabled')
                                    else:
                                        self.suee.config(state='normal')
                                        self.suee.delete(0, tk.END)
                                
                                def ingreso():
                                    fallo = False
                                    try:
                                        ExcepcionVacio.valorVacio(self.modelo_entry.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada Modelo está vacía, por favor completar.")
                    
                                    try:
                                        ExcepcionVacio.valorVacio(self.pesomax_entry.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada Peso Max está vacía, por favor completar.")
                                    
                                    try:
                                        ExcepcionVacio.valorVacio(self.valor_entry.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada Valor está vacía, por favor completar.")
                                    
                                    try:
                                        ExcepcionVacio.valorVacio(self.suee.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada Asientos está vacía, por favor completar.")
                    
                                    try:
                                        ExcepcionEntero.tipoInt(self.pesomax_entry.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada {self.pesomax_entry.get()} debe ser un número, por favor modificar.")
                    
                                    try:
                                        ExcepcionEntero.tipoInt(self.valor_entry.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada {self.valor_entry.get()} debe ser un número, por favor modificar.")
                    
                                    try:
                                        ExcepcionEntero.tipoInt(self.suee.get())
                                    except:
                                        fallo = True
                                        messagebox.showwarning(title="Advertencia",
                                                            message=f"La entrada {self.suee.get()} debe ser un número, por favor modificar.")
                                    
                                    if not fallo:
                                        avion = Avion(self.modelo_entry.get(),int(self.pesomax_entry.get()),int(self.valor_entry.get()),int(self.suee.get()))
                                        vuelo.setAvion(avion)
                                        self.aeropuerto.transaccion(f"Compra de {avion.getModelo()}",-avion.getValor())
                                        self.lb.insert(tk.END, "ID: " + str(avion.getId()) + " " * (
                                            7 - len(str(avion.getId()))) + "Valor: " + str(avion.getValor()) + " " * (
                                            8 - len(str(avion.getValor()))) + "Modelo: " + avion.getModelo())
                                        pantallaEliminarAvion()
                    
                                self.nl = Label(self.of, text="Modelo:", font=Font(family='Courier', size=100))
                                self.nl.grid(row=1, column=0, padx=0, pady=5, sticky="w")
                                self.modelo_entry = Entry(self.of, width=20)
                                self.modelo_entry.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")
                    
                                self.el = Label(self.of, text="Peso Max:", font=Font(family='Courier', size=100))
                                self.el.grid(row=2, column=0, padx=0, pady=5, sticky="w")
                                self.pesomax_entry = Entry(self.of, width=20)
                                self.pesomax_entry.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")
                    
                                self.ccl = Label(self.of, text="Valor:", font=Font(family='Courier', size=100))
                                self.ccl.grid(row=3, column=0, padx=0, pady=5, sticky="w")
                                self.valor_entry = Entry(self.of, width=20)
                                self.valor_entry.grid(row=3, column=1, padx=0, pady=5, sticky="nsew")
                    
                                self.suevalue = BooleanVar(self.of)
                                self.suel = Label(self.of, text="Cantidad de asientos:", font=Font(family='Courier', size=100))
                                self.suel.grid(row=4, column=0, padx=0, pady=5, sticky="w")
                                self.suee = Entry(self.of, width=20)
                                self.suee.grid(row=4, column=1, padx=0, pady=5, sticky="nsew")
                                self.suec = ttk.Checkbutton(self.of, text="Asientos por defecto",
                                                            variable=self.suevalue, command=check)
                                self.suec.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
                    
                                self.ingresar = Button(self.of, text="Ingresar nuevo avion", command=ingreso)
                                self.ingresar.grid(row=5, column=0, padx=0, pady=5, sticky="nsew", columnspan=3)
                    
                        else:
                           self.aeropuerto.cancelarAvion(avion)
                           self.lb.delete(curr)

            self.cancelar = Button(self.ventanaOpera, text="Eliminar", command=cancelar)
            self.cancelar.grid(row=4, column=0, padx=5, pady=5, sticky="nsew", columnspan=4)

            self.widgetsActuales.extend([self.lp, self.ld, self.lb, self.scroll, self.of,self.cancelar])


        def pantallaComprarAvion():
            borrarElementos()
            def limpiarFrame():
                for widget in self.of.winfo_children():
                    widget.destroy()

            self.lp = Label(self.fp, text="Comprar avión", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd,
                            text="En este apartado puede realizar la compra de un avión y asignarle un determinado vuelo",
                            font=("Courier", 10))
            self.ld.pack()

            vuelos = self.aeropuerto.getAviones()

            self.scroll = Scrollbar(self.ventanaOpera, orient='vertical')

            self.lb = Listbox(self.ventanaOpera, yscrollcommand=self.scroll.set, font='Courier', width=40, height=22)
            self.lb.grid(row=0, column=0, columnspan=4, sticky="snew", padx=5, pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=4, row=0, sticky='NS')

            for avion in self.aeropuerto.getAviones():
                self.lb.insert(tk.END, "ID: " + str(avion.getId()) + " " * (
                        7 - len(str(avion.getId()))) + "Valor: " + str(avion.getValor()) + " " * (
                        8 - len(str(avion.getValor()))) + "Modelo: " + avion.getModelo())

            self.of = Frame(self.ventanaOpera)
            self.of.grid(row=0, column=5, rowspan=4, sticky='nsew', padx=30, pady=30)



            self.tl = Label(self.of, text="Ingrese los datos del nuevo avion",
                            font=Font(family='Courier', size=100))
            self.tl.grid(row=0, column=0, padx=0, pady=5, sticky="w", columnspan=2)

            def check():
                if self.suevalue.get():
                    self.suee.delete(0, tk.END)
                    self.suee.insert(0, 20)
                    self.suee.config(state='disabled')
                else:
                    self.suee.config(state='normal')
                    self.suee.delete(0, tk.END)
            
            def ingresar():
                fallo = False
                try:
                    ExcepcionVacio.valorVacio(self.modelo_entry.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                        message=f"La entrada Modelo está vacía, por favor completar.")

                try:
                    ExcepcionVacio.valorVacio(self.pesomax_entry.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                        message=f"La entrada Peso Max está vacía, por favor completar.")
                
                try:
                    ExcepcionVacio.valorVacio(self.valor_entry.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                        message=f"La entrada Valor está vacía, por favor completar.")
                
                try:
                    ExcepcionVacio.valorVacio(self.suee.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                        message=f"La entrada Asientos está vacía, por favor completar.")

                try:
                    ExcepcionEntero.tipoInt(self.pesomax_entry.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                           message=f"La entrada {self.pesomax_entry.get()} debe ser un número, por favor modificar.")

                try:
                    ExcepcionEntero.tipoInt(self.valor_entry.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                           message=f"La entrada {self.valor_entry.get()} debe ser un número, por favor modificar.")

                try:
                    ExcepcionEntero.tipoInt(self.suee.get())
                except:
                    fallo = True
                    messagebox.showwarning(title="Advertencia",
                                           message=f"La entrada {self.suee.get()} debe ser un número, por favor modificar.")
                
                if not fallo:
                    avion = Avion(self.modelo_entry.get(),int(self.pesomax_entry.get()),int(self.valor_entry.get()),int(self.suee.get()))
                    self.aeropuerto.transaccion(f"Compra de {avion.getModelo()}",-avion.getValor())
                    self.lb.insert(tk.END, "ID: " + str(avion.getId()) + " " * (
                        7 - len(str(avion.getId()))) + "Valor: " + str(avion.getValor()) + " " * (
                        8 - len(str(avion.getValor()))) + "Modelo: " + avion.getModelo())
                    pantallaComprarAvion()

            self.nl = Label(self.of, text="Modelo:", font=Font(family='Courier', size=100))
            self.nl.grid(row=1, column=0, padx=0, pady=5, sticky="w")
            self.modelo_entry = Entry(self.of, width=20)
            self.modelo_entry.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")

            self.el = Label(self.of, text="Peso Max:", font=Font(family='Courier', size=100))
            self.el.grid(row=2, column=0, padx=0, pady=5, sticky="w")
            self.pesomax_entry = Entry(self.of, width=20)
            self.pesomax_entry.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")

            self.ccl = Label(self.of, text="Valor:", font=Font(family='Courier', size=100))
            self.ccl.grid(row=3, column=0, padx=0, pady=5, sticky="w")
            self.valor_entry = Entry(self.of, width=20)
            self.valor_entry.grid(row=3, column=1, padx=0, pady=5, sticky="nsew")

            self.suevalue = BooleanVar(self.of)
            self.suel = Label(self.of, text="Cantidad de asientos:", font=Font(family='Courier', size=100))
            self.suel.grid(row=4, column=0, padx=0, pady=5, sticky="w")
            self.suee = Entry(self.of, width=20)
            self.suee.grid(row=4, column=1, padx=0, pady=5, sticky="nsew")
            self.suec = ttk.Checkbutton(self.of, text="Asientos por defecto",
                                        variable=self.suevalue, command=check)
            self.suec.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

            self.ingresar = Button(self.of, text="Crear nuevo avion", command=ingresar)
            self.ingresar.grid(row=5, column=0, padx=0, pady=5, sticky="nsew", columnspan=3)

            self.widgetsActuales.extend(
                [self.lp, self.ld, self.lb,
                 self.scroll, self.of])

        def pantallaNomina():
            def aceptarfun():
                empleadosi = []
                total = 0
                for i in self.checkemp.curselection():
                    empleadosi.append(empleados[i])
                    total += empleados[i].getSueldo()

                opcion = messagebox.askokcancel('Alerta de pago', f'Está a punto de pagar ${total}\nCofirmar?')
                if opcion:
                    try:
                        ExcepcionValorMaximo.menorQue(total, self.aeropuerto.getDinero())
                        for e in empleadosi:
                            self.aeropuerto.transaccion(f'nomina de {e.getNombre()}', (-1) * e.getSueldo())
                            pantallaFinanzas()

                    except ExcepcionValorMaximo:
                        messagebox.showerror('Error',
                                             f'Fondos insuficientes\nsolo tienes ${self.aeropuerto.getDinero()}')

                    """if total > self.aeropuerto.getDinero():
                        messagebox.showerror('Error',
                                             f'Fondos insuficientes\nsolo tienes {self.aeropuerto.getDinero()}')
                    else:
                        for e in empleadosi:
                            self.aeropuerto.transaccion(f'nomina de {e.getNombre()}', (-1) * e.getSueldo())
                            pantallaFinanzas()"""

            empleados = self.aeropuerto.getEmpleados()
            empleadosnames = list(map(lambda x: '$ ' + str(x.getSueldo()) + ' | ' + x.getNombre(), empleados))

            self.label1 = Label(self.ventanaOpera, text="Seleccione los empleados\na los que les va a pagar",
                                font=("Courier", 10))

            self.framelist = Frame(self.ventanaOpera)
            self.checkemp = Listbox(self.framelist, selectmode='multiple')
            self.scroll = Scrollbar(self.framelist, orient=VERTICAL)
            self.checkemp.config(yscrollcommand=self.scroll.set)
            self.scroll.config(command=self.checkemp.yview)
            self.checkemp.insert(0, *empleadosnames)

            self.aceptar = Button(self.ventanaOpera, text='Aceptar', command=aceptarfun)

            self.label1.grid(padx=8, pady=1, row=2, column=0)
            self.scroll.pack(side=RIGHT, fill=Y)
            self.checkemp.pack(fill=X)
            self.framelist.grid(ipadx=80, padx=80, pady=10, row=3, column=0, rowspan=5)
            self.aceptar.grid(ipadx=80, padx=80, pady=10, row=8, column=0)

            self.widgetsActuales.extend([self.checkemp, self.aceptar, self.label1, self.scroll])

        def pantallaTransacciones():
            def aceptarfun():
                valor = self.entrada_valor.get()
                concepto = self.entrada_concepto.get()
                combo = self.combo.get()
                if combo == 'Retiro':
                    opcion = messagebox.askokcancel('Alerta de pago', f'Está a punto de pagar ${valor}\nCofirmar?')
                else:
                    opcion = messagebox.askokcancel('Alerta de pago', f'Está a punto de ingresar ${valor}\nCofirmar?')
                if concepto == '':
                    concepto = 'Sin concepto'

                if opcion:
                    try:
                        valor = float(valor)
                        ExcepcionPositivo.valorPositivo(valor)

                        if combo == 'Ingreso':
                            self.aeropuerto.transaccion(concepto, valor)
                            pantallaFinanzas()

                        elif combo == 'Retiro':
                            ExcepcionValorMaximo.menorQue(valor, self.aeropuerto.getDinero())
                            self.aeropuerto.transaccion(concepto, valor * (-1))
                            pantallaFinanzas()

                        else:
                            messagebox.showerror('Error', 'Debes seleccionar Ingreso o Retiro')
                            
                    except ExcepcionPositivo:
                        messagebox.showerror('Error', 'No puedes introducir un numero negativo ni cero')
                    except ExcepcionValorMaximo:
                        messagebox.showerror('Error', f'Fondos insuficientes\nsolo tienes {self.aeropuerto.getDinero()}')
                    except ValueError:
                        messagebox.showerror('Error', 'Debes introducir solamente numeros en el monto')

            textstr = ""
            textconcept = ""
            textvalue = ""
            for i in range(len(self.aeropuerto.getTransaccionesKeys())):
                textstr += str(self.aeropuerto.getTransaccionesValues()[i]) + \
                           ' ' * (10 - len(str(self.aeropuerto.getTransaccionesValues()[i]))) + '|  ' + \
                           self.aeropuerto.getTransaccionesKeys()[i] + '\n'

            self.frametrans = Frame(self.ventanaOpera, width='25', height='25')
            self.scrolltrans = Scrollbar(self.frametrans)
            self.text = Text(self.frametrans, wrap=NONE, width='50', yscrollcommand=self.scrolltrans.set)
            self.text.bind("<Key>", lambda e: "break")
            self.text.delete(1.0, END)
            self.text.insert(END, textstr)
            self.newtrans = Label(self.ventanaOpera, text='Nueva transaccion', bg='gray80')
            self.combo = ttk.Combobox(self.ventanaOpera, state='readonly', values=['Ingreso', 'Retiro'])
            self.le = Label(self.ventanaOpera, text='Ingresa el concepto de la transaccion:')
            self.entrada_concepto = Entry(self.ventanaOpera)
            self.le2 = Label(self.ventanaOpera, text='Ingresa el monto de la transaccion:')
            self.entrada_valor = Entry(self.ventanaOpera)
            self.aceptar = Button(self.ventanaOpera, text='Aceptar', command=aceptarfun)

            self.scrolltrans.config(command=self.text.yview)

            self.frametrans.grid(row=2, column=1, rowspan=7, columnspan=1)
            self.newtrans.grid(row=2, column=2, columnspan=2, sticky='snew', ipadx=1, ipady=1, pady=2, padx=30)
            self.combo.grid(row=3, column=2, sticky='sw', padx=30)
            self.le.grid(row=4, column=2, sticky='sw', ipadx=1, ipady=1, pady=2, padx=30)
            self.entrada_concepto.grid(row=5, column=2, sticky='nwe', ipadx=1, ipady=1, pady=2, padx=30)
            self.le2.grid(row=6, column=2, sticky='sw', ipadx=1, ipady=1, pady=2, padx=30)
            self.entrada_valor.grid(row=7, column=2, sticky='nwe', ipadx=1, ipady=1, pady=2, padx=30)
            self.aceptar.grid(row=8, column=2, ipadx=80, padx=80, pady=10,)
            self.scrolltrans.pack(side=RIGHT, fill=Y)
            self.text.pack(side=LEFT)
            self.widgetsActuales.extend([self.frametrans, self.newtrans, self.combo, self.le, self.entrada_concepto,
                                         self.le2, self.entrada_valor, self.aceptar])

        def pantallaFinanzas():
            borrarElementos()

            self.lp = Label(self.fp, text="Gestor de Finanzas", font=("Courier", 12), height=2, bg="gray80")
            self.ld = Label(self.fd,
                            text="En este apartado puede realizar el pago de nomina a los empleados, registrar los "
                                 "cambios con el dinero del aeropuerto, y ver el historial de transacciones",
                            font=("Courier", 10))
            self.labeldinero = Label(self.ventanaOpera, text=f'Dinero del Aeropuerto: {self.aeropuerto.getDinero()}',
                                     font=("Courier", 10), bg='gray10', fg='white')
            self.bnomina = Button(self.ventanaOpera, text='Nomina', command=pantallaNomina)
            self.btrans = Button(self.ventanaOpera, text='Transacciones', command=pantallaTransacciones)

            # self.checkemp = ChecklistBox(self.ventanaOpera)
            self.lp.pack()
            self.ld.pack()
            self.labeldinero.grid(ipadx=0, padx=0, pady=0, row=0, column=0, columnspan=4, sticky='nsew')
            #root.columnconfigure(1, weight=1)
            self.bnomina.grid(ipadx=80, padx=80, pady=30, row=1, column=0)
            self.btrans.grid(ipadx=80, padx=80, pady=30, row=1, column=1, columnspan=1)
            self.ventanaOpera.columnconfigure(0, weight=1)
            self.ventanaOpera.columnconfigure(1, weight=1)
            self.ventanaOpera.columnconfigure(2, weight=1)

            self.widgetsActuales.extend([self.lp, self.ld, self.bnomina, self.btrans, self.labeldinero])

        def pantallaProgramarVuelo():
            borrarElementos()

            self.lp = Label(self.fp, text="Programar Vuelo", font=("Courier", 12), height=2, bg="gray80")
            self.lp.pack()
            self.ld = Label(self.fd,
                            text="En este apartado puede programar un nuevo vuelo",
                            font=("Courier", 10))
            self.ld.pack()

            self.l1 = Label(self.ventanaOpera, text='Fecha')
            self.l2 = Label(self.ventanaOpera, text='Hora')
            self.l4 = Label(self.ventanaOpera, text='Minutos')
            self.l3 = Label(self.ventanaOpera, text='Aviones disponibles')
            self.e1 = Entry(self.ventanaOpera)
            self.e2 = Entry(self.ventanaOpera)
            self.esub = Label(self.ventanaOpera, text=':')
            self.e3 = Entry(self.ventanaOpera)
            self.l1.grid(row=0, column=0)
            self.l2.grid(row=0, column=2)
            self.l4.grid(row=0, column=4)
            self.l3.grid(row=2, column=0, columnspan=5)
            self.e1.grid(row=1, column=0)
            self.e2.grid(row=1, column=1)
            self.e2.grid(row=1, column=2)
            self.esub.grid(row=1, column=3)
            self.e3.grid(row=1, column=4)

            self.scroll = Scrollbar(self.ventanaOpera, orient='vertical')
            self.lb = Listbox(self.ventanaOpera, yscrollcommand=self.scroll.set, font='Courier', width=40, height=16)
            self.lb.grid(row=3, column=0, columnspan=5, sticky="snew", padx=5, pady=5)

            self.scroll.configure(command=self.lb.yview)
            self.scroll.grid(column=5, row=3, sticky='NS')

            for i in self.aeropuerto.getAviones():
                self.lb.insert(tk.END, "ID: " + str(i.getId()) + " " * (
                        7 - len(str(i.getId()))) + "Valor: " + str(i.getValor()) + " " * (
                        8 - len(str(i.getValor()))) + "Modelo: " + i.getModelo())

            self.of = Frame(self.ventanaOpera)
            self.of.grid(row=0, column=6, rowspan=4, sticky='nsew', padx=30, pady=30)

            self.tl = Label(self.of, text="Ingrese los datos del nuevo vuelo",
                            font=Font(family='Courier', size=100))
            self.tl.grid(row=0, column=0, padx=0, pady=5, sticky="w", columnspan=2)

            self.sl = Label(self.of, text="Identificador:", font=Font(family='Courier', size=100))
            self.sl.grid(row=1, column=0, padx=0, pady=5, sticky="w")
            self.sc = ttk.Combobox(self.of, state="readonly", values=["Nacional", "Internacional"], width=20)
            self.sc.grid(row=1, column=1, padx=0, pady=5, sticky="nsew")

            self.nl = Label(self.of, text="Destino:", font=Font(family='Courier', size=100))
            self.nl.grid(row=2, column=0, padx=0, pady=5, sticky="w")
            self.destino = Entry(self.of, width=20)
            self.destino.grid(row=2, column=1, padx=0, pady=5, sticky="nsew")

            self.el = Label(self.of, text="Costo:", font=Font(family='Courier', size=100))
            self.el.grid(row=3, column=0, padx=0, pady=5, sticky="w")
            self.costo = Entry(self.of, width=20)
            self.costo.grid(row=3, column=1, padx=0, pady=5, sticky="nsew")

            self.ccl = Label(self.of, text="Sala de embarque:", font=Font(family='Courier', size=100))
            self.ccl.grid(row=4, column=0, padx=0, pady=5, sticky="w")
            self.sala = Entry(self.of, width=20)
            self.sala.grid(row=4, column=1, padx=0, pady=5, sticky="nsew")

            def obtenerAvion():
                global avionElegido
                indice = self.lb.curselection()
                idAvion = int(self.lb.get(indice).split("      Valor:")[0][4:])
                for i in self.aeropuerto.getAviones():
                    if i.getId() == idAvion: avionElegido = i
                try:
                    fecha = self.e1.get() + " " + self.e2.get() + ":" + self.e3.get()
                    Vuelo(avionElegido, datetime.strptime(fecha,'%d/%m/%Y %H:%M'),self.destino.get(),int(self.costo.get()),self.sala.get())
                    self.conf = Label(self.of, text="El vuelo ha sido agendado!", font=Font(family='Courier', size=100))
                    self.conf.grid(row=7, column=0, padx=0, pady=5)
                    self.widgetsActuales.append(self.conf)
                except ExcepcionTipo:
                    messagebox.showwarning(title="Advertencia",
                                        message=f"Los tipos de datos requeridos no concuerdan, revise el formato de fecha.")

            self.ingresar = Button(self.of, text="Ingresar nuevo vuelo", command=obtenerAvion)
            self.ingresar.grid(row=6, column=0, padx=0, pady=5, sticky="nsew", columnspan=3)

            self.widgetsActuales.extend(
                [self.lp, self.ld, self.lb, self.l1, self.l2, self.l3, self.l4, self.e1, self.e2, self.e3, self.esub,
                 self.scroll, self.of])


        # Menus
        self._barraMenu = Menu(self)

        archivo = Menu(self._barraMenu)
        self._barraMenu.add_cascade(label="Archivo", menu=archivo)
        archivo.add_command(label="Aplicacion", command=descripcion)
        archivo.add_command(label="Salir y guardar", command=self.salir)

        self.procesosYConsultas = Menu(self._barraMenu)

        self._barraMenu.add_cascade(label="Procesos y consultas", menu = self.procesosYConsultas)
        self.procesosYConsultas.add_command(label = "Reserva de vuelo", command = pantallaReservaDeVuelo)
        self.procesosYConsultas.add_command(label = "Programar vuelo", command = pantallaProgramarVuelo)
        self.procesosYConsultas.add_command(label = "Gestion de empleados", command = pantallaEmpleados)
        self.procesosYConsultas.add_command(label = "Gestionar finanzas", command = pantallaFinanzas)

        self.menuModificaciones = Menu(self.procesosYConsultas)
        self.procesosYConsultas.add_cascade(menu=self.menuModificaciones, label="Administración de vuelos y aviones")
        self.menuModificaciones.add_command(label="Cambiar asiento", command=pantallaCambiarAsiento)
        self.menuModificaciones.add_command(label="Cancelar vuelo", command=pantallaCancelarVuelo)
        self.menuModificaciones.add_command(label="Eliminar avión", command=pantallaEliminarAvion)
        self.menuModificaciones.add_command(label="Comprar avión", command=pantallaComprarAvion)

        ayuda = Menu(self._barraMenu)
        self._barraMenu.add_cascade(label="Ayuda", menu=ayuda)
        ayuda.add_command(label="Acerca de", command=info)

        self.config(menu=self._barraMenu)

        # Frames
        self.frame = Frame(self, relief="ridge", bd=2, bg="black")
        self.frame.pack(padx=15, pady=15, expand=True, fill=BOTH)
        self.fp = Frame(self.frame, bg="gray80")
        self.fp.pack(ipadx=6, padx=2, ipady=2, pady=2, fill=X)
        self.fd = Frame(self.frame)
        self.fd.pack(ipadx=2, padx=2, ipady=2, pady=2, fill=X)
        self.ventanaOpera = Frame(self.frame, bd=2)
        self.ventanaOpera.pack(padx=5, pady=5, fill=BOTH, expand=True)

        # Llamado a pantalla principal
        pantallaPrincipal()

    def valoresIniciales(self):

        self.aeropuerto.setDinero(10000000)
        a1 = Avion("XYZ", 100, 50000)
        vuelo1 = Vuelo(a1, datetime(2022, 11, 30, 10, 0, 0), "Cancun", 1500, "A1")
        vuelo2 = Vuelo(Avion("YY3X", 150, 75000), datetime(2022, 10, 15, 10, 0, 0), "Madrid", 3250, "A2")
        vuelo3 = Vuelo(Avion("XCF", 75, 25000), datetime(2022, 12, 5, 10, 0, 0), "Paris", 5500, "A2")
        e1 = Empleado("Juan", 12345, 30, "M", 2300, Cargos.PILOTO.getCargo())
        e2 = Empleado("Pedro", 543657, 35, "M", 1800, Cargos.COPILOTO.getCargo())
        e3 = Empleado("Sara", 4235246, 66, "F", 1500, Cargos.CONTROL_DE_PISTA.getCargo())
        e4 = Empleado("Carla", 67436653, 35, "F", 1500, Cargos.AZAFATA.getCargo())
        e5 = Empleado("Federico", 9787845, 40, "M", 1800, Cargos.AZAFATA.getCargo())
        e6 = Empleado("Andrea", 2425, 38, "F", 1800, Cargos.PILOTO.getCargo())
        e7 = Empleado("Camilo", 27354235, 60, "M", 1800, Cargos.PILOTO.getCargo())
        e8 = Empleado("Maria", 14136, 55, "F", 1800, Cargos.CONTROL_DE_PISTA.getCargo())
        e9 = Empleado("Fernando", 64378, 23, "M", 1800, Cargos.AZAFATA.getCargo())
        Empleado("Paco", 451675, 48, "M", 1800, Cargos.CONTROL_DE_PISTA.getCargo())
        Empleado("Camila", 2565324, 19, "F", 1800, Cargos.COPILOTO.getCargo())
        Empleado("Luisa", 47594, 34, "F", 1800, Cargos.PILOTO.getCargo())
        Empleado("Jose", 11055, 45, "M", 1800, Cargos.AZAFATA.getCargo())

        e1.setVuelo(vuelo1)
        e2.setVuelo(vuelo1)
        e3.setVuelo(vuelo1)
        e4.setVuelo(vuelo2)
        e5.setVuelo(vuelo2)
        e6.setVuelo(vuelo2)
        e7.setVuelo(vuelo3)
        e8.setVuelo(vuelo3)
        e9.setVuelo(vuelo3)

        p1 = Pasajero("Samara", 4535436, 18, "F")
        p2 = Pasajero("Carolina", 14364535, 20, "F")
        p3 = Pasajero("Catalina", 654623562, 27, "F")
        p4 = Pasajero("Ana", 1443524, 56, "F")
        p5 = Pasajero("Sofia", 13424565, 31, "F")
        p6 = Pasajero("Valentina", 348764, 43, "F")
        p7 = Pasajero("Felipe", 534556, 64, "M")
        p8 = Pasajero("Sebastian", 37467, 46, "M")
        p9 = Pasajero("Cristian", 453786, 36, "M")
        p10 = Pasajero("Andres", 237237, 36, "M")
        p11 = Pasajero("Julian", 764521, 65, "M")
        p12 = Pasajero("Julio", 7868754, 35, "M")

        for i in self.aeropuerto.getPasajeros():
            i.addEquipaje(Equipaje(5))

        vuelo1.agregarPasajero(p1, 1)
        vuelo1.agregarPasajero(p2, 2)
        vuelo1.agregarPasajero(p3, 3)
        vuelo1.agregarPasajero(p4, 4)
        vuelo2.agregarPasajero(p5, 1)
        vuelo2.agregarPasajero(p6, 2)
        vuelo2.agregarPasajero(p7, 3)
        vuelo2.agregarPasajero(p8, 4)
        vuelo3.agregarPasajero(p9, 1)
        vuelo3.agregarPasajero(p10, 2)
        vuelo3.agregarPasajero(p11, 3)
        vuelo3.agregarPasajero(p12, 4)

    def salir(self):
        self.__class__.VSabierta = False
        self.ventanaInicio.iconify()
        self.ventanaInicio.deiconify()
        serializar(self.aeropuerto)
        self.destroy()
