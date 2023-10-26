
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

  #ABM Reserva
  def CrearTablaReserva(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS RESERVA (
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER,
        fechaChekin DATETIME,
        fechaCheckout DATETIME,
        habitacion_id INTEGER,
        estado TEXT,
        huesped_id INTEGER,
        tipoReserva  TEXT,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADO (id),
        FOREIGN KEY (habitacion_id) REFERENCES HABITACION (id),
        FOREIGN KEY (huesped_id) REFERENCES HUESPED (id)
        )
        ''')
        self.conexion.commit()
    
  def IngresarReserva(self, empleado_id, fecha_checkin, fecha_checkout,habitacion_id, estado, huesped_id, tipo_reserva):
        result = None
        self.cursor.execute(
            "INSERT INTO RESERVA (empleado_id, fechaChekin, fechaCheckout, habitacion_id, estado, huesped_id, tipo_reserva) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (empleado_id, fecha_checkin, fecha_checkout, habitacion_id, estado, huesped_id, tipo_reserva))
        if self.cursor:
            self.conexion.commit()
            result = "Reserva creada con éxito!!!"
        else:
            result = "Error al crear la reserva"
        return result
    
  def MostrarReservas(self):
        result = None
        self.cursor.execute("SELECT * FROM RESERVA")
        if self.cursor:
            result = self.cursor.fetchall()
        else:
            result = "Error al recuperar reservas"
        return result
    
  def ModificarReserva(self, empleado_id, fecha_checkin, fecha_checkout,habitacion_id, estado, huesped_id, tipoReserva, id):
        result = None
        self.cursor.execute(
            "UPDATE RESERVA SET empleado_id=?, fechaChekin=?, fechaCheckout=?, habitacion_id=?, estado=?, huesped_id=?, tipoReserva=? WHERE id = ?",
            (empleado_id, fecha_checkin, fecha_checkout, habitacion_id, estado, huesped_id, tipoReserva, id))
        if self.cursor:
            self.conexion.commit()
            result = "Reserva modificada con éxito!!!"
        else:
            result = "Error al modificar la reserva"
        return result
    
  def EliminarReserva(self, id):
        result = None
        self.cursor.execute("DELETE FROM RESERVA WHERE id = ?", (id,))
        if self.cursor:
            self.conexion.commit()
            print("Reserva eliminada con éxito!!!")
        else:
            print("Error al eliminar la reserva")
        

  def CerrarConexion(self):
        self.conexion.close()
  
  #ABM Reserva

  #ABM Actividad - EN PROCESO
  def CrearTablaActividad(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS ACTIVIDAD(
      id INTEGER PRIMARY KEY,
      nombre TEXT,
      tipo_actividad TEXT,
      capacidad TEXT,
      reserva_id INT,
      FOREIGN KEY (reserva_id) REFERENCES RESERVA (id)
      )
    ''')
    self.conexion.commit()

  def IngresarActividad(self, nombre, tipo_actividad, reserva_id):
    self.cursor.execute(
      "INSERT INTO ACTIVIDAD (nombre, tipo_actividad, capacidad, reserva_id) VALUES (?, ?, 10, ?)",
      (nombre, tipo_actividad, reserva_id))
    self.conexion.commit()
    print("Actividad creada con exito!!!")
  ######
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


  
  #ABM Actividad

  #ABM Huesped
  def CrearTablaHuesped(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS HUESPED(
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    numero_pasaporte INT,
    dni INT,
    nacionalidad INT,
    grupo_sanguineo TEXT,
    seguro_vida TEXT
    )
    ''')
    self.conexion.commit()
  
  def IngresarHuesped(self, nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida):
    self.cursor.execute(
      "INSERT INTO HUESPED (nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida) VALUES (?, ?, ?, ?, ?, ?, ?)",
      (nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida))
    self.conexion.commit()
    print("Huesped creado con exito!!!")
  
  def MostrarHuespedes(self):
    try:
        self.cursor.execute("SELECT * FROM HUESPED")
        huespedes = self.cursor.fetchall()
        return huespedes
    except sqlite3.Error as e:
        print("Error al recuperar huespedes:", e)
        return []
  
  def ModificarHuespedes(self, id, nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida):
    
      self.cursor.execute(
          " UPDATE HUESPED SET nombre=?,apellido=?, numero_pasaporte=?,dni=?,nacionalidad=?,grupo_sanguineo=?, seguro_vida=? WHERE id = ? ",
          (nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida, id))
      
        
      self.conexion.commit()
      print("\n")
      print("Huesped modificado con éxito!!!")
      print("\n")
      
   
  #Verifica que hay un ID existente contandolo en la bd
  def IDExists(self, numeroID):   
    self.cursor.execute("SELECT COUNT(*) FROM HUESPED WHERE id = ?", (numeroID,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
     
  def HuespedEliminar(self, id):
    self.cursor.execute(" DELETE FROM HUESPED WHERE id = ?", (id))
    self.conexion.commit()
    print("\n")
    print("Huesped eliminado con exito!!!")
    print("\n")
  
  
  #ABM Huesped