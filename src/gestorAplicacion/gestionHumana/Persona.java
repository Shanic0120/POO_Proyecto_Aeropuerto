// Autores: Juan Jose Zapata Cadavid, Juan Camilo Molina Roncancio
/*
 * Clase abstracta para implementar informacion y metodos comunes en Pasajero y Empleado
 */
package gestorAplicacion.gestionHumana;

import java.io.Serializable;

import gestorAplicacion.gestionVuelos.Aeropuerto;

public abstract class Persona implements Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	protected String nombre;
	protected final int cedula;
	protected int edad;
	protected String sexo;
	protected static Aeropuerto aeropuerto;

	public Persona(String nombre, int cedula, int edad, String sexo) {
		this.nombre = nombre;
		this.cedula = cedula;
		this.edad = edad;
		this.sexo = sexo;
	}

	public static void setAeropuerto(Aeropuerto aeropuerto) {
		Persona.aeropuerto = aeropuerto;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getEdad() {
		return edad;
	}

	public void setEdad(int edad) {
		this.edad = edad;
	}

	public String getSexo() {
		return sexo;
	}

	public void setSexo(String sexo) {
		this.sexo = sexo;
	}

	public int getCedula() {
		return this.cedula;
	}

	public abstract String toString();

	public String imprimirLista(){
		return "Nombre: " + nombre + " Cedula: " + cedula;
	};
}
