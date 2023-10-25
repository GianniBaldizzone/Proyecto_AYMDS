from Menu import Menu
class InicioSesion:
    def autenticar(self, nombre_usuario, contrasena):
        # Simulación de autenticación exitosa para este ejemplo
        if nombre_usuario == "usuario" and contrasena == "contraseña":
            bucle = 1
            return True
        else:
            bucle = 0
            return False

    def mostrar_inicio_sesion(self):
      bucle = 0
      while bucle != 1:
        print("=== Inicio de Sesión ===")
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        if self.autenticar(nombre_usuario, contrasena):
            print("Inicio de sesión exitoso.")
            print("\n")
            menu_principal = Menu()
            menu_principal.mostrar_menu()
        else:
            print("Inicio de sesión fallido. Verifique sus credenciales.")
            