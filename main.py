import unittest
from flask import Flask, render_template
from bd import Conexion

app = Flask(__name__)


@app.route('/')
def index():
  nombre_base_datos = 'househunter.db'
  conexion = Conexion(nombre_base_datos)


  nombre = "Gamaliel"
  apellido = "Quiroz"
  datos = {
      'titulo': 'Mi Página',
      'mensaje': '¡Hola desde Flask!',
      'nombre': nombre,
      'apellido': apellido
  }

  return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
    
def run_tests():
    # Crea una instancia del TestLoader
    test_loader = unittest.TestLoader()

    # Carga las pruebas desde los archivos de prueba
    test_suite = test_loader.discover('test', pattern='test_*.py')

    # Ejecuta las pruebas utilizando TextTestRunner
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

if __name__ == '__main__':

    run_tests()

 
from iniciosesion import InicioSesion
from Menu import Menu
from iniciosesion import InicioSesion

menu_inicio_sesion = InicioSesion()
menu_inicio_sesion.mostrar_inicio_sesion()
