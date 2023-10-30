// Autores: Maria Camila Zapata Arrubla, Juan Camilo Molina Roncancio
/* Descripcion: Esta clase permite la creacion de aviones, generar un tiquete y agregar un pasajero a un determinado vuelo,
 * se dispone de la opcion de encontrar un vuelo
 */

package gestorAplicacion.gestionVuelos;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import gestorAplicacion.gestionHumana.Empleado;
import gestorAplicacion.gestionHumana.Pasajero;

public class Vuelo implements Serializable {
	/**
	 *
	 */
	private static final long serialVersionUID = 1L;
	private Avion avion;
	private List<Empleado> empleados = new ArrayList<>();
	private List<Pasajero> pasajeros = new ArrayList<>();
	private LocalDateTime fecha;
	private final static String origen = "Medellin";
	private String destino;
	private boolean enVuelo;
	private int costo;
	private String salaEmbarque;
	private double pesoActual;
	private final int id;
	private static Aeropuerto aeropuerto;

	public Vuelo(Avion avion, LocalDateTime fecha, String destino, int costo, String salaEmbarque) {
		this.avion = avion;
		this.fecha = fecha;
		this.destino = destino;
		this.costo = costo;
		this.salaEmbarque = salaEmbarque;
		this.id = nuevoID();
		aeropuerto.agregarVuelo(this);

	}

	public static int nuevoID() {
		if (aeropuerto.getVuelos().size() != 0) {
			return aeropuerto.getVuelos().get(aeropuerto.getVuelos().size() - 1).getId() + 1;
		} else {
			return 1;
		}
	}

	public boolean agregarPasajero(Pasajero pasajero, int nroAsiento) {

		double pesoEquipajePasajero = 0;
		for (Equipaje equipaje : pasajero.getEquipajes())
			pesoEquipajePasajero += equipaje.getPeso();
		Asiento asientoElegido = avion.getAsientos().get(nroAsiento - 1);

		if (pesoActual + pesoEquipajePasajero < avion.getPesoMaximo() && pasajeros.size() < avion.getAsientos().size()
				&& !asientoElegido.isOcupado()) {
			pesoActual += pesoEquipajePasajero;
			pasajeros.add(pasajero);
			pasajero.setAsiento(asientoElegido);
			pasajero.setVuelo(this);
			asientoElegido.setOcupado(true);
			if (asientoElegido.getClase().equals("Primera clase")) {
				aeropuerto.transaccion("Boleto Primera Clase", 3 * costo);
				pasajero.setInversion(3 * costo);
			} else if (asientoElegido.getClase().equals("Ejecutiva")) {
				aeropuerto.transaccion("Boleto Clase Ejecutiva", 2 * costo);
				pasajero.setInversion(2 * costo);
			} else {
				aeropuerto.transaccion("Boleto Clase Turista", costo);
				pasajero.setInversion(costo);
			}
			return true;
		} else {
			return false;
		}
	}

	@Override
	public String toString() {
		String infoVuelo = "ID vuelo: " + id + " - Fecha del vuelo: " + fecha + " - Origen: " + origen + " - Destino: "
				+ destino + " - Precio: " + costo + "\n";
		return infoVuelo;
	}

	public String tiquete(Pasajero pasajero) {
		String tique = "\n" + "Ha sido registrado exitosamente" + "\n" + "\n" + "------------------------------------\n"
				+ "             Tiquete " + "\n" + "------------------------------------\n"
				+ "Nombre Pasajero: " + pasajero.getNombre() + "\n" + "Fecha: " + fecha + "\n" + "Vuelo: " + getId()
				+ "\n" + "Sala de embarque: " + pasajero.getVuelo().getSalaEmbarque() + "\n" + "Clase: "
				+ pasajero.getAsiento().getClase() + "\n" + "Num Silla: " + pasajero.getAsiento().getNumero() + "\n"
				+ "Origen: " + origen + "\n" + "Destino: " + getDestino() + "\n" + "Precio Total: "
				+ pasajero.getInversion() + "\n" + "------------------------------------\n";
		return tique;
	}

	public Avion getAvion() {
		return avion;
	}

	public void setAvion(Avion avion) {
		this.avion = avion;
	}

	public List<Empleado> getEmpleados() {
		return empleados;
	}

	public void setEmpleados(List<Empleado> empleados) {
		this.empleados = empleados;
	}

	public List<Pasajero> getPasajeros() {
		return pasajeros;
	}

	public void setPasajeros(List<Pasajero> pasajeros) {
		this.pasajeros = pasajeros;
	}

	public LocalDateTime getFecha() {
		return fecha;
	}

	public void setFecha(LocalDateTime fecha) {
		this.fecha = fecha;
	}

	public String getOrigen() {
		return origen;
	}

	public String getDestino() {
		return destino;
	}

	public void setDestino(String destino) {
		this.destino = destino;
	}

	public boolean isEnVuelo() {
		return enVuelo;
	}

	public void setEnVuelo(boolean enVuelo) {
		this.enVuelo = enVuelo;
	}

	public int getCosto() {
		return costo;
	}

	public void setCosto(int costo) {
		this.costo = costo;
	}

	public String getSalaEmbarque() {
		return salaEmbarque;
	}

	public void setSalaEmbarque(String salaEmbarque) {
		this.salaEmbarque = salaEmbarque;
	}

	public double getPesoActual() {
		return pesoActual;
	}

	public void setPesoActual(double pesoActual) {
		this.pesoActual = pesoActual;
	}

	public int getId() {
		return id;
	}

	public static void setAeropuerto(Aeropuerto aeropuerto) {
		Vuelo.aeropuerto = aeropuerto;
	}

	public static Vuelo encontrarVuelo(int id) {
		if (id - 1 <= aeropuerto.getVuelos().size()) {
			return aeropuerto.getVuelos().get(id - 1);
		}
		return null;
	}
}
