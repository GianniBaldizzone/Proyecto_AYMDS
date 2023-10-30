import sqlite3
from bd import Conexion


class ValidacionesEmpleado:
    @staticmethod
    def validar_nombre(nombre):
        while True:
            if nombre and nombre.strip().isalpha():
                return nombre.strip()
            else:
                print("Error: El nombre no puede estar vacío y debe contener solo letras.")
                nombre = input("Por favor, ingrese el nombre nuevamente: ")

    @staticmethod
    def validar_apellido(apellido):
        while True:
            if apellido and apellido.strip().isalpha():
                return apellido.strip()
            else:
                print("Error: El apellido no puede estar vacío y debe contener solo letras.")
                apellido = input("Por favor, ingrese el apellido nuevamente: ")

    @staticmethod
    def validar_dni():
        while True:
            dni = input("Ingrese el DNI: ")
            if dni and dni.strip().isdigit() and len(dni.strip()) == 8:
                return int(dni.strip())
            else:
                print("Error: El DNI debe tener 8 dígitos y ser un número válido.")

    @staticmethod
    def validar_administrador():
        while True:
            isAdmin = input("Es administrador (1 para sí, 0 para no): ")
            if isAdmin and isAdmin.strip().isdigit() and int(isAdmin.strip()) in [0, 1]:
                return int(isAdmin.strip())
            else:
                print("Error: El estado de administrador debe ser 0 o 1.")

    @staticmethod
    def validar_telefono():
        while True:
            telefono = input("Ingrese el número de teléfono: ")
            if telefono and telefono.strip().isdigit() and len(telefono.strip()) >= 7:
                return int(telefono.strip())
            else:
                print("Error: El número de teléfono debe tener al menos 7 dígitos y ser un número válido.")
  

    @staticmethod    
    def validar_contrasena():
        while True:
            contrasena = input("Ingrese la contraseña: ")

            # Validar que la contraseña tiene al menos 8 caracteres
            if len(contrasena) < 8:
                print("Error: La contraseña debe tener al menos 8 caracteres.")
                continue

            # Validar que la contraseña contiene al menos una letra y un número
            if not any(c.isalpha() for c in contrasena) or not any(c.isdigit() for c in contrasena):
                print("Error: La contraseña debe contener al menos una letra y un número.")
                continue

            return contrasena
        
    @staticmethod    
    def validar_ID():
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        while True:
            empleado_id = input("Ingrese el ID del empleado: ")
            
                # Validar que el id no sea nulo
            if empleado_id is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                empleado_id = int(empleado_id)  # Intenta convertir el valor a un entero
                if empleado_id <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            if not conexion.existeID(empleado_id):
                print("Error: El empleado con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            return empleado_id