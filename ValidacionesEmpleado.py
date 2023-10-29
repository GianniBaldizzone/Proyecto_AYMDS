
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
  