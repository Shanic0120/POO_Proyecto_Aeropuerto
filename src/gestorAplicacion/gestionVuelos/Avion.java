// Autores: Juan Camilo Molina Roncancio
/*
 * En esta clase se agrupa la informacion de los aviones que posea el aeropuerto, se asigna el id automaticamente
 * los demas atributos como modelo, peso maximo que soporta y valor esta definido por el usuario, la cantidad de asientos
 * puede ser una cantidad aleatoria entre 15 o 20 o el usuario puede elegir la cantidad de los mismos.
 */
package gestorAplicacion.gestionVuelos;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

public class Avion implements Serializable {
	/**
	 *
	 */
	private static final long serialVersionUID = 1L;
	private int id;
	private String modelo;
	private int pesoMaximo;
	private List<Asiento> asientos = new ArrayList<>();
	private int valor;
	private static Aeropuerto aeropuerto;

	public Avion(){
		this.genAsientos(15, 20);
	}

	public Avion(String modelo, int pesoMaximo, int valor) {
		this();
		this.modelo = modelo;
		this.pesoMaximo = pesoMaximo;
		this.valor = valor;
		this.id = nuevoID();
		aeropuerto.agregarAvion(this);
	}

	public Avion(String modelo, int pesoMaximo, int valor, int cantidadAsientos){
		this.modelo = modelo;
		this.pesoMaximo = pesoMaximo;
		this.valor = valor;
		this.id = nuevoID();
		this.genAsientos(cantidadAsientos, cantidadAsientos);
		aeropuerto.agregarAvion(this);
	}

	public static int nuevoID() {
		if (aeropuerto.getAviones().size() != 0) {
			return aeropuerto.getAviones().get(aeropuerto.getAviones().size() - 1).getId() + 1;
		} else {
			return 1;
		}
	}

	/*
	 * Con esta funcion genero la cantidad de asientos y su clase aleatoriamente, aunque dependiendo del constructor que se use
	 * la cantidad de asientos puede ser fijada por el usuario, solo se asigna aleatoriamente la clase.
	 */
	public void genAsientos(int min, int max) {
		List<String> tipoAsiento = new ArrayList<>();
		tipoAsiento.add("Turista");
		tipoAsiento.add("Ejecutiva");
		tipoAsiento.add("Primera clase");

		int cant = (int) (min + Math.random() * (max - min));

		for (int i = 1; i <= cant; i++) {
			int ind = (int) (Math.random() * 3);
			asientos.add(new Asiento(i, tipoAsiento.get(ind)));
		}
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public int getPesoMaximo() {
		return pesoMaximo;
	}

	public void setPesoMaximo(int pesoMaximo) {
		this.pesoMaximo = pesoMaximo;
	}

	public List<Asiento> getAsientos() {
		return asientos;
	}

	public void setAsientos(List<Asiento> asientos) {
		this.asientos = asientos;
	}

	public int getValor() {
		return valor;
	}

	public void setValor(int valor) {
		this.valor = valor;
	}

	public static void setAeropuerto(Aeropuerto aeropuerto) {
		Avion.aeropuerto = aeropuerto;
	}

	@Override
	public String toString() {
		return "ID avion: " + id + " - Modelo: " + modelo + " - Cantidad de asientos: " + asientos.size()
				+ " - Peso maximo: " + pesoMaximo;
	}
}
