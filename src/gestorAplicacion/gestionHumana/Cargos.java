// Autores: Juan Jose Zapata Cadavid, Juan Camilo Molina Roncancio
/*
 * Cargos asociados a la clase Empleado, junto con su sueldo base
 */
package gestorAplicacion.gestionHumana;

public enum Cargos {
	AZAFATA("Azafata", 1000), CONTROL_DE_PISTA("Control de pista", 1500), PILOTO("Piloto", 2000),
	COPILOTO("Copiloto", 1800);

	private String cargo;
	private int sueldoBase;

	Cargos(String cargo, int sueldoBase) {
		this.cargo = cargo;
		this.sueldoBase = sueldoBase;
	}

	public String getCargo() {
		return cargo;
	}

	public int getSueldoBase() {
		return sueldoBase;
	}

}
