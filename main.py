import unittest
from flask import Flask, render_template, request
from bd import Conexion

app = Flask(__name__)


@app.route('/')
def index():
  nombre_base_datos = 'househunter.db'
 
 
  return render_template('index.html')


from iniciosesion import InicioSesion
@app.route('/programa', methods=['POST'])
def programa():
    if request.method == 'POST':
        nombre_usuario = request.form["nombre_usuario"]
        contrasena = request.form["contrasena"]
        
        # Crea una instancia de InicioSesion y realiza la autenticación
        inicio_sesion = InicioSesion()
        
        #autenticamos
        empleado_id = inicio_sesion.autenticar(nombre_usuario, contrasena)
        
        #redirecciones
        
        #si son validas las credenciales
        if empleado_id is not None:
            return render_template('programa.html', nombre_usuario=nombre_usuario)
        
        #si no son validas las credenciales
        if empleado_id is None:
            error = 'Credenciales Incorrectas. Por favor, vuelva a intentarlo.'
            return render_template('index.html', error=error) 
       

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/hospedaje')
def hospedaje():
    return render_template('hospedaje.html')

@app.route('/actividades')
def actividades():
    return render_template('actividades.html')

@app.route('/abm')
def abm():
    return render_template('abm.html')

@app.route('/reserva/reservaNueva')
def  reservaNueva():
    return render_template('reservaNueva.html')

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
