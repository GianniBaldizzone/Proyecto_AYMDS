from iniciosesion import InicioSesion
from Menu import Menu
from  iniciosesion import InicioSesion

import unittest
import sys
from iniciosesion import TestInicioSesion


if __name__ == "__main__":
  print("Bienvenido")
  menutest = ""
  while menutest != "N":
    menutest = input("Quiere realizar los test S/N ?")
    if menutest == "S":
      resultado_test = unittest.TestLoader().loadTestsFromTestCase(TestInicioSesion)
      resultado_ = unittest.TextTestResult(sys.stdout, True, 1)
      resultado_test.run(resultado_)
      if resultado_.wasSuccessful():
        print("Fue exitoso")
        print(resultado_)
      else:
        print("Hubo error")
        print(resultado_)
    else:
      print("A bueno adios master")
  print("adios")


menu_inicio_sesion = InicioSesion()

menu_inicio_sesion.mostrar_inicio_sesion()

