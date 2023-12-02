import unittest
from flask import Flask, render_template, request, redirect, url_for, session
from bd import Conexion
from Menu import Menu

app = Flask(__name__)
app.secret_key = 'contrasena1'  # Clave secreta para las sesiones
nombreBD = 'househunter.db'
conexion = Conexion(nombreBD)

app.debug = True




@app.route('/cerrar')
def cerrar():
  session.clear()
  return redirect('login')
  

@app.route('/')
def index():
     # Verificar si el usuario ya está autenticado
    if 'usuario' in session:
        return redirect(url_for('programa'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Verificar si el usuario ya está autenticado
    if 'usuario' in session:
        return redirect(url_for('programa'))

    
    if request.method == 'POST':
        nombre_usuario = request.form["nombre_usuario"]
        contrasena = request.form["contrasena"]
        print(f"Usuario: {nombre_usuario}, Contraseña: {contrasena}")
        nombreBD = 'househunter.db'
        conexion = Conexion(nombreBD)
        empleados = conexion.MostrarEmpleados()
        conexion.CerrarConexion()
        error = "Credenciales Incorrectas. Por favor, vuelva a intentarlo."

        for empleado in empleados:
            print(f"Empleado en la base de datos: {empleado}")
            if empleado[1] == nombre_usuario and empleado[6] == contrasena:
                session['usuario'] = empleado[1]
                session['contrasena'] = empleado[6]
                session['id'] = empleado[0]
                
                return redirect(url_for('programa'))
                
        
        return render_template('login.html', error=error)

    error = ""
    return render_template('login.html', error=error)
 
 

@app.route('/programa', methods=['GET', 'POST'])
def programa():
    if len(session) == 0:
        return redirect('login')
    else:
        # Crear una instancia de TuClaseMenu (ajusta según la implementación real)
        menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
        reservas = menu.ver_reservas()

        return render_template('programa.html', nombre_usuario=session.get('usuario'), reservas=reservas)


@app.route('/reserva/reservaVer', methods=['GET'])
def  reservaVer():
     # Crear una instancia de TuClaseMenu (ajusta según la implementación real)
        menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
        reservas = menu.ver_reservas()

        return render_template('reservaVer.html', nombre_usuario=session.get('usuario'), reservas=reservas)
    

@app.route('/hospedaje/HospedajeVer', methods=['GET'])
def  hospedajeVer():
     # Crear una instancia de TuClaseMenu (ajusta según la implementación real)
        menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
        hospedaje = menu.ver_hospedajes()

        return render_template('hospedajeVer.html', nombre_usuario=session.get('usuario'), hospedaje=hospedaje)
        
@app.route('/reserva', methods=['GET'])
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
def reservaNueva():
    menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
    numeros_habitacion = menu.obtener_numeros_habitacion()

    return render_template('reservaNueva.html', nombre_usuario=session.get('usuario'), numeros_habitacion=numeros_habitacion)

@app.route('/reserva/reservaCancelar')
def  reservaCancelar():
    return render_template('reservaCancelar.html')

@app.route('/reserva/reservaEditar')
def  reservaEditar():
    return render_template('reservaEditar.html')

@app.route('/reserva/reservaEditar2')
def  reservaEditar2():
    return render_template('reservaEditar2.html')

@app.route('/hospedaje/checkinNuevo')
def  checkinNuevo():
    return render_template('checkinNuevo.html')

@app.route('/hospedaje/checkinCancelar')
def  checkinCancelar():
    return render_template('checkinCancelar.html')

@app.route('/hospedaje/checkinEditar')
def  checkinEditar():
    return render_template('checkinEditar.html')

@app.route('/hospedaje/checkinEditar2')
def  checkinEditar2():
    return render_template('checkinEditar2.html')

@app.route('/actividades/actividadDisponible')
def  actividadDisponible():
    
     # Crear una instancia de TuClaseMenu (ajusta según la implementación real)
        menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
        actividad = menu.mostrar_actividad()

        return render_template('actividadDisponible.html', nombre_usuario=session.get('usuario'), actividad=actividad)
    

@app.route('/actividades/verReservaActividad')
def  verReservaActividad():
    
     # Crear una instancia de TuClaseMenu (ajusta según la implementación real)
        menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
        reserva = menu.ver_reservas_actividades()

        return render_template('verReservaActividad.html', nombre_usuario=session.get('usuario'), reserva=reserva)

@app.route('/actividades/actividadNueva')
def  actividadNueva():
    return render_template('actividadNueva.html')

@app.route('/actividades/actividadCancelar')
def  actividadCancelar():
    return render_template('actividadCancelar.html')

@app.route('/actividades/actividadEditar')
def  actividadEditar():
    return render_template('actividadEditar.html')

@app.route('/actividades/actividadEditar2')
def  actividadEditar2():
    return render_template('actividadEditar2.html')

@app.route('/abm/abmHabitaciones')
def  abmHabitaciones():
    return render_template('abmHabitaciones.html')

@app.route('/abm/abmEmpleados')
def  abmEmpleados():
    return render_template('abmEmpleados.html')

@app.route('/abm/abmActividades')
def  abmActividades():
    return render_template('abmActividades.html')

@app.route('/abm/abmHuespedes')
def  abmHuespedes():
    return render_template('abmHuespedes.html')

@app.route('/abm/abmBd')
def  abmBd():
    return render_template('abmBd.html')

@app.route('/abm/abmHabitaciones/habitacionCrear')
def  habitacionCrear():
    return render_template('habitacionCrear.html')

@app.route('/abm/abmHabitaciones/habitacionEditar')
def  habitacionEditar():
    return render_template('habitacionEditar.html')

@app.route('/abm/abmHabitaciones/habitacionEditar2')
def  habitacionEditar2():
    return render_template('habitacionEditar2.html')

@app.route('/abm/abmHabitaciones/habitacionEliminar')
def  habitacionEliminar():
    return render_template('habitacionEliminar.html')

@app.route('/abm/abmHabitaciones/habitacionMostrar')
def  habitacionMostrar():
    menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
    habitacion = menu.mostrar_habitaciones()

    return render_template('habitacionMostrar.html', nombre_usuario=session.get('usuario'), habitacion=habitacion)
    

@app.route('/abm/abmHabitaciones/habitacionFiltrar')
def  habitacionFiltrar():
    return render_template('habitacionFiltrar.html')

@app.route('/abm/abmEmpleados/empleadoCrear')
def  empleadoCrear():
    return render_template('empleadoCrear.html')

@app.route('/abm/abmEmpleados/empleadoEditar')
def  empleadoEditar():
    return render_template('empleadoEditar.html')

@app.route('/abm/abmEmpleados/empleadoEditar2')
def  empleadoEditar2():
    return render_template('empleadoEditar2.html')

@app.route('/abm/abmEmpleados/empleadoEliminar')
def  empleadoEliminar():
    return render_template('empleadoEliminar.html')

@app.route('/abm/abmEmpleados/empleadoMostrar')
def  empleadoMostrar():
    menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
    empleado = menu.mostrar_empleado()

    return render_template('empleadoMostrar.html', nombre_usuario=session.get('usuario'), empleado=empleado)
    

@app.route('/abm/abmActividades/actividadCrear')
def  actividadCrear():
    return render_template('actividadCrear.html')

@app.route('/abm/abmActividades/actividadEdit')
def  actividadEdit():
    return render_template('actividadEdit.html')

@app.route('/abm/abmActividades/actividadEdit2')
def  actividadEdit2():
    return render_template('actividadEdit2.html')

@app.route('/abm/abmActividades/actividadEliminar')
def  actividadEliminar():
    return render_template('actividadEliminar.html')

@app.route('/abm/abmActividades/actividadMostrar')
def  actividadMostrar():
    menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
    actividad = menu.mostrar_actividad()

    return render_template('actividadDisponible.html', nombre_usuario=session.get('usuario'), actividad=actividad)

@app.route('/abm/abmHuespedes/huespedCrear')
def  huespedCrear():
    return render_template('huespedCrear.html')

@app.route('/abm/abmHuespedes/huespedEdit')
def  huespedEdit():
    return render_template('huespedEdit.html')

@app.route('/abm/abmHuespedes/huespedEdit2')
def  huespedEdit2():
    return render_template('huespedEdit2.html')

@app.route('/abm/abmHuespedes/huespedEliminar')
def  huespedEliminar():
    return render_template('huespedEliminar.html')

@app.route('/abm/abmHuespedes/huespedMostrar')
def  huespedMostrar():
    menu = Menu(nombre_empleado=session.get('usuario'), contrasena_empleado=session.get('contrasena'), id_empleado=session.get('id'))
    huesped = menu.mostrar_huespedes()

    return render_template('huespedMostrar.html', nombre_usuario=session.get('usuario'), huesped=huesped)

@app.route('/abm/abmBd/crearTablas')
def  crearTablas():
    return render_template('crearTablas.html')

@app.route('/crearTablas/crearTablasHabitacion')
def  crearTablasHabitacion():
    return render_template('crearTablasHabitacion.html')




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
