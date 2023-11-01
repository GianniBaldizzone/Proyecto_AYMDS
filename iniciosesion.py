import sqlite3
from Menu import Menu
class InicioSesion:
    def __init__(self):
        self.conexion = sqlite3.connect("househunter.db")
        self.cursor = self.conexion.cursor()
        self.id_empleado = None  # Variable para almacenar el ID del empleado

    def autenticar(self, nombre_usuario, contrasena):
        try:
            self.cursor.execute("SELECT id FROM EMPLEADO WHERE nombre=? AND contraseña=?", (nombre_usuario, contrasena))
            empleado_id = self.cursor.fetchone()

            if empleado_id:
                empleado_id = empleado_id[0]  # Extraer el ID del resultado
                print(f"Inicio de sesión exitoso para el empleado con ID {empleado_id}.")
                return empleado_id
            else:
                print("Inicio de sesión fallido. Verifique sus credenciales.")
                return None
        except sqlite3.Error as e:
            print("Error al autenticar:", e)
            return None

    def mostrar_inicio_sesion(self):
        bucle = 0
        self.id_empleado = None  # Reiniciar el ID del empleado

        while bucle != 1:
            print("=== Inicio de Sesión ===")
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            self.id_empleado = self.autenticar(nombre_usuario, contrasena)

            if self.id_empleado is not None:
                print("\n")
                print(f"Inicio de sesión exitoso para el empleado con ID {self.id_empleado}.")
                menu_principal = Menu(nombre_usuario, contrasena, self.id_empleado)
                menu_principal.mostrar_menu()
                bucle = 1