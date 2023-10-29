
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
      capacidad INT,
      tipo_de_habitacion TEXT,
      disponibilidad TEXT
      )
    ''')
    self.conexion.commit()

  def IngresarHabitacion(self, numero, precio, piso, capacidad, tipoDeHabitacion, disponibilidad):
    self.cursor.execute(
      "INSERT INTO HABITACION (numero, precio, piso, capacidad, tipo_de_habitacion, disponibilidad) VALUES (?, ?, ?,?, ?, ?)",
      (numero, precio, piso, capacidad, tipoDeHabitacion, disponibilidad))
    self.conexion.commit()
    print("Habitacion creada con exito!!!")

  def MostrarHabitaciones(self):
    self.cursor.execute("SELECT * FROM HABITACION")
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def ModificarHabitacion(self, numero, precio, piso, capacidad, tipoDeHabitacion, disponibilidad):
    self.cursor.execute(
        " UPDATE HABITACION SET numero=?,precio=?,piso=?,capacidad=?,tipoDeHabitacion=?,disponibilidad=?  WHERE id = ? ",
        ( numero, precio, piso, capacidad, tipoDeHabitacion,disponibilidad))
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
    try:
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS EMPLEADO(
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        dni INT,
        isAdmin INT,
        telefono INT,
        contraseña TEXT
        )
        ''')
        self.conexion.commit()
        print("Tabla EMPLEADO creada exitosamente!")
    except sqlite3.Error as e:
        print("Error al crear la tabla EMPLEADO:", e)
  
  def IngresarEmpleados(self, nombre, apellido, dni,isAdmin, telefono, contraseña):
    self.cursor.execute(
      "INSERT INTO EMPLEADO (nombre, apellido, dni, isAdmin, telefono,contraseña) VALUES (?, ?, ?, ?, ?,?)",
      (nombre, apellido, dni, isAdmin, telefono, contraseña))
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
            "INSERT INTO RESERVA (empleado_id, fechaChekin, fechaCheckout, habitacion_id, estado, huesped_id, tipoReserva) VALUES (?, ?, ?, ?, ?, ?, ?)",
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
  def MostrarActividad(self):
    self.cursor.execute("SELECT *FROM ACTIVIDAD")
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def ModificaActividad(nombre, tipo_actividad, capacidad, reserva_id):
    self.cursor.execute(
        " UPDATE ACTIVIDAD SET nombre=?,capacidad=?,reserva_id=? WHERE id = ? ",
        (nombre, tipo_actividad, capacidad, reserva_id))
    self.conexion.commit()

  def ModificarEliminar(self, id):
    self.cursor.execute(" DELETE FROM ACTIVIDAD WHERE id = ?", (id))
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
  
  def ModificarHuespedes(self, numeroID, campo, nuevo_valor):
    consulta_sql = f"UPDATE HUESPED SET {campo} = ? WHERE id = ?"
    
  
    self.cursor.execute(consulta_sql, (nuevo_valor, numeroID))
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

  #Eliminación de tablas - Test 

  def EliminarTablaHabitacion(self):
    try:
        self.cursor.execute("DROP TABLE IF EXISTS HABITACION")
        self.conexion.commit()
        print("Tabla HABITACION eliminada con éxito!!!")
    except sqlite3.Error as e:
        print("Error al eliminar la tabla HABITACION:", e)

  def EliminarTablaEmpleados(self):
    try:
        self.cursor.execute("DROP TABLE IF EXISTS EMPLEADO")
        self.conexion.commit()
        print("Tabla EMPLEADO eliminada con éxito!!!")
    except sqlite3.Error as e:
        print("Error al eliminar la tabla EMPLEADO:", e)

  def EliminarTablaReserva(self):
    try:
        self.cursor.execute("DROP TABLE IF EXISTS RESERVA")
        self.conexion.commit()
        print("Tabla RESERVA eliminada con éxito!!!")
    except sqlite3.Error as e:
        print("Error al eliminar la tabla RESERVA:", e)

  def EliminarTablaActividad(self):
    try:
        self.cursor.execute("DROP TABLE IF EXISTS ACTIVIDAD")
        self.conexion.commit()
        print("Tabla ACTIVIDAD eliminada con éxito!!!")
    except sqlite3.Error as e:
        print("Error al eliminar la tabla ACTIVIDAD:", e)

  def EliminarTablaHuesped(self):
    try:
        self.cursor.execute("DROP TABLE IF EXISTS HUESPED")
        self.conexion.commit()
        print("Tabla HUESPED eliminada con éxito!!!")
    except sqlite3.Error as e:
        print("Error al eliminar la tabla HUESPED:", e)

  #Eliminación de tablas - Test 

  #Seteo de datos

  def InsertarDatosPruebaHabitacion(self):
    query = '''
    INSERT INTO HABITACION (numero, precio, piso, capacidad, tipo_de_habitacion, disponibilidad) 
    VALUES 
    (101, 150, 1, 2, 'Doble', 'Disponible'),
    (102, 200, 2, 4, 'Suite', 'Disponible'),
    (103, 250, 1, 3, 'Individual', 'Disponible'),
    (104, 300, 3, 6, 'Suite Presidencial', 'Disponible'),
    (105, 180, 2, 3, 'Doble', 'Disponible'),
    (106, 220, 1, 2, 'Individual', 'Disponible'),
    (107, 270, 3, 4, 'Doble', 'Disponible'),
    (108, 320, 2, 3, 'Individual', 'Disponible'),
    (109, 350, 4, 5, 'Suite', 'Disponible'),
    (110, 400, 3, 4, 'Doble', 'Disponible')
    '''
    self.cursor.execute(query)
    self.conexion.commit()
    print("Datos de prueba para HABITACION insertados con éxito!!!")

  def InsertarDatosPruebaEmpleados(self):
    query = '''
    INSERT INTO EMPLEADO (nombre, apellido, dni, isAdmin, telefono, contraseña) 
    VALUES 
    ('Gianni', 'Baldizzone', 12345678, 1, 123456789, 'contrasena1'),
    ('Victoria', 'Troiano', 23456789, 1, 234567890, 'contrasena2'),
    ('Carlos', 'Rodriguez', 34567890, 0, 345678901, 'contrasena3'),
    ('Laura', 'Martinez', 45678901, 0, 456789012, 'contrasena4'),
    ('David', 'Lopez', 56789012, 0, 567890123, 'contrasena5'),
    ('Ana', 'Torres', 67890123, 0, 678901234, 'contrasena6'),
    ('Pedro', 'Sanchez', 78901234, 0, 789012345, 'contrasena7'),
    ('Elena', 'Ramirez', 89012345, 0, 890123456, 'contrasena8'),
    ('Gabriel', 'Hernandez', 90123456, 0, 901234567, 'contrasena9'),
    ('Sofia', 'Diaz', 12345670, 0, 123456780, 'contrasena10')
    '''
    self.cursor.execute(query)
    self.conexion.commit()
    print("Datos de prueba para EMPLEADO (incluyendo contraseñas) insertados con éxito!!!")


  def InsertarDatosPruebaReserva(self):
    query = '''
    INSERT INTO RESERVA (empleado_id, fechaChekin, fechaCheckout, habitacion_id, estado, huesped_id, tipoReserva) 
    VALUES 
    (1, '2023-11-01', '2023-11-10', 1, 'Activa', 1, 'Reserva'),
    (1, '2023-11-02', '2023-11-11', 2, 'Activa', 2, 'Reserva'),
    (1, '2023-11-03', '2023-11-12', 3, 'Activa', 3, 'Reserva'),
    (1, '2023-11-04', '2023-11-13', 4, 'Activa', 4, 'Reserva'),
    (1, '2023-11-05', '2023-11-14', 5, 'Activa', 5, 'Reserva'),
    (2, '2023-11-06', '2023-11-15', 6, 'Activa', 6, 'Reserva'),
    (2, '2023-11-07', '2023-11-16', 7, 'Activa', 7, 'Reserva'),
    (2, '2023-11-08', '2023-11-17', 8, 'Activa', 8, 'Reserva'),
    (2, '2023-11-09', '2023-11-18', 9, 'Activa', 9, 'Reserva'),
    (2, '2023-11-10', '2023-11-19', 10, 'Activa', 10, 'Reserva')
    '''
    self.cursor.execute(query)
    self.conexion.commit()
    print("Datos de prueba para RESERVA insertados con éxito!!!")


  def InsertarDatosPruebaActividad(self):
    query = '''
    INSERT INTO ACTIVIDAD (nombre, tipo_actividad, capacidad, reserva_id) 
    VALUES 
    ('Gimnasio', 'Deporte', 20, 1),
    ('Piscina', 'Recreación', 50, 2),
    ('Masajes', 'Bienestar', 10, 3),
    ('Excursión local', 'Turismo', 30, 4),
    ('Clases de cocina', 'Culinaria', 15, 5),
    ('Sala de conferencias', 'Negocios', 100, 6),
    ('Entretenimiento nocturno', 'Entretenimiento', 80, 7),
    ('Servicio de habitaciones', 'Servicio', 200, 8),
    ('Lavandería', 'Servicio', 150, 9),
    ('Transporte local', 'Turismo', 40, 10)
    '''
    self.cursor.execute(query)
    self.conexion.commit()
    print("Datos de prueba para ACTIVIDAD insertados con éxito!!!")

  def InsertarDatosPruebaHuesped(self):
    query = '''
    INSERT INTO HUESPED (nombre, apellido, numero_pasaporte, dni, nacionalidad, grupo_sanguineo, seguro_vida) 
    VALUES 
    ('Carlos', 'Gomez', 'AB123456', 12345678, 'Argentina', 'A+', 'Sí'),
    ('Ana', 'Martinez', 'CD789012', 23456789, 'España', 'B-', 'No'),
    ('Luis', 'Rodriguez', 'EF345678', 34567890, 'México', 'O+', 'Sí'),
    ('Elena', 'Perez', 'GH901234', 45678901, 'Colombia', 'AB-', 'No'),
    ('Marta', 'Hernandez', 'IJ567890', 56789012, 'Perú', 'A-', 'Sí'),
    ('Javier', 'Lopez', 'KL123456', 67890123, 'Chile', 'B+', 'No'),
    ('Isabel', 'Diaz', 'MN789012', 78901234, 'Brasil', 'O-', 'Sí'),
    ('Sergio', 'Sanchez', 'OP901234', 89012345, 'Uruguay', 'AB+', 'No'),
    ('Laura', 'Garcia', 'QR123456', 90123456, 'Paraguay', 'A+', 'Sí'),
    ('Daniel', 'Fernandez', 'ST789012', 12345670, 'Ecuador', 'B-', 'No')
    '''
    self.cursor.execute(query)
    self.conexion.commit()
    print("Datos de prueba para HUESPED insertados con éxito!!!")