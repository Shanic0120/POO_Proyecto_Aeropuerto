import pickle
import os
import pathlib

def deserializar(aeropuerto):
    #Apertura del archivo donde será leido el flujo de bytes que representen el objeto. En este caso se trata de administracion
    ruta=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\aeropuerto"),"rb")
    #Indicamos la variable donde se guardará el objeto deserializado. En este caso el valor de la caja de Administración
    aertemp=pickle.load(ruta)
    aeropuerto.setNombre(aertemp.getNombre())
    aeropuerto.setVuelos(aertemp.getVuelos())
    aeropuerto.setPasajeros(aertemp.getPasajeros())
    aeropuerto.setEmpleados(aertemp.getEmpleados())
    aeropuerto.setAviones(aertemp.getAviones())
    aeropuerto.setTransaccionesKeys(aertemp.getTransaccionesKeys())
    aeropuerto.setTransaccionesValues(aertemp.getTransaccionesValues())
    aeropuerto.setDinero(aertemp.getDinero())
    #Se cierra el archivo abierto
    ruta.close()