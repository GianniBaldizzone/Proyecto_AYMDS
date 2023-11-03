import unittest
from unittest.mock import patch
from io import StringIO
from iniciosesion import InicioSesion  # Importa la clase InicioSesion desde tu módulo

class TestInicioSesion(unittest.TestCase):
    def setUp(self):
        
        self.inicio_sesion = InicioSesion()
        
        # Redirige la salida estándar para capturar las impresiones
        self.output_buffer = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.output_buffer

    def tearDown(self):
        # Cierra la conexión a la base de datos y restaura la salida estándar
        self.inicio_sesion.conexion.close()
        sys.stdout = self.old_stdout

    @patch('builtins.input', side_effect=["test_user", "test_password"])
    def test_mostrar_inicio_sesion_exitoso(self, mock_input):
        self.inicio_sesion.cursor.execute("CREATE TABLE IF NOT EXISTS EMPLEADO (id INTEGER PRIMARY KEY, nombre TEXT, contraseña TEXT)")
        self.inicio_sesion.cursor.execute("INSERT INTO EMPLEADO (nombre, contraseña) VALUES (?, ?)", ("test_user", "test_password"))
        
        self.inicio_sesion.mostrar_inicio_sesion()

        # Captura la salida impresa y verifica si contiene el mensaje de éxito
        output = self.output_buffer.getvalue()
        self.assertIn("Inicio de sesión exitoso para el empleado con ID", output)

    @patch('builtins.input', side_effect=["usuario_inexistente", "contraseña_incorrecta"])
    def test_mostrar_inicio_sesion_fallido(self, mock_input):
        self.inicio_sesion.mostrar_inicio_sesion()

        # Captura la salida impresa y verifica si contiene el mensaje de falla
        output = self.output_buffer.getvalue()
        self.assertIn("Inicio de sesión fallido. Verifique sus credenciales.", output)

if __name__ == '__main__':
    unittest.main()