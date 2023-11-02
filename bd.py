
import sqlite3
from datetime import datetime


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

  def IngresarHabitacion(self, numero, precio, piso, capacidad, tipoDeHabitacion):
    self.cursor.execute(
      "INSERT INTO HABITACION (numero, precio, piso, capacidad, tipo_de_habitacion, disponibilidad) VALUES (?, ?, ?,?, ?,?)",
      (numero, precio, piso, capacidad, tipoDeHabitacion,"Disponible"))
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

  def actualizar_disponibilidad_habitacion(self, habitacion_id):
        try:
            self.cursor.execute("UPDATE HABITACION SET disponibilidad=? WHERE id=?", ("No disponible", habitacion_id))
            self.conexion.commit()
            print(f"La disponibilidad de la habitación con ID {habitacion_id} se ha actualizado a 'No disponible'.")
        except sqlite3.Error as e:
            print("Error al actualizar la disponibilidad de la habitación:", e)

  def obtener_id_habitacion_por_numero(self):
    while True:
        numero_habitacion = input("Ingrese el número de habitación: ")
        if not numero_habitacion.isdigit():
            print("Error: Debe ingresar un número de habitación válido.")
            continue

        try:
            numero_habitacion = int(numero_habitacion)
            self.cursor.execute("SELECT id, disponibilidad FROM HABITACION WHERE numero=?", (numero_habitacion,))
            resultado = self.cursor.fetchone()

            if resultado:
                id_habitacion, disponibilidad = resultado
                if disponibilidad == 'Disponible':
                    return id_habitacion
                else:
                    print(f"La habitación con número {numero_habitacion} no está disponible.")
            else:
                print(f"No se encontró ninguna habitación con el número {numero_habitacion}.")
        except sqlite3.Error as e:
            print("Error al obtener el ID de la habitación:", e)

        # Solicitar un nuevo número de habitación
        print("Por favor, ingrese un número de habitación válido.")
  
  
  
  
  
  def MostrarHabitacionesPorPiso(self, piso):
    self.cursor.execute("SELECT * FROM HABITACION WHERE piso = ?", (piso,))
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def MostrarHabitacionesPorCantidadMaxima(self, cantidadMaxima):
    self.cursor.execute("SELECT *FROM HABITACION WHERE capacidad_maxima = ?",(cantidadMaxima,))
    habitaciones = self.cursor.fetchall()
    return habitaciones
  
  def existeIDHab(self, habitacion_id):
    self.cursor.execute("SELECT COUNT(*) FROM HABITACION WHERE id = ?", (habitacion_id,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count

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
  
  def existeID(self, empleado_id):
    self.cursor.execute("SELECT COUNT(*) FROM EMPLEADO WHERE id = ?", (empleado_id,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
  
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
  
  def ConsultarReservasHospedaje(self):
        self.cursor.execute("SELECT * FROM RESERVA WHERE tipoReserva = 'Hospedaje'")
        reservas_hospedaje = self.cursor.fetchall()
        if not reservas_hospedaje:
            print("No se encontraron reservas de tipo Hospedaje.")
        return reservas_hospedaje

  def ConsultarReservasReserva(self):
        self.cursor.execute("SELECT * FROM RESERVA WHERE tipoReserva = 'Reserva'")
        reservas_reserva = self.cursor.fetchall()
        if not reservas_reserva:
            print("No se encontraron reservas de tipo Reserva.")
        return reservas_reserva
    
  def ModificarReservas(self, numeroID, campo, nuevo_valor):
    consulta_sql = f"UPDATE RESERVA SET {campo} = ? WHERE id = ?"
    
  
    self.cursor.execute(consulta_sql, (nuevo_valor, numeroID))
    self.conexion.commit()

    print("\n")
    print("Reserva modificada con éxito!!!")
    print("\n")
      
    
  def EliminarReserva(self, id):
    result = None
    self.cursor.execute("DELETE FROM RESERVA WHERE id = ? AND tipoReserva = 'Reserva'", (id,))
    if self.cursor.rowcount > 0:
        self.conexion.commit()
        print("Reserva eliminada con éxito!!!")
    else:
        print("Error: No se encontró una reserva de tipo 'Reserva' con el ID proporcionado.")

  def EliminarHospedaje(self, id):
    result = None
    self.cursor.execute("DELETE FROM RESERVA WHERE id = ? AND tipoReserva = 'Hospedaje'", (id,))
    if self.cursor.rowcount > 0:
        self.conexion.commit()
        print("Hospedaje eliminado con éxito!!!")
    else:
        print("Error: No se encontró un hospedaje de tipo 'Hospedaje' con el ID proporcionado.")
  def CerrarConexion(self):
        self.conexion.close()
  

  def existe_reserva_similar(self, fecha_checkin, fecha_checkout, habitacion_id):
        try:
            print(f"Verificando si existe una reserva similar para habitación {habitacion_id} en el intervalo de tiempo:")
            print(f"Fecha de check-in: {fecha_checkin}")
            print(f"Fecha de check-out: {fecha_checkout}")

            query = "SELECT COUNT(*) FROM RESERVA WHERE habitacion_id = ? AND fechaChekin <= ? AND fechaCheckout >= ?"
            params = (habitacion_id, fecha_checkout, fecha_checkin)
            self.cursor.execute(query, params)
            count = self.cursor.fetchone()[0]

            if count > 0:
                print("¡Existe una reserva similar en la base de datos!")
                return True
            else:
                print("No se encontraron reservas similares en la base de datos.")
                return False
        except sqlite3.Error as e:
            print("Error al verificar la existencia de la reserva:", e)
            return True  # En caso de error, se asume que la reserva existe (por precaución)




  #Verifica que hay un ID existente contandolo en la bd
  def IDReservaExists(self, numeroID):   
    self.cursor.execute("SELECT COUNT(*) FROM RESERVA WHERE id = ?", (numeroID,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
  #Verifica que hay un ID existente contandolo en la bd
  def IDReservaExiste(self, reserva_id):   
    self.cursor.execute("SELECT COUNT(*) FROM RESERVA WHERE id = ?", (reserva_id,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
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

  def IngresarActividad(self, nombre, tipo_actividad):
    self.cursor.execute(
      "INSERT INTO ACTIVIDAD (nombre, tipo_actividad, capacidad) VALUES (?, ?, 10)",
      (nombre, tipo_actividad))
    self.conexion.commit()
    print("Actividad creada con exito!!!")
  
  
  def ModificaActividad(self, numeroID, campo, nuevo_valor):
    consulta_sql = f"UPDATE ACTIVIDAD SET {campo} = ? WHERE id = ?"
    
  
    self.cursor.execute(consulta_sql, (nuevo_valor, numeroID))
    self.conexion.commit()

    print("\n")
    print("Actividad modificada con éxito!!!")
    print("\n")
      

  def EliminarActividad(self, id):
    self.cursor.execute(" DELETE FROM ACTIVIDAD WHERE id = ?", (id,))
    self.conexion.commit()

  def MostrarActividades(self):
    self.cursor.execute("SELECT * FROM ACTIVIDAD")
    actividades = self.cursor.fetchall()
    return actividades
  
  #ABM Actividad
  
  #ABM Reserva actividad
   ##################################
  #ABM ACTIVIDAD RESERVA
  def CrearTablaActividadReserva(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS ACTIVIDADRESERVA(
    id INTEGER PRIMARY KEY,
    actividad_id INTEGER,
    reserva_id INTEGER,
    FOREIGN KEY (actividad_id) REFERENCES ACTIVIDAD (id),
    FOREIGN KEY (reserva_id) REFERENCES RESERVA (id)
    )
    ''')
    self.conexion.commit()
  ##La reserva de la actividad
  def IngresarReservaActividad(self, actividad_id, reserva_id):
    self.cursor.execute(
      "INSERT INTO ACTIVIDADRESERVA (actividad_id, reserva_id) VALUES (?, ?)",
      (actividad_id, reserva_id))
    self.conexion.commit()
    print("Actividad reservada con exito!!!")
  
  def MostrarActividadReserva(self):
    try:
        self.cursor.execute("SELECT * FROM ACTIVIDADRESERVA")
        reservas = self.cursor.fetchall()
        return reservas
    except sqlite3.Error as e:
        print("Error al recuperar las reservas de las actividades:", e)
        return []
  
  def ModificaActividadReserva(actividad_id, reserva_id):
    self.cursor.execute(
        " UPDATE ACTIVIDADRESERVA SET actividad_id=?,reserva_id=? WHERE id = ? ",
        (actividad_id, reserva_id))
    self.conexion.commit()
  
  def EliminarActividadReserva(self, id):
    self.cursor.execute("DELETE FROM ACTIVIDADRESERVA WHERE id = ?", (id,))
    self.conexion.commit()
  
  #Verifica que hay un ID existente contandolo en la bd
  def IDActividadExiste(self, actividad_id):   
    self.cursor.execute("SELECT COUNT(*) FROM ACTIVIDAD WHERE id = ?", (actividad_id,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
  def IDActividadReservaExiste(self, numeroID):   
    self.cursor.execute("SELECT COUNT(*) FROM ACTIVIDADRESERVA WHERE id = ?", (numeroID,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
  ###################################
  #ABM Reserva actividad
  
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
    huesped_id = self.cursor.lastrowid
    print("Huesped creado con éxito, ID:", huesped_id)
    return huesped_id
  
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
  
  def existeIDHuesp(self, huesped_id):
    self.cursor.execute("SELECT COUNT(*) FROM HUESPED WHERE id = ?", (huesped_id,))
    count = self.cursor.fetchone()[0]
    if count > 0:
      count = True
    else:
      count = False
    return count
  
  
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
    # Lista de tipos de habitación y sus tarifas base
    tipos_habitacion = ["Plata", "Gold", "Diamante"]
    tarifas_base = [150, 200, 250]

    # Inicializa el número de habitación
    numero_habitacion = 1

    for piso in range(5):  # Los pisos van de 0 a 4
        for tipo_habitacion, tarifa_base in zip(tipos_habitacion, tarifas_base):
            for _ in range(20):  # Generar 20 habitaciones por tipo de habitación y piso
                # Calcula la capacidad basada en el piso (1, 2 o 3)
                capacidad = 1 + (piso % 3)

                # Realiza la inserción directa en la base de datos
                self.cursor.execute(
                    "INSERT INTO HABITACION (numero, precio, piso, capacidad, tipo_de_habitacion, disponibilidad) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (numero_habitacion, tarifa_base, piso, capacidad, tipo_habitacion, 'Disponible')
                )

                numero_habitacion += 1

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


# Metodos para actualizar el estado de las habitaciones al iniciar el programa
  def verificar_y_actualizar_disponibilidad(self):
        habitaciones_actualizadas = []  # Lista para almacenar las habitaciones actualizadas

        try:
            # Obtén la fecha y hora actual
            now = datetime.now()

            # Consulta la base de datos para obtener reservas y hospedajes con fecha de check-out pasada
            self.cursor.execute("SELECT id, habitacion_id FROM RESERVA WHERE fechaCheckout <= ?", (now,))
            reservas = self.cursor.fetchall()

            for reserva in reservas:
                reserva_id, habitacion_id = reserva
                # Realiza el check-out y actualiza la disponibilidad de la habitación correspondiente
                self.actualizar_disponibilidad_habitacion_check_out(habitacion_id)
                habitaciones_actualizadas.append(habitacion_id)  # Agrega la habitación actualizada a la lista
        except sqlite3.Error as e:
            print("Error al verificar y actualizar disponibilidad:", e)

        return habitaciones_actualizadas  # Devuelve la lista de habitaciones actualizadas

  def actualizar_disponibilidad_habitacion_check_out(self, habitacion_id):
        try:
            self.cursor.execute("UPDATE HABITACION SET disponibilidad=? WHERE id=?", ("Disponible", habitacion_id))
            self.conexion.commit()
            print(f"La disponibilidad de la habitación con ID {habitacion_id} se ha actualizado a 'Disponible'.")
        except sqlite3.Error as e:
            print("Error al actualizar la disponibilidad de la habitación:", e)



  def actualizar_disponibilidad_reservas_activas(self):
        habitaciones_actualizadas = []  # Lista para almacenar las habitaciones actualizadas
        now = datetime.now()

        try:
            # Consulta la base de datos para obtener reservas activas con fecha de check-in anterior o igual y fecha de check-out posterior o igual a la fecha actual
            self.cursor.execute("SELECT r.id, r.habitacion_id FROM RESERVA r WHERE r.fechaChekin <= ? AND r.fechaCheckout >= ?", (now, now))
            reservas_activas = self.cursor.fetchall()

            for reserva in reservas_activas:
                reserva_id, habitacion_id = reserva
                # Realiza la actualización de disponibilidad para cada habitación asociada a una reserva activa
                self.actualizar_disponibilidad_habitacion(reserva_id, habitacion_id)
                habitaciones_actualizadas.append(habitacion_id)

        except sqlite3.Error as e:
            print("Error al actualizar la disponibilidad de las habitaciones:", e)

        return habitaciones_actualizadas  # Devuelve la lista de habitaciones actualizadas

  def actualizar_disponibilidad_habitacion(self, reserva_id, habitacion_id):
        try:
            # Realiza el check-out y actualiza la disponibilidad de la habitación
            self.cursor.execute("UPDATE HABITACION SET disponibilidad=? WHERE id=?", ("Disponible", habitacion_id))
            self.conexion.commit()
            print(f"La disponibilidad de la habitación con ID {habitacion_id} se ha actualizado a 'Disponible' debido a la reserva con ID {reserva_id}.")
        except sqlite3.Error as e:
            print("Error al actualizar la disponibilidad de la habitación:", e)

# Metodos para actualizar el estado de las habitaciones al iniciar el programa

#Metodo para calcular la facturacion
  def calcular_precio_habitacion(tipo_habitacion, num_personas):
    # Consulta la base de datos para obtener las tarifas
    tarifa_base = obtener_tarifa_base(tipo_habitacion)
    tarifa_por_persona = obtener_tarifa_por_persona(tipo_habitacion)
    
    # Calcula el precio total
    precio_total = tarifa_base + (tarifa_por_persona * (num_personas - 1))
    
    return precio_total
  
#Metodo para calcular la facturacion