// Autores: Juan Jose Zapata Cadavid, Juan Camilo Molina Roncancio
/*
 * Empleados del aeropuerto, quienes estan asociados a un vuelo y tiene los datos para poder pagarles, 
 * hereda de persona
 */
package gestorAplicacion.gestionHumana;

import gestorAplicacion.gestionVuelos.Aeropuerto;
import gestorAplicacion.gestionVuelos.Vuelo;

public class Empleado extends Persona {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private int sueldo;
	private String cargo;
	private Vuelo vuelo;
	private int experiencia;

	public Empleado(String nombre, int sueldo, int cedula, Cargos cargo, int edad, String sexo, int experiencia) {
		super(nombre, cedula, edad, sexo);
		this.sueldo = sueldo;
		this.cargo = cargo.getCargo();
		this.experiencia = experiencia;
		aeropuerto.agregarEmpleado(this);
	}

	public Empleado(String nombre, int cedula, Cargos cargo, int edad, String sexo) {
		this(nombre, cargo.getSueldoBase(), cedula, cargo, edad, sexo, 0);
	}

	@Override
	public String toString() {
		if (this.vuelo == null) {
			return "Nombre: " + nombre + ".\nCedula: " + cedula + "\nEdad: " + edad + "\nSexo: " + sexo + ".\nCargo: "
					+ cargo + ".\nSueldo: " + sueldo + "$.\nVuelo: Este empleado aun no tiene un vuelo asignado.";
		} else {
			return "Nombre: " + nombre + ".\nCedula: " + cedula + "\nEdad: " + edad + "\nSexo: " + sexo + ".\nCargo: "
					+ cargo + ".\nSueldo: " + sueldo + "$.\nVuelo: " + vuelo.toString();
		}
	}

	public String imprimirLista(){
		return "Nombre: " + nombre + " Cedula: " + cedula + " Cargo: " + cargo + " anios de experiencia: " + experiencia;
	}

	/*
	 * Retorna el empleado con el numero de cedula que se pasa por parametro
	 */
	public static Empleado buscarEmpleado(int cedula) {
		for (Empleado empleado : aeropuerto.getEmpleados()) {
			if (empleado.getCedula() == cedula) {
				return empleado;
			}
		}
		return null;
	}

	public int getSueldo() {
		return sueldo;
	}

	public void setSueldo(int sueldo) {
		this.sueldo = sueldo;
	}

	public String getCargo() {
		return cargo;
	}

	public void setCargo(Cargos cargo) {
		this.cargo = cargo.getCargo();
	}

	public Vuelo getVuelo() {
		return vuelo;
	}

	public void setVuelo(Vuelo vuelo) {
		this.vuelo = vuelo;
		this.vuelo.getEmpleados().add(this);
	}

	public void setExperiencia(int experiencia) {
		this.experiencia = experiencia;
	}

	public int getExperiencia() {
		return experiencia;
	}

	// Metodo de instancia que paga la nomina al empleado
	public int pagoNomina(Aeropuerto aeropuerto) {
		int dineroapagar = this.getSueldo();
		float nuevosaldo = aeropuerto.getDinero() - dineroapagar;

		if (nuevosaldo < 0) {
			return -1;
		} else {
			// Aeropuerto.setDinero(nuevosaldo);
			aeropuerto.transaccion("Nomina " + this.getNombre(), dineroapagar * (-1));
			return dineroapagar;
		}
	}
}
