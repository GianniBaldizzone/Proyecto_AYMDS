
import sqlite3


class Conexion:
  
  #Conexion
  def __init__(self, nombreBD):
    self.conexion = sqlite3.connect(nombreBD)
    self.cursor = self.conexion.cursor()
  
  def CerrarBD(self):
    self.conexion.close()
    self.cursor.close()
  #Conexion
  
  #ABM habitaciones
  def CrearTablaHabitacion(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS HABITACION(
      id INTEGER PRIMARY KEY,
      numero INT,
      precio FLOAT,
      piso INT,
      estado_de_limpieza TEXT,
      capacidad_actual INT,
      capacidad_maxima INT,
      tipo_de_habitacion TEXT
      )
    ''')
    self.conexion.commit()

  def IngresarHabitacion(self, numero, precio, piso,capacidadMaxima, tipoDeHabitacion):
    self.cursor.execute(
      "INSERT INTO HABITACION (numero, precio, piso, estado_de_limpieza, capacidad_actual, capacidad_maxima, tipo_de_habitacion) VALUES (?, ?, ?,'Limpio', 0, ?, ?)",
      (numero, precio, piso, capacidadMaxima, tipoDeHabitacion))
    self.conexion.commit()
    print("Habitacion creada con exito!!!")

  def MostrarHabitaciones(self):
    self.cursor.execute("SELECT *FROM HABITACION")
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def ModificarHabitacion(self, nombre, apellido, dni, id):
    self.cursor.execute(
        " UPDATE CLIENTE SET nombre=?,apellido=?,dni=? WHERE id = ? ",
        (nombre, apellido, dni, id))
    self.conexion.commit()

  def ModificarEliminar(self, id):
    self.cursor.execute(" DELETE FROM HABITACION WHERE id = ?", (id))
    self.conexion.commit()



  def MostrarHabitacionesPorPiso(self, piso):
    self.cursor.execute("SELECT * FROM HABITACION WHERE piso = ?", (piso,))
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def MostrarHabitacionesPorCantidadMaxima(self, cantidadMaxima):
    self.cursor.execute("SELECT *FROM HABITACION WHERE capacidad_maxima = ?",(cantidadMaxima,))
    habitaciones = self.cursor.fetchall()
    return habitaciones

  #ABM habitaciones
  #ABM empleados
  def CrearTablaEmpleados(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLEADO(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    dni INT,
    isAdmin INT,
    telefono INT
    )
    ''')
    self.conexion.commit()
  
  def IngresarEmpleados(self, nombre, apellido, dni,isAdmin, telefono):
    self.cursor.execute(
      "INSERT INTO EMPLEADO (nombre, apellido, dni, isAdmin, telefono) VALUES (?, ?, ?, ?, ?)",
      (nombre, apellido, dni, isAdmin, telefono))
    self.conexion.commit()
    print("Empleado creado con exito!!!")
  
  def MostrarEmpleados(self):
    try:
        self.cursor.execute("SELECT * FROM EMPLEADO")
        empleados = self.cursor.fetchall()
        return empleados
    except sqlite3.Error as e:
        print("Error al recuperar empleados:", e)
        return []
  
  def ModificarEmpleados(self, nombre, apellido, dni, isAdmin, telefono):
    self.cursor.execute(
        " UPDATE EMPLEADO SET nombre=?,apellido=?,dni=?,isAdmin=?,telefono=? WHERE id = ? ",
        (nombre, apellido, dni, isAdmin, telefono, id))
    self.conexion.commit()
  
  def EmpleadoEliminar(self, id):
    self.cursor.execute(" DELETE FROM EMPLEADO WHERE id = ?", (id))
    self.conexion.commit()
    print("\n")
    print("Empleado eliminado con exito!!!")
    print("\n")
  
  
  #ABM Empleados



