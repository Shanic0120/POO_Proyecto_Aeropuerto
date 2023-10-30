// Autores: Juan Camilo Molina Roncancio
/*
 * Esta clase agrupa las caracteristicas de un equipaje (peso y propietario), se usa principalmente
 * para asignarlo a determinado pasajero.
 */
package gestorAplicacion.gestionVuelos;

import java.io.Serializable;

import gestorAplicacion.gestionHumana.Pasajero;

public class Equipaje implements Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private double peso;
	private Pasajero propietario;

	public Equipaje(double peso, Pasajero propietario) {
		this.peso = peso;
		this.propietario = propietario;
	}

	public double getPeso() {
		return peso;
	}

	public void setPeso(double peso) {
		this.peso = peso;
	}

	public Pasajero getPropietario() {
		return propietario;
	}

	public void setPropietario(Pasajero propietario) {
		this.propietario = propietario;
	}
}
