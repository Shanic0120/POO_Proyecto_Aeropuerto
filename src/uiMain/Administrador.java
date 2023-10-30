// Autores: Juan Jose Zapata Cadavid, Maria Camila Zapata Arrubla, Juan Camilo Molina Roncancio
/* Esta clase sera la encargada de la interaccion entre el sistema y el administrador
 * del aeropuerto, en ella se haran todos los prints e inputs necesarios para esto.
 * A su vez hay varios metodos que comunican los objetos de los demas paquetes entre si.
 */

package uiMain;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import basedatos.Serializador;
import gestorAplicacion.gestionHumana.Cargos;
import gestorAplicacion.gestionHumana.Empleado;
import gestorAplicacion.gestionHumana.Pasajero;
import gestorAplicacion.gestionHumana.Persona;
import gestorAplicacion.gestionVuelos.Aeropuerto;
import gestorAplicacion.gestionVuelos.Asiento;
import gestorAplicacion.gestionVuelos.Avion;
import gestorAplicacion.gestionVuelos.Equipaje;
import gestorAplicacion.gestionVuelos.Vuelo;
import gestorAplicacion.gestionVuelos.zonasEmbarque;

public class Administrador {
	public static final Aeropuerto AEROPUERTO = new Aeropuerto();

	public static void main(String[] args) {

		inicializarStatics();
		// inicializadorObjetos();
		Scanner entrada = new Scanner(System.in);
		System.out.println("\n-- Bienvenido al sistema de administracion de Vuelos --");

		opcionesPrincipales();
	}

	/*
	 * Imprime dos columnas con la cedula y el nombre de los empleados asociados al
	 * aeropuerto
	 */
	public static void mostrarEmpleados() {
		System.out.println("Estos son los empleados del aeropuerto:\n");
		System.out.println("Cedula         Nombre");
		for (Empleado empleado : AEROPUERTO.getEmpleados()) {
			System.out.println(empleado.getCedula() + " ".repeat(15 - Integer.toString(empleado.getCedula()).length())
					+ empleado.getNombre());
		}
	}

	/*
	 * Da ciertos valores iniciales al aeropuerto y a sus objetos para tener ya
	 * guardados ciertos datos
	 */
	public static void inicializadorObjetos() {
		Vuelo vuelo1 = new Vuelo(new Avion("X", 100, 30000), LocalDateTime.now(), "Bogota", 2000, "1A");
		Vuelo vuelo2 = new Vuelo(new Avion("A", 50, 10000), LocalDateTime.now(), "Miami", 1500, "1B");
		Vuelo vuelo3 = new Vuelo(new Avion("X35", 150, 45000), LocalDateTime.now(), "Barranquilla", 2500, "2C");
		Vuelo vuelo4 = new Vuelo(new Avion("Y3", 65, 20000), LocalDateTime.now(), "Cucuta", 1700, "3C");

		List<Equipaje> equipaje = new ArrayList<>();
		Pasajero pasajero1 = new Pasajero("Pepito", 897915, 68, "M", 0);
		Pasajero pasajero2 = new Pasajero("Camilo", 345364, 70, "M", 0);
		Pasajero pasajero3 = new Pasajero("Carlos", 343543, 89, "M", 0);
		Pasajero pasajero4 = new Pasajero("Juan", 785234, 26, "M", 0);
		Pasajero pasajero5 = new Pasajero("Pedro", 53746, 35, "M", 0);
		Pasajero pasajero6 = new Pasajero("Sara", 43786, 67, "F", 0);
		Pasajero pasajero7 = new Pasajero("Camila", 34387, 39, "F", 0);
		Pasajero pasajero8 = new Pasajero("Carla", 0752375, 21, "F", 0);
		Pasajero pasajero9 = new Pasajero("Maria", 575207, 8, "F", 0);
		Pasajero pasajero10 = new Pasajero("Manuela", 397357, 17, "F", 0);
		Pasajero pasajero11 = new Pasajero("Juanita", 7873087, 19, "F", 0);
		Pasajero pasajero12 = new Pasajero("Carmen", 786930, 30, "F", 0);

		for (Pasajero pasajero : AEROPUERTO.getPasajeros()) {
			equipaje = new ArrayList<>();
			equipaje.add(new Equipaje(Math.random() * 10, pasajero));
			pasajero.setEquipajes(equipaje);
		}

		for (int i = 0; i < AEROPUERTO.getPasajeros().size(); i++) {
			if (i <= 3) {
				vuelo1.agregarPasajero(AEROPUERTO.getPasajeros().get(i), i + 1);
			} else if (i <= 6) {
				vuelo2.agregarPasajero(AEROPUERTO.getPasajeros().get(i), i);
			} else if (i <= 9) {
				vuelo3.agregarPasajero(AEROPUERTO.getPasajeros().get(i), i);
			} else {
				vuelo4.agregarPasajero(AEROPUERTO.getPasajeros().get(i), i);
			}
		}

		AEROPUERTO.setDinero((long) Math.pow(10, 7));
		Empleado e1 = new Empleado("Juan Carlos", 1200000, 10023031, Cargos.PILOTO, 45, "M", 10);
		Empleado e2 = new Empleado("Felipe", 900000, 4553031, Cargos.COPILOTO, 37, "M", 4);
		Empleado e3 = new Empleado("Andrea", 456174, Cargos.AZAFATA, 31, "F");
		Empleado e4 = new Empleado("Sara", 1841587, Cargos.COPILOTO, 38, "F");
		Empleado e5 = new Empleado("Sofia", 123456, Cargos.PILOTO, 48, "F");

		e4.setVuelo(vuelo1);
		e5.setVuelo(vuelo2);
		e3.setVuelo(vuelo2);
		e1.setVuelo(vuelo3);
		e2.setVuelo(vuelo1);

		Serializador.serializar(AEROPUERTO);
	}

	/*
	 * Da a ciertas clases el valor del AEROPUERTO para el funcionamiento correcto
	 * de estas
	 */
	public static void inicializarStatics() {
		Avion.setAeropuerto(AEROPUERTO);
		Persona.setAeropuerto(AEROPUERTO);
		Vuelo.setAeropuerto(AEROPUERTO);
	}

	/*
	 * Menu principal donde estan las 5 funcionalidades principales
	 */
	public static void opcionesPrincipales() {
		Scanner entrada = new Scanner(System.in);
		int option = 0;

		System.out.println("\nIngrese el numero de la opcion a elegir:");
		System.out.print("1. Reserva de vuelo.\n" + "2. Programar nuevos vuelos.\n" + "3. Gestionar empleados.\n"
				+ "4. Administrar finanzas.\n" + "5. Administrar vuelos y aviones.\n\n"
				+ "0. Pulse para finalizar el programa.\n");
		option = entrada.nextInt();
		switch (option) {
		case 1:
			reservaDeVuelo();
			break;
		case 2:
			programarVuelos();
			break;
		case 3:
			gestionarEmpleadosInterfaz();
			break;
		case 4:
			interfazFinanzas();
			break;
		case 5:
			Modificaciones();
			break;
		case 0:
			salirDelSistema();
			break;
		default:
			System.out.println("Opcion incorrecta, vuelva a intentarlo.");
			opcionesPrincipales();
		}
	}

	/*
	 * Con este metodo que no recibe nada como parametro se despliega el menu para la creacion de nuevos
	 * vuelos, con elementos como avion, fecha (la cual se parsea con la libreria LocalDateTime, destino entre otros elementos.
	 * Ademas se implementa un pequeno sistema de recomendacion de empleados para el vuelo segun las caracteristicas del mismo.
	 */
	public static void programarVuelos() {
		Scanner entrada = new Scanner(System.in);
		try {
			for (Avion avion : AEROPUERTO.getAviones())
				System.out.println(avion);
			System.out.print("\nIngrese el ID del avion designado para el vuelo: ");
			int id = entrada.nextInt();
			System.out.print("Ingrese la fecha y hora del vuelo (en formato DD/MM/AAAA HH:MM:SS): ");
			entrada.nextLine();
			String str = entrada.nextLine();

			LocalDateTime fechaVuelo = LocalDateTime.parse(str, DateTimeFormatter.ofPattern("d/M/yyyy H:m:s"));

			for (Vuelo vuelo : AEROPUERTO.getVuelos()) {
				if (vuelo.getAvion().getId() == id && vuelo.getFecha().getDayOfMonth() == fechaVuelo.getDayOfMonth()
						&& vuelo.getFecha().getYear() == fechaVuelo.getYear()
						&& vuelo.getFecha().getMonth() == fechaVuelo.getMonth()) {
					System.out.println("El avion ya ha sido programado en un vuelo en esa fecha, intente en otra.");
					programarVuelos();
					return;
				}
			}

			System.out.print("Ingrese el destino del vuelo: ");
			String destino = entrada.nextLine();
			System.out.print("Ingrese el costo por pasajero del vuelo: ");
			int costo = entrada.nextInt();
			System.out.print("Ingrese la sala de embarque del vuelo, las disponibles son las siguientes: ");
			System.out.println(zonasEmbarque.mostrarZonas());
			entrada.nextLine();
			String salaEmb = entrada.nextLine();

			if (!Aeropuerto.conjunto.contains(salaEmb)) {
				System.out.println("Por favor ingrese una sala de embarque valida.");
				programarVuelos();
				return;
			}

			System.out.print("El vuelo es internacional? (y/n): ");
			String internacional = entrada.nextLine();

			for (Avion avion : AEROPUERTO.getAviones()) {
				if (avion.getId() == id) {
					Vuelo vueloNuevo = new Vuelo(avion, fechaVuelo, destino, costo, salaEmb);
				}
			}

			System.out.println("El vuelo ha sido creado exitosamente.\n");
			System.out.println("Se recomiendan los siguiente empleados segun las caracteristicas del vuelo: ");

			boolean hayEmpleados = false;
			if (internacional.equals("y")) {
				for (Persona empleado : AEROPUERTO.getEmpleados()) {
					if (((Empleado)empleado).getExperiencia() >= 5) {
						System.out.println(empleado.imprimirLista());
						hayEmpleados = true;
					}
				}
				if (!hayEmpleados)
					System.out.println("por el momento se considera que no hay personal calificado para el vuelo.");
			} else {
				System.out.println("Cualquier empleado puede cumplir las expectativas de calidad.");
			}
			System.out
					.print("\nPara la asignacion de los empleados por favor ingrese al menu de gestion de empleados.\n"
							+ "Ingrese 1 para ir a la opcion de gestion de empleados o 0 para regresar al menu principal: ");

			int des = entrada.nextInt();

			if (des == 1)
				gestionarEmpleadosInterfaz();
			else
				opcionesPrincipales();

		} catch (Exception e) {
			System.out.println("\nHa ocurrido un error, intentelo nuevamente.");
			programarVuelos();
		}
	}

	/*
	 * Interfaz principal de la funcionalidad 3. En este metodo se muestran y
	 * gestionan los empleados del aeropuerto.
	 */
	public static void gestionarEmpleadosInterfaz() {
		mostrarEmpleados();
		System.out.println("Introduzca la cedula para ver mas opciones:");
		System.out.println("0. Volver");
		Scanner entrada = new Scanner(System.in);
		int cedula = entrada.nextInt();
		if (cedula == 0) {
			opcionesPrincipales();
		}
		while (Empleado.buscarEmpleado(cedula) == null) {
			cedula = entrada.nextInt();
			if (cedula == 0) {
				opcionesPrincipales();
				break;
			}
			System.out.println("Esta cedula no esta asignada a ningun empleado, vuelva a intentarlo.");
		}
		Empleado empleadoActual = Empleado.buscarEmpleado(cedula);
		System.out.println(empleadoActual);
		opcionesEmpleado(empleadoActual);
	}

	/*
	 * Muestra y permite seleccionar las opciones posibles a realizar con el
	 * empleado pasado por parametro
	 */
	private static void opcionesEmpleado(Empleado empleadoActual) {
		Scanner entrada = new Scanner(System.in);

		System.out.println(
				"Seleccione la accion que quiere realizar:\n0. Volver.\n1. Cambiar cargo.\n2. Cambiar sueldo.\n3. Asignar vuelo.\n4. Despedir.");
		int option = entrada.nextInt();
		switch (option) {
		case 0:
			gestionarEmpleadosInterfaz();
			break;
		case 1:
			cambiarCargo(empleadoActual);
			break;
		case 2:
			cambiarSueldo(empleadoActual);
			break;
		case 3:
			asignarVuelo(empleadoActual);
			break;
		case 4:
			AEROPUERTO.despedirEmpleado(empleadoActual);
			System.out.println(empleadoActual.getNombre() + " ha sido despedido.");
			break;
		default:
			System.out.println("Opcion erronea, vuelva a intentarlo.");
			opcionesEmpleado(empleadoActual);
		}
		opcionesPrincipales();
	}

	/*
	 * Aumenta o disminuye el sueldo del empleado pasado por parametro
	 */
	public static void cambiarSueldo(Empleado empleado) {
		System.out.println("El sueldo actual de " + empleado.getNombre() + " es " + empleado.getSueldo());
		System.out.println(
				"Ingrese el valor a aumentar o disminuir, en caso de disminuir coloca que un - antes del valor: ");
		System.out.println("0. Volver.");
		Scanner entrada = new Scanner(System.in);
		int valor = entrada.nextInt();
		if (valor == 0) {
			opcionesEmpleado(empleado);
		} else if (valor < 0 && Math.abs(valor) >= empleado.getSueldo()) {
			System.out.println("Reduccion de sueldo invalida, intente nuevamente.");
			cambiarSueldo(empleado);
		}
		empleado.setSueldo(empleado.getSueldo() + valor);
		System.out.println("El nuevo sueldo de " + empleado.getNombre() + " es " + empleado.getSueldo());
		opcionesPrincipales();
	}

	/*
	 * Recibe como parametro un empleado, al cual se le asigna un vuelo determinado.
	 */
	public static void asignarVuelo(Empleado empleado) {

		if (empleado.getVuelo() == null) {
			System.out.println("Este empleado no tiene vuelo asignado");
		} else {
			System.out.println("El vuelo de este empleado es:\n" + empleado.getVuelo());
		}
		System.out.println("Seleccione el ID del vuelo al que quiere asignar al empleado: ");

		for (Vuelo vuelo : AEROPUERTO.getVuelos()) {
			if (vuelo != empleado.getVuelo()) {
				System.out.println(vuelo);
			}
		}
		System.out.println("0. Volver.");
		Scanner entrada = new Scanner(System.in);
		int idVuelo = entrada.nextInt();
		if (idVuelo == 0) {
			opcionesEmpleado(empleado);
		}
		if (Vuelo.encontrarVuelo(idVuelo) == null) {
			System.out.println("ID invalido, vuelva a intentarlo.\n");
			asignarVuelo(empleado);
		} else {
			empleado.setVuelo(Vuelo.encontrarVuelo(idVuelo));
			System.out.println("Ahora el vuelo del empleado es:\n" + empleado.getVuelo());
			System.out.println("Los empleados de este vuelo son:\n");
			for (Empleado empleado2 : empleado.getVuelo().getEmpleados()) {
				System.out.println(empleado2);
			}
			System.out.println("Verifique manualmente que el vuelo solo tenga un piloto y un copiloto.");
			opcionesPrincipales();
		}
	}

	/*
	 * Ejecuta la interfaz para cambiar el cargo del empleado que entra por
	 * parametro
	 */
	public static void cambiarCargo(Empleado empleado) {

		System.out.println("El cargo actual de " + empleado.getNombre() + " es " + empleado.getCargo());
		System.out.println("A que cargo quieres asignarle? Los cargos disponibles son: ");

		for (int i = 0; i < Cargos.values().length; i++) {
			System.out.println((i + 1) + ". " + Cargos.values()[i].getCargo());
		}
		Scanner entrada = new Scanner(System.in);
		System.out.println("Ingrese el indice del cargo a elegir: ");
		int indice = entrada.nextInt();
		if (indice == 0) {
			opcionesEmpleado(empleado);
		}
		if (indice <= Cargos.values().length) {
			if (Cargos.values()[indice - 1].getCargo().equals(empleado.getCargo())) {
				System.out.println(empleado.getNombre() + " ya era " + empleado.getCargo());
			} else {
				empleado.setCargo(Cargos.values()[indice - 1]);
				System.out.println("Ahora el cargo de " + empleado.getNombre() + " es " + empleado.getCargo());
				System.out.println("¿Desea cambiar el saldo de " + empleado.getNombre() + "?\n1. Si.\n2. No\n");
				int opcion = entrada.nextInt();
				switch (opcion) {
				case 1: {
					cambiarSueldo(empleado);
					break;

				}
				case 2: {
					System.out.println("Saliendo al menu principal.");
					opcionesPrincipales();
					break;
				}
				default:
					System.out.println("Opcion erronea, saliendo al menu principal.");
					opcionesPrincipales();
					break;
				}
			}

		} else {
			System.out.println("Valor erroneo, vuelva a intentarlo.");
			cambiarCargo(empleado);
		}
		opcionesPrincipales();
	}

	/*
	 * Guarda el objeto aeropuerto, donde estan todos los valores necesarios para
	 * una siguiente ejecucion, y sale del sistema
	 */
	public static void salirDelSistema() {
		System.out.println("Vuelva pronto");
		Serializador.serializar(AEROPUERTO);
		System.exit(0);
	}

	/*
	 * Es el metodo principal de la funcionalidad de reservas de vuelos, dado un destino
	 * indicado por el usuario se hace la busqueda de los posibles vuelos, se piden todos los
	 * datos para la creacion de los objetos necesarios.
	 */
	public static void reservaDeVuelo() {
		Scanner entradas = new Scanner(System.in);
		System.out.print("Por favor inserte la ciudad de destino: \n0. Volver.\n");
		for (Vuelo vuelo : AEROPUERTO.getVuelos()) {
			System.out.println(vuelo.getDestino());
		}
		String entradaDestino = entradas.nextLine();
		if (entradaDestino.equals("0")) {
			opcionesPrincipales();
		}

		List<Vuelo> vuelosDisp = new ArrayList<>();
		for (Vuelo vuelo : AEROPUERTO.getVuelos()) {
			if (vuelo.getDestino().equals(entradaDestino) && !vuelo.isEnVuelo()) {
				vuelosDisp.add(vuelo);
			}
		}

		if (!vuelosDisp.isEmpty())
			for (Vuelo vuelo : vuelosDisp)
				System.out.print(vuelo);
		else {
			System.out.println("Lo sentimos, no hay vuelos disponibles desde Medellin para el destino indicado");
			opcionesPrincipales();
		}
		System.out.print("Inserte el ID del vuelo de su preferencia: ");
		int IDvuelo = entradas.nextInt();

		Vuelo vueloElegido = null;
		for (Vuelo vuelo : vuelosDisp)
			if (vuelo.getId() == IDvuelo)
				vueloElegido = vuelo;

		System.out.println("\nFormulario de datos personales");

		System.out.print("Inserte su nombre: ");
		entradas.nextLine();
		String nombre = entradas.nextLine();
		System.out.print("Inserte su documento de identidad: ");
		int documento = entradas.nextInt();
		System.out.print("Inserte su edad: ");
		int edad = entradas.nextInt();
		System.out.print("Inserte su genero: ");
		entradas.nextLine();
		String sexo = entradas.nextLine();
		System.out.print("Inserte la cantidad de equipajes que transporta: ");
		int nroEquipajes = entradas.nextInt();
		List<Equipaje> equipajes = new ArrayList<>();
		Pasajero nuevoPasajero = new Pasajero(nombre, documento, edad, sexo, 0);

		for (int i = 1; i <= nroEquipajes; i++) {
			System.out.print("Inserte el peso del equipaje " + i + ": ");
			double peso = entradas.nextDouble();
			equipajes.add(new Equipaje(peso, nuevoPasajero));
		}
		nuevoPasajero.setEquipajes(equipajes);
		System.out.println("\nLos asientos disponibles en el vuelo son los siguientes: ");
		for (Asiento asiento : vueloElegido.getAvion().getAsientos()) {
			if (!asiento.isOcupado())
				System.out.println(asiento);
		}

		System.out.print("\nIngrese el numero de asiento de su preferencia: ");
		int nroAsiento = entradas.nextInt();
		if (vueloElegido.agregarPasajero(nuevoPasajero, nroAsiento)) {
			System.out.println(vueloElegido.tiquete(nuevoPasajero)); // Imprime el tiquete
		} else {
			vueloElegido.getPasajeros().remove(nuevoPasajero); // Por si no se hace efectiva la reserva dado el peso del
																// equipaje
			AEROPUERTO.getPasajeros().remove(nuevoPasajero);
			System.out.println(
					"\nNo queda espacio suficiente en este vuelo para su equipaje o ha elegido un asiento no disponible, "
							+ "por favor elija otro vuelo (o asiento) o reduzca el peso.");
		}

		int option;
		do {
			System.out.println("\nIngrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Volver.
					2. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				opcionesPrincipales();
			case 2:
				salirDelSistema();
				break;
			}
		} while (option != 3);
	}

	/*
	 * Interfaz de el sistema de administracion de finanzas para que el usuario
	 * pueda: -pagar la nomina de los empleados -ver el historial de transacciones
	 * -modificar el sueldo de los empleados (tambien se puede realizar en el menu
	 * de gestionar empleados) -crear un nuevo empleado -
	 */
	public static void interfazFinanzas() {
		Scanner entrada = new Scanner(System.in);
		System.out.println("\n-- Bienvenido al sistema de administracion de Finanzas --");
		System.out.println("Saldo actual = " + AEROPUERTO.getDinero());

		int option;
		System.out.println("\nIngrese el numero de la opcion a elegir:");
		System.out.print("""
				1. Pagar Nomina de empleados.
				2. ver historial de transacciones.
				3. Contratar nuevo empleado.
				4. Modificar el dinero del aeropuerto
				5. Volver.
				0. Cerrar.
				""");

		option = entrada.nextInt();
		switch (option) {
		case 1:
			pagarNominaInterfaz();
			break;
		case 2:
			System.out.println(AEROPUERTO.transacciones());
			interfazFinanzas();
			break;
		case 3:
			nuevoEmpleado();
			interfazFinanzas();
			break;
		case 4:
			modificarDinero();
			interfazFinanzas();
			break;
		case 5:
			opcionesPrincipales();
			break;
		case 0:
			salirDelSistema();
			break;
		default:
			System.out.println("Opcion incorrecta, vuelva a intentarlo.");
		}
	}

	/*
	 * Interfaz de pago de nomina para que el usuario pueda: -pagar la nomina de
	 * todos los empleados -elegir empleados uno a uno para pagarles nomina -
	 */
	public static void pagarNominaInterfaz() {
		int dineroapagar = 0;
		List<Empleado> lempleados = AEROPUERTO.getEmpleados();
		Scanner entrada = new Scanner(System.in);
		System.out.println("\n-- Bienvenido al sistema de pago de nomina --");

		int option;
		int option2;
		System.out.println("\nDesea pagarle a todos los empleados?");
		System.out.print("""
				1. Pagar a todos los empleados
				2. Elegir empleados
				3. Finalizar y Volver.
				""");

		option = entrada.nextInt();

		if (option == 1) {
			pagarNominaGeneral(lempleados);
			pagarNominaInterfaz();
		} else if (option == 2) {
			System.out.println("\nListado de empleados");
			for (int i = 0; i < lempleados.size(); i++) {
				System.out.println((i + 1) + ". " + lempleados.get(i).getCargo() + ": " + lempleados.get(i).getNombre()
						+ ", sueldo = " + lempleados.get(i).getSueldo());
			}
			System.out.println("Selecciona el numero del empleado a pagar o pulsa 0 para volver:");
			option2 = entrada.nextInt();

			if (option2 == 0) {
				// pass
			} else if (option2 < 1 || option2 > lempleados.size()) {
				System.out.println("Error: numero incorrecto");
			} else {
				dineroapagar = lempleados.get(option2 - 1).pagoNomina(AEROPUERTO);
				if (dineroapagar < 0) {
					System.out.println("No se ha podido realizar la transaccion: no tienes suficiente dinero");
				} else {
					// Aeropuerto.setDinero(nuevosaldo);
					System.out.println("Transaccion realizada, nuevo saldo = " + AEROPUERTO.getDinero());
				}
			}
			pagarNominaInterfaz();

		} else if (option == 3) {
			interfazFinanzas();
		} else {
			System.out.println("Opcion incorrecta, vuelva a intentarlo.");
			pagarNominaInterfaz();
		}
	}

	// metodo para pagar la nomina a un listado de empleados
	public static void pagarNominaGeneral(List<Empleado> empleados) {
		int dineroapagar = 0;
		for (Empleado empleado : empleados) {
			dineroapagar += empleado.getSueldo();
		}
		float nuevosaldo = AEROPUERTO.getDinero() - dineroapagar;

		if (nuevosaldo < 0) {
			System.out.println("No se ha podido realizar la transaccion: no tienes suficiente dinero");
		} else {
			AEROPUERTO.transaccion("Nomina General", dineroapagar * (-1));
			// Aeropuerto.setDinero(nuevosaldo);
			System.out.println("Transaccion realizada, nuevo saldo = " + AEROPUERTO.getDinero());
		}
	}

	// metodo para ingresar o retirar dinero al aeropuerto
	public static void modificarDinero() {
		Scanner entrada = new Scanner(System.in);
		System.out.println("\n-- Bienvenido al sistema de transacciones externas --");
		System.out.println("Desea ingresar o retirar dinero?");
		System.out.println("1. Ingresar\n2. Retirar\n0. Volver");
		int option = entrada.nextInt();

		if (option == 0) {
			interfazFinanzas();
			return;
		} else if (option != 1 && option != 2) {
			System.out.println("numero incorrecto, vuelve a intentar");
			modificarDinero();
			return;
		}

		System.out.println("Ingrese el valor de la transaccion: ");
		int monto = entrada.nextInt();

		System.out.println("Ingrese el cocepto de la transaccion (Breve descripcion):");
		entrada.nextLine();
		String cocepto = entrada.nextLine();

		switch (option) {
		case 1:
			AEROPUERTO.transaccion(cocepto, monto);
			System.out.println("Se ha ingresado exitosamente el monto de " + monto);
			break;
		case 2:
			if (AEROPUERTO.getDinero() - monto >= 0) {
				AEROPUERTO.transaccion(cocepto, monto * (-1));
				System.out.println("Se ha retirado exitosamente el monto de " + monto);
			} else {
				System.out.println("Fondos insuficientes, no se ha podido realizar la transaccion");
			}
			break;
		}
		System.out.println("Nuevo saldo = " + AEROPUERTO.getDinero());
	}

	// metodo para crear (contratar) un nuevo empleado
	// el metodo retorna el nuevo empleado aunque no es necesario asignar este
	// retorno
	public static void nuevoEmpleado() {
		String nombret;
		int cedulat;
		Cargos cargot;
		int edadt;
		String sexot;
		int sueldot;

		Scanner entrada = new Scanner(System.in);
		System.out.println("---NUEVO EMPLEADO---");
		System.out.print("Por favor inserte el nombre del empleado: ");
		nombret = entrada.nextLine();
		System.out.print("Por favor elija el cargo del empleado:\n");
		cargot = elegirCargo();
		System.out.print("Por favor inserte el sexo del empleado, (M) para hombres y (F) para mujeres: ");
		sexot = entrada.nextLine();

		System.out.print("Por favor inserte la edad del empleado: ");
		edadt = entrada.nextInt();
		System.out.print("Por favor inserte el sueldo del empleado: \n(Inserte 0 si desea asignarle el precio base): ");
		sueldot = entrada.nextInt();

		int cedula = pedirCedula();
		if (sueldot == 0) {
			sueldot = cargot.getSueldoBase();
		}
		System.out.println("Se ha agragado al empleado " + nombret);
		new Empleado(nombret, sueldot, cedula, cargot, edadt, sexot, 0);
	}

	public static int pedirCedula() {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Por favor inserte la cedula del empleado: ");
		int c = entrada.nextInt();
		for (Empleado empleado : AEROPUERTO.getEmpleados()) {
			if (c == empleado.getCedula()) {
				return pedirCedula();
			}
		}
		return c;

	}

	// Metodo usado al crear un empleado para elegir uno de los cargos disponibles
	public static Cargos elegirCargo() {
		for (int i = 0; i < Cargos.values().length; i++) {
			System.out.println((i + 1) + ". " + Cargos.values()[i].getCargo());
		}
		Scanner entrada = new Scanner(System.in);
		System.out.println("Ingrese el indice del cargo a elegir: ");
		int indice = entrada.nextInt();
		if (indice <= Cargos.values().length) {
			return Cargos.values()[indice - 1];
		} else {
			System.out.println("Valor erroneo, vuelva a intentarlo.");
			return elegirCargo();
		}
	}

	/*
	 * Metodo mostrarPasajeros Permite ver los pasajeros activos en el aeropuerto.
	 */
	public static void mostrarPasajeros() {
		System.out.println("Estos son los pasajeros del aeropuerto:\n");
		System.out.println("Cedula         Nombre");
		for (Persona pasajero : AEROPUERTO.getPasajeros()) {
			System.out.println(pasajero.imprimirLista());
		}
	}

	/*
	 * Metodo mostrarVuelos Permite ver los vuelos disponibles en el aeropuerto.
	 */
	public static void mostrarVuelos() {
		System.out.println("El aeropuerto dispone de los siguientes vuelos: \n");
		System.out.println("ID             Destino");
		for (Vuelo vuelo : AEROPUERTO.getVuelos()) {
			System.out.println(
					vuelo.getId() + " ".repeat(15 - Integer.toString(vuelo.getId()).length()) + vuelo.getDestino());
		}
	}

	/*
	 * Metodo mostrarAviones Permite ver los aviones disponibles del aeropuerto.
	 */
	public static void mostrarAviones() {
		System.out.println("El aeropuerto dispone de los siguientes aviones: \n");
		System.out.println("ID             Modelo");
		for (Avion avion : AEROPUERTO.getAviones()) {
			System.out.println(
					avion.getId() + " ".repeat(15 - Integer.toString(avion.getId()).length()) + avion.getModelo());
		}
	}

	/*
	 * Funcionalidad Modificaciones Esta funcionalidad permite las opciones de
	 * cambiar asiento, cancelar un vuelo y eliminar un avion. En cada opcion
	 * contiene su respectivo metodo
	 */
	public static void Modificaciones() {
		Scanner entrada = new Scanner(System.in);
		System.out.println("\n-- Bienvenido al sistema de administracion de vuelos y aviones --");

		int option;

		System.out.println("\nIngrese el numero de la opcion a elegir:");
		System.out.print("""
				1. Cambiar asiento.
				2. Cancelar vuelo.
				3. Eliminar avion.
				4. Ingresar nuevo avion.
				5. Volver.
				6. Finalizar.
				""");

		option = entrada.nextInt();
		switch (option) {
		case 1:
			cambiarAsiento();
			break;
		case 2:
			cancelarVuelo();
			break;
		case 3:
			eliminarAvion();
			break;
		case 4:
			int idMax = 0;

			for (int l = 0; l < AEROPUERTO.getAviones().size(); l++) {
				if (AEROPUERTO.getAviones().get(l).getId() > idMax) {
					idMax = AEROPUERTO.getAviones().get(l).getId();
				}
			}

			comprarAvion(idMax);
		case 5:
			opcionesPrincipales();
			break;
		case 6:
			salirDelSistema();
			break;
		}

	}

	/*
	 * Metodo cambiarAsiento Permite al pasajero cambiar su asiento una vez ya ha
	 * reservado vuelo. En este se piden los datos del pasajero para verificar que
	 * se encuentre registrado y hacer el debido proceso. Si el pasajero no esta
	 * registrado se mostrara un mensaje. Si el pasajero esta registrado se
	 * realizara el proceso de reversa de vuelo. Para lo anterior se creo el metodo
	 * reservaDeVuelo2()
	 */
	private static void cambiarAsiento() {
		mostrarPasajeros();
		Scanner entradas = new Scanner(System.in);
		System.out.println("Ingrese su documento de identidad.");
		int documento = entradas.nextInt();
		Persona pasajero = Pasajero.buscarPasajero(documento); // Verifica si el pasajero se encuentra registrado
		if (pasajero == null) {
			System.out.println("El usuario no se encuentra registrado.\n");
			int option;
			do {
				System.out.println("\nIngrese el numero de la opcion a elegir:");
				System.out.print("""
						1. Intentar de nuevo.
						2. Volver.
						3. Finalizar.
						""");

				option = entradas.nextInt();
				switch (option) {
				case 1:
					cambiarAsiento();
					break;
				case 2:
					opcionesPrincipales();
					break;
				case 3:
					salirDelSistema();
					break;
				}
			} while (option != 4);

		} else {
			((Pasajero) pasajero).getAsiento().setOcupado(false); // Se habilita el asiento que tenia el pasajero
			reservaDeVuelo2((Pasajero)pasajero); // Proceso de reserva de vuelo, es diferente a la primera reserva que se hace
		}
	}

	/*
	 * Metodo reservaDeVuelo2 El metodo recibe como parametros un pasajero. Este
	 * metodo permite hacer el cambio de asiento conservando los datos ingresados en
	 * la primera reserva que se hizo, por lo que no es necesario volver a pedirlos
	 * en esta ocasion. En caso de que el costo del asiento sea mayor al pagado en
	 * la primera reserva se pide un excedente, en caso contrario se devuelve el
	 * dinero
	 */
	public static void reservaDeVuelo2(Pasajero pasajero) {
		int valorInicial = pasajero.getInversion();
		Scanner entradas = new Scanner(System.in);

		System.out.println("\nLos asientos disponibles en el vuelo son los siguientes: ");
		for (Asiento asiento : pasajero.getVuelo().getAvion().getAsientos()) {
			if (!asiento.isOcupado())
				System.out.println(asiento);
		}

		System.out.print("\nIngrese el numero de asiento de su preferencia: ");
		int nroAsiento = entradas.nextInt();
		Asiento nuevoasiento = null;

		// Es para actualizar el asiento
		for (int j = 0; j < pasajero.getVuelo().getAvion().getAsientos().size(); j++) {
			if (nroAsiento == pasajero.getVuelo().getAvion().getAsientos().get(j).getNumero()) {
				pasajero.getVuelo().getAvion().getAsientos().get(j).setOcupado(true);
				nuevoasiento = pasajero.getVuelo().getAvion().getAsientos().get(j);
				pasajero.getAsiento().setNumero(nroAsiento);
				pasajero.getAsiento().setClase(pasajero.getVuelo().getAvion().getAsientos().get(j).getClase());
			}
		}
		if (nuevoasiento.getClase().equals("Primera clase")) {
			pasajero.setInversion(3 * pasajero.getVuelo().getCosto());
		} else if (nuevoasiento.getClase().equals("Ejecutiva")) {
			pasajero.setInversion(2 * pasajero.getVuelo().getCosto());
		} else {
			pasajero.setInversion(pasajero.getVuelo().getCosto());
		}
		System.out.println(pasajero.getVuelo().tiquete(pasajero));
		if (valorInicial < pasajero.getInversion()) {
			System.out.println("Por favor pagar un excedente de: " + "$" + (pasajero.getInversion() - valorInicial));
			AEROPUERTO.transaccion("Excedente cambio de asiento", pasajero.getInversion() - valorInicial); // se agrega
																											// dinero al
																											// aeropuerto
		} else {
			System.out.println("Devolucion: " + "$" + (valorInicial - pasajero.getInversion()));
			AEROPUERTO.transaccion("Devolucion cambio de asiento", valorInicial - pasajero.getInversion()); // se retira
																											// dinero
																											// del
																											// aeropuerto
		}

		int option;
		do {
			System.out.println("\nIngrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Volver.
					2. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				opcionesPrincipales();
			case 2:
				salirDelSistema();
				break;
			}
		} while (option != 3);

	}

	/*
	 * Metodo cancelarVuelo Es invocado desde el metodo Modificaciones. Se pide el
	 * ID del vuelo con el fin de revisar que del vuelo correspondiente se eliminen
	 * los pasajeros. Se mostrara los vuelos disponibles actualizados
	 */
	private static void cancelarVuelo() {
		mostrarVuelos();
		Scanner entradas = new Scanner(System.in);

		System.out.println("Por favor ingrese el ID del vuelo que desea cancelar:\n0. Volver a modificaciones.\n");
		int id = entradas.nextInt();

		if (id == 0) {
			Modificaciones();
		}
		Vuelo vueloCancelado = Vuelo.encontrarVuelo(id);

		for (Pasajero pasajero : vueloCancelado.getPasajeros()) {
			AEROPUERTO.getPasajeros().remove(pasajero);
		}

		AEROPUERTO.getVuelos().remove(vueloCancelado);

		System.out.println("\nLa lista de vuelos ha sido actualizada.\n");
		mostrarVuelos();

		int option;
		do {
			System.out.println("\nIngrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Volver.
					2. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				opcionesPrincipales();
				break;
			case 2:
				salirDelSistema();
				break;
			}
		} while (option != 3);

	}

	/*
	 * Metodo cancelarVuelo (Sobrecarga) Este metodo recibe como parametros un
	 * objeto de tipo vuelo. Es invocado por el metodo eliminarAvion. Este metodo
	 * esta pensado para que cuando se elimine el avion se pueda eliminar el vuelo
	 * el cual tenia asignado dicho avion
	 */
	private static void cancelarVuelo(Vuelo vuelo) {
		Scanner entradas = new Scanner(System.in);

		Vuelo vueloCancelado = Vuelo.encontrarVuelo(vuelo.getId());

		for (Pasajero pasajero : vueloCancelado.getPasajeros()) {
			AEROPUERTO.getPasajeros().remove(pasajero);
		}

		AEROPUERTO.getVuelos().remove(vueloCancelado);

		System.out.println("\nLa lista de vuelos ha sido actualizada.\n");
		mostrarVuelos();

		int option;
		do {
			System.out.println("\nIngrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Volver.
					2. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				opcionesPrincipales();
				break;
			case 2:
				salirDelSistema();
				break;
			}
		} while (option != 3);

	}

	/*
	 * Metodo eliminarAvion En este metodo esta la opcion de agregar otro avion al
	 * vuelo que le corresponde o eliminar el vuelo en caso que no se le asigne otro
	 * vuelo. Se crea dos variables, una de tipo vuelo y otra de tipo avion. Se pide
	 * el ID del avion que se desea eliminar, con este ID, si coincide con la lista
	 * de aviones se le asigna a la variable a, posterior a esto se elimina dicho
	 * avion de la lista. Despues se busca el respectivo vuelo del avion y se le
	 * asigna a la variable v. a y v se usan para los cambios necesarios
	 */
	private static void eliminarAvion() {
		mostrarAviones();
		Scanner entradas = new Scanner(System.in);

		System.out.println("Por favor ingrese el ID del avion que desea eliminar: ");
		int id = entradas.nextInt();
		Vuelo v = null;
		Avion a = null;
		int idMax = 0;

		// Sirve para definir el id maximo de la lista de aviones, con el fin de que los
		// proximos aviones que se agreguen
		// tengan un id diferente
		for (int l = 0; l < AEROPUERTO.getAviones().size(); l++) {
			if (AEROPUERTO.getAviones().get(l).getId() > idMax) {
				idMax = AEROPUERTO.getAviones().get(l).getId();
			}
		}

		for (int i = 0; i < AEROPUERTO.getAviones().size(); i++) {
			if (id == AEROPUERTO.getAviones().get(i).getId()) {
				a = AEROPUERTO.getAviones().get(i);
				AEROPUERTO.getAviones().remove(AEROPUERTO.getAviones().get(i));
			}
			for (int j = 0; j < AEROPUERTO.getVuelos().size(); j++) {
				if (a != null) {
					if (a.getId() == AEROPUERTO.getVuelos().get(j).getAvion().getId()) {
						v = AEROPUERTO.getVuelos().get(j);
					}
				}
			}

		}

		if (v == null) {
			System.out.println("El avion se elimino");
			int option;
			do {
				System.out.println("Ingrese el numero de la opcion a elegir:");
				System.out.print("""
						1. Volver.
						2. Finalizar.
						""");

				option = entradas.nextInt();
				switch (option) {
				case 1:
					opcionesPrincipales();
					break;
				case 2:
					salirDelSistema();
					break;
				}
			} while (option != 3);

		}

		int option;
		do {
			System.out.println("Desea agregar un avion al vuelo " + v);
			System.out.println("Ingrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Si.
					2. No.
					3. Volver.
					4. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				agregarAvion(v, idMax);
				break;
			case 2:
				cancelarVuelo(v);
				break;
			case 3:
				opcionesPrincipales();
				break;
			case 4:
				salirDelSistema();
				break;
			}
		} while (option != 5);

		System.out.println("\nLa lista de aviones ha sido actualizada.\n");
		mostrarAviones();
	}

	/*
	 * Metodo agregarAvion Recibe como parametro un objeto de tipo vuelo y otro de
	 * tipo int. Este metedo sirve para agregar un nuevo avion y este agregarlo a un
	 * vuelo. Se invoca el metodo comprarAvion
	 */
	private static void agregarAvion(Vuelo vuelo, int idMax) {
		comprarAvion(idMax);
		Scanner entradas = new Scanner(System.in);
		vuelo.setAvion(AEROPUERTO.getAviones().get(AEROPUERTO.getAviones().size() - 1));
		int option;
		do {
			System.out.println("\nSe ha agregado el avion exitosamente.\n");
			System.out.println("Ingrese el numero de la opcion a elegir:");
			System.out.print("""
					1. Volver.
					2. Finalizar.
					""");

			option = entradas.nextInt();
			switch (option) {
			case 1:
				opcionesPrincipales();
				break;
			case 2:
				salirDelSistema();
				break;
			}
		} while (option != 3);
	}

	/*
	 * Metodo comprarAvion Se pide los respectivos valores para crear un avion, como
	 * lo es el modelo, el peso y el valor. Se verifica los fondos del aeropuerto
	 * para realizar los respectivos cambios
	 */
	public static void comprarAvion(int idMax) {
		Scanner entradas = new Scanner(System.in);
		System.out.println("Por favor ingrese el modelo del avion: ");
		String modelo = entradas.nextLine();

		System.out.println("Por favor ingrese el peso maximo del avion: ");
		int peso = entradas.nextInt();

		System.out.println("Por favor ingrese el precio del avion: ");
		int valor = entradas.nextInt();

		if (valor > AEROPUERTO.getDinero()) {
			System.out.println("No hay fondos suficientes para comprar este avion, intentelo de nuevo.");
			comprarAvion(idMax);

		}

		Avion av = new Avion(modelo, peso, valor);
		av.setId(idMax + 1);
		mostrarAviones();
	}
}
