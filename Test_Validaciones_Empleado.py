import unittest
from ValidacionesEmpleado import ValidacionesEmpleado

class TestValidacionesEmpleado(unittest.TestCase):

    def test_validar_nombre(self):
        # Caso de prueba: Nombre válido
        nombre = "Victoria"
        if nombre and nombre.strip().isalpha():
            return True
        self.assertEqual(nombre)
        
       # Caso de prueba: Nombre no válido (dígitos)
        nombre = "123"
        self.assertFalse(nombre and nombre.strip().isalpha())

        

        # Caso de prueba: Nombre vacío
        nombre = ""
        resultado = ValidacionesEmpleado.validar_nombre(nombre)
        self.assertIsNone(resultado)

        # Caso de prueba: Nombre con dígitos
        nombre = "Victoria123"
        resultado = ValidacionesEmpleado.validar_nombre(nombre)
        self.assertIsNone(resultado)

    def test_validar_apellido(self):
        # Caso de prueba: Apellido válido
        apellido = "Troiano"
        resultado = ValidacionesEmpleado.validar_apellido(apellido)
        self.assertEqual(resultado, "Troiano")

        # Caso de prueba: Apellido vacío
        apellido = ""
        resultado = ValidacionesEmpleado.validar_apellido(apellido)
        self.assertIsNone(resultado)

        # Caso de prueba: Apellido con dígitos
        apellido = "Troiano456"
        resultado = ValidacionesEmpleado.validar_apellido(apellido)
        self.assertIsNone(resultado)



#if __name__ == '__main__':
    #unittest.main()
