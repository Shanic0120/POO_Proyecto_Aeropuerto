// Autores: Juan Jose Zapata Cadavid, Juan Camilo Molina Roncancio
/* Se encarga del manejo de los atributos del aeropuerto, como su nombre indica
 * es donde se van a almacenar todos los datos del sistema.
 */

package gestorAplicacion.gestionVuelos;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import basedatos.Deserializador;
import gestorAplicacion.gestionHumana.Empleado;
import gestorAplicacion.gestionHumana.Pasajero;

public class Aeropuerto implements Serializable, zonasEmbarque {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String nombre;
	private List<Vuelo> vuelos = new ArrayList<>();
	private List<Empleado> empleados = new ArrayList<>();
	private List<Pasajero> pasajeros = new ArrayList<>();
	private List<Avion> aviones = new ArrayList<>();
	private List<String> transaccionesKeys = new ArrayList<>();
	private List<Integer> transaccionesValues = new ArrayList<>();
	private long dinero;

	public Aeropuerto() {
		Deserializador.deserializar(this);
	}

	public void ingresarDinero(int pago) {
		dinero += pago;
	}

	public long getDinero() {
		return dinero;
	}

	public void setDinero(long dinero) {
		this.dinero = dinero;
	}

	public Aeropuerto(String nombre) {
		this.nombre = nombre;
	}

	public void agregarVuelo(Vuelo vuelo) {
		this.vuelos.add(vuelo);
	}

	public void agregarEmpleado(Empleado empleado) {
		this.empleados.add(empleado);
	}

	public void agregarAvion(Avion avion) {
		this.aviones.add(avion);
	}

	public List<Vuelo> getVuelos() {
		return vuelos;
	}

	public void setVuelos(List<Vuelo> vuelos) {
		this.vuelos = vuelos;
	}

	public List<Empleado> getEmpleados() {
		return empleados;
	}

	public void setEmpleados(List<Empleado> empleados) {
		this.empleados = empleados;
	}

	public List<Avion> getAviones() {
		return aviones;
	}

	public void setAviones(List<Avion> aviones) {
		this.aviones = aviones;
	}

	public List<Pasajero> getPasajeros() {
		return pasajeros;
	}

	public void setPasajeros(List<Pasajero> pasajeros) {
		this.pasajeros = pasajeros;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void despedirEmpleado(Empleado empleado) {
		if (empleado.getVuelo() != null) {
			empleado.getVuelo().getEmpleados().remove(empleado);
		}

		empleados.remove(empleados.indexOf(empleado));
	}

	/*
	 * metodo para realizar una transaccion primer argumento es un String con el
	 * concepto (breve descripcion) de la transaccion segundo argumento es el valor
	 * de la transaccion (si es retiro de dinero debe ser negativo) el metodo retira
	 * el dinero correspondiente del aeropuerto y añade la transaccion a la lista
	 */
	public void transaccion(String concepto, int valor) {
		transaccionesKeys.add(concepto);
		transaccionesValues.add(valor);

		ingresarDinero(valor);
	}

	// Metodo para desplegar el historial de transacciones al usuario
	public String transacciones() {
		int acumulador = 0;
		StringBuilder historial = new StringBuilder();

		for (int i = 0; i < Math.min(transaccionesKeys.size(), transaccionesValues.size()); i++) {
			historial.append(i + 1).append(":  ").append(transaccionesKeys.get(i)).append(" --- ")
					.append(transaccionesValues.get(i)).append("\n");
			acumulador += transaccionesValues.get(i);
		}
		historial.append("rendimiento total : --- ").append(acumulador);
		return historial.toString();
	}

	public List<String> getTransaccionesKeys() {
		return transaccionesKeys;
	}

	public void setTransaccionesKeys(List<String> transaccionesKeys) {
		this.transaccionesKeys = transaccionesKeys;
	}

	public List<Integer> getTransaccionesValues() {
		return transaccionesValues;
	}

	public void setTransaccionesValues(List<Integer> transaccionesValues) {
		this.transaccionesValues = transaccionesValues;
	}
}
