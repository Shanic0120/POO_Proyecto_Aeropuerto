// Autores: Juan Camilo Molina Roncancio
/*
 * Esta interfaz es implementada por Aeropuerto, aqui se agrupan todas las salas de embarque disponibles
 * en el aeropuerto guardadas como constantes.
 */
package gestorAplicacion.gestionVuelos;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public interface zonasEmbarque {

	String sala1 = "A1";
	String sala2 = "A2";
	String sala3 = "A3";
	String sala4 = "B1";
	String sala5 = "B2";
	String sala6 = "B3";
	String sala7 = "C1";
	String sala8 = "C2";
	String sala9 = "C3";
	String sala10 = "D1";
	String sala11 = "D2";
	String sala12 = "D3";

	List<String> conjunto = new ArrayList<>(
			Arrays.asList(sala1, sala2, sala3, sala4, sala5, sala6, sala7, sala8, sala9, sala10, sala11, sala12));

	/*
	 * Este metodo retorna un String con toda la informacion de las salas formateadas para posteriormente
	 * ser imprimida en uiMain para la creacion de vuelos.
	 */
	static String mostrarZonas() {
		String zondisp = "";
		zondisp += "\n\t\tZona A\n";
		for (int i = 0; i < 3; i++) {
			zondisp += " - " + conjunto.get(i) + " - ";
		}
		zondisp += "\n\t\tZona B\n";
		for (int i = 3; i < 6; i++) {
			zondisp += " - " + conjunto.get(i) + " - ";
		}
		zondisp += "\n\t\tZona C\n";
		for (int i = 6; i < 9; i++) {
			zondisp += " - " + conjunto.get(i) + " - ";
		}
		zondisp += "\n\t\tZona D\n";
		for (int i = 9; i < 12; i++) {
			zondisp += " - " + conjunto.get(i) + " - ";
		}
		zondisp += "\n";
		return zondisp;
	}
}
