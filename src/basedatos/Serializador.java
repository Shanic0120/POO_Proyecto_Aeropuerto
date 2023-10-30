// Autores: Juan Jose Zapata Cadavid
/*
 * Guardar los archivos para no perder informacion al terminar de ejecutar
 */
package basedatos;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

import gestorAplicacion.gestionVuelos.Aeropuerto;

public class Serializador {
	/*
	 * Guarda en el archivo txt el objeto aeropuerto pasado por parametro
	 */
	public static <E> void serializar(Aeropuerto aeropuerto) {
		FileOutputStream fos;
		try {
			String ruta = System.getProperty("user.dir") + "\\src\\basedatos\\temp\\aeropuerto.txt";
			fos = new FileOutputStream(ruta);
			ObjectOutputStream outputStream = new ObjectOutputStream(fos);
			outputStream.writeObject(aeropuerto);
			outputStream.close();
			fos.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
}
