// Autores: Juan Jose Zapata Cadavid
/* 
 * Extraer los valores guardados en la memoria para usarlo luego en la RAM
 */
package basedatos;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

import gestorAplicacion.gestionVuelos.Aeropuerto;

public class Deserializador {
	/*
	 * Se encarga de extraer a aeropuerto de aeropuerto.txt y asignar todos los
	 * valores al aeropuerto que se pasa por parametro
	 */
	public static <E> void deserializar(Aeropuerto aeropuerto) {
		FileInputStream fin;

		try {
			String ruta = System.getProperty("user.dir") + "\\src\\basedatos\\temp\\aeropuerto.txt";
			fin = new FileInputStream(ruta);
			ObjectInputStream oos = new ObjectInputStream(fin);
			Aeropuerto e = (Aeropuerto) oos.readObject();

			aeropuerto.setAviones(e.getAviones());
			aeropuerto.setDinero(e.getDinero());
			aeropuerto.setEmpleados(e.getEmpleados());
			aeropuerto.setNombre(e.getNombre());
			aeropuerto.setPasajeros(e.getPasajeros());
			// aeropuerto.setSalas(e.getSalas());
			aeropuerto.setVuelos(e.getVuelos());
			aeropuerto.setTransaccionesKeys(e.getTransaccionesKeys());
			aeropuerto.setTransaccionesValues(e.getTransaccionesValues());

			oos.close();
			fin.close();

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
}
