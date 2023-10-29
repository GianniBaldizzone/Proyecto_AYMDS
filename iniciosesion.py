import sqlite3
from Menu import Menu

class InicioSesion:
    def __init__(self):
        self.conexion = sqlite3.connect("househunter.db")
        self.cursor = self.conexion.cursor()

    def autenticar(self, nombre_usuario, contrasena):
        try:
            # Consultar la base de datos para verificar las credenciales
            self.cursor.execute("SELECT * FROM EMPLEADO WHERE nombre=? AND contraseña=?", (nombre_usuario, contrasena))
            empleado = self.cursor.fetchone()

            if empleado:
                print("Inicio de sesión exitoso.")
                return True
            else:
                print("Inicio de sesión fallido. Verifique sus credenciales.")
                return False
        except sqlite3.Error as e:
            print("Error al autenticar:", e)
            return False

    def mostrar_inicio_sesion(self):
        bucle = 0
        while bucle != 1:
            print("=== Inicio de Sesión ===")
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            if self.autenticar(nombre_usuario, contrasena):
                print("\n")
                menu_principal = Menu()
                menu_principal.mostrar_menu()
                bucle = 1
