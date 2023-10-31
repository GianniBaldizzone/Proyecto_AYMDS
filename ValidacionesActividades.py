import sqlite3
from bd import Conexion


class ValidacionesActividades:
    @staticmethod
    def validacionNombre():
        nombre = input("Ingrese un nombre para la actividad:")
        while True:
            if nombre and nombre.strip().isalpha():
                return nombre.strip()
            else:
                print("Error: El nombre de la actividad no puede estar vacío y debe contener solo letras.")
                nombre = input("Por favor, ingrese el nombre nuevamente: ")

    @staticmethod
    def validarTipoActividad():
        bucle = True

        while bucle:
            print("*** Seleccionar Tipo de Actividad***")
            print("1. Paga")
            print("2. Gratuita")
            
            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                tipo_actividad = "Paga"
                print("El tipo de actividad seleccionado fue Paga.")
                return tipo_actividad
            elif eleccion == "2":
                tipo_actividad = "Gratuita"
                print("El tipo de actividad seleccionado fue Gratuita.")
                return tipo_actividad
           
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción válida.")
    
    @staticmethod
    def validarReservaId():
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        
        while True:
            reserva_id = input("Ingrese el ID de la reserva: ")
            
                # Validar que el id no sea nulo
            if reserva_id is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                reserva_id = int(reserva_id)  # Intenta convertir el valor a un entero
                if reserva_id <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            if not conexion.IDReservaExiste(reserva_id):
                print("Error: La reserva con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            return reserva_id
    
    @staticmethod
    def validarActividadId():
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        
        while True:
            actividad_id = input("Ingrese el ID de la actividad: ")
            
                # Validar que el id no sea nulo
            if actividad_id is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                actividad_id = int(actividad_id)  # Intenta convertir el valor a un entero
                if actividad_id <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            if not conexion.IDActividadExiste(actividad_id):
                print("Error: La actividad con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            return actividad_id