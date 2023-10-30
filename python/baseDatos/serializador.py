import os
import pathlib
import pickle

def serializar(aeropuerto):
    #Creación y apertura del archivo donde será guardado el flujo de bytes que representen el objeto. En este caso se trata de administracion
    ruta=open(os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\aeropuerto"),"wb") 
    #Indicamos el dato que será serializado.
    pickle.dump(aeropuerto,ruta)
    #Se cierra el archivo creado
    ruta.close()