from ValidacionesHuesped import ValidacionesHuesped
from ValidacionesHabitaciones import ValidacionesHabitaciones
from bd import Conexion
from datetime import datetime
from ValidacionesEmpleado import ValidacionesEmpleado
from ValidacionesReserva import ValidacionesReserva
from ValidacionesActividades import ValidacionesActividades

class Menu:

  def __init__(self, nombre_empleado, contrasena_empleado, id_empleado):
        self.nombre_empelado = nombre_empleado
        self.contrasena_empleado = contrasena_empleado
        self.id_empleado = id_empleado
  
  #menu principal
  def mostrar_menu(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú principal ===")
      print("Seleccione una opción:")
      print("1. Reserva")
      print("2. Hospedaje")
      print("3. Actividades")
      print("4. Limpieza")
      print("5. ABM")
      print("6. Salir")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")
      print("\n")

      if eleccion == "1":
        self.mostrar_reservas()
      elif eleccion == "2":
        self.mostrar_hospedaje()
      elif eleccion == "3":
        self.mostrar_menu_actividades()
      elif eleccion == "4":
        self.mostrar_limpieza()
      elif eleccion == "5":
        self.mostrar_abm()
      elif eleccion == "6":
        bucle = 1
        print("¡Hasta luego!")

      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
#menu principal
#menu reservas
  ###
  def mostrar_reservas(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú Reserva ===")
      print("Seleccione una opción:")
      print("1. Ver reservas")
      print("2. Hacer una reserva")
      print("3. Cancelar reserva")
      print("4. Modificar reserva")
      print("5. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        print("Ingresaste a la lista de reservas")
        self.ver_reservas()
      elif eleccion == "2":
        print("Ingresaste al menú realizar reservas")
        self.hacer_reserva()
      elif eleccion == "3":
        print("Ingresaste al menú para eliminar reservas")
        self.eliminar_reserva()
      elif eleccion == "4":
        print("Ingresaste al menú para modificar reservas")
        self.modificar_reserva()
      elif eleccion == "5":
        print("Volviendo...")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def ver_reservas(self):
    print("### Listado de reservas ###")
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaReserva()
    reservas = conexion.ConsultarReservasReserva()

    if len(reservas) > 0:
      for reserva in reservas:
        print(
          f"ID Reserva: {reserva[0]}, Empleado ID: {reserva[1]}, Fecha checkin: {reserva[2]}, Fecha checkout: {reserva[3]}, ID Habitacion: {reserva[4]}, Estado: {reserva[5]}, ID Huesped: {reserva[6]}, Tipo de Reserva: {reserva[7]}"
          )
        print("\n")
    else:
      print("No hay reservas registradas")
      print("\n")
    print("\n")

  def hacer_reserva(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    empleado_id = ValidacionesEmpleado.validar_ID()
    fecha_checkin = ValidacionesReserva.validar_checkin() 
    fecha_checkout = ValidacionesReserva.validar_checkout(fecha_checkin) 
    habitacion_id = ValidacionesHabitaciones.validaciones_id_hab()
    estado = ValidacionesHabitaciones.validaciones_estado_hab()
    huesped_id = ValidacionesHuesped.validaciones_id_huesp()
    tipo_reserva = "Reserva"
    
    conexion.IngresarReserva(empleado_id, fecha_checkin, fecha_checkout,habitacion_id, estado, huesped_id, tipo_reserva)
    print("\n")

  def modificar_reserva(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    numeroID = ValidacionesReserva.validar_id_reserva()
    bucle = 0
    while bucle != 1:
      print("\n")
      print("Seleccione una opción a modificar:")
      print("1. Empleado ID")
      print("2. Fecha checkin")
      print("3. Fecha checkout")
      print("4. Habitacion ID")
      print("5. Estado")
      print("6. Huesped ID")
      print("7. Tipo de reserva")
      print("8. Salir de modificar")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")
      print("\n")

      if eleccion == "1":
        campo = "empleado_id"
      elif eleccion == "2":
        campo = "fecha_checkout"
      elif eleccion == "3":
        campo = "habitacion_id"
      elif eleccion == "4":
        campo = "estado"
      elif eleccion == "5":
        campo = "huesped_id"
      elif eleccion == "6":
        campo = "tipo_reserva"
      elif eleccion == "7":
        bucle = 1
        print("Has salido del menu modificar huesped")

      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

      print("\n")
      if eleccion != "8":
        print("\n")
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}:")
        campo = ValidacionesReserva.validar_campos(campo)
        conexion.ModificarReservas(numeroID, campo, nuevo_valor)
        print(f"Se ha modificado el campo {campo} satisfactoriamente.")
        print("\n")
        print("\n")
    conexion.ModificarReservas(numeroID, campo, nuevo_valor)
    
    print("\n")

  def eliminar_reserva(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    print("\n")
    numeroID = ValidacionesReserva.validar_id_reserva()
    print("\n")
    conexion.EliminarReserva(numeroID)
    print("\n")
#menu reservas
#menu hospedaje

  def mostrar_hospedaje(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú Hospedajes ===")
      print("Seleccione una opción:")
      print("1. Ver hospedajes")
      print("2. Hacer nuevo Check_in")
      print("3. Modificar Check-in")
      print("4. Eliminar Check-in")
      print("5. Mostrar Check-in")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.ver_hospedajes()
      elif eleccion == "2":
        self.check_in()
      elif eleccion == "3":
        self.modificar_checkin()
      elif eleccion == "4":
        self.eliminar_checkin()
      elif eleccion == "5":
        self.mostrar_checkin()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def ver_hospedajes(self):
    print("### Listado de hospedajes ###")
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaReserva()
    reservas = conexion.ConsultarReservasHospedaje()

    if len(reservas) > 0:
      for reserva in reservas:
        print(
          f"ID Reserva: {reserva[0]}, Empleado ID: {reserva[1]}, Fecha checkin: {reserva[2]}, Fecha checkout: {reserva[3]}, ID Habitacion: {reserva[4]}, Estado: {reserva[5]}, ID Huesped: {reserva[6]}, Tipo de Reserva: {reserva[7]}"
          )
        print("\n")
    else:
      print("No hay hospedajes registrados")
      print("\n")
    print("\n")
    
  ## CHECKIN ##
  def check_in(self):
    print("=== Crear Check-in ===")
    print("\n")
    ValidacionesHuesped()
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    nombre = ValidacionesHuesped.validar_nombre()
    apellido = ValidacionesHuesped.validar_apellido()
    nacionalidad = ValidacionesHuesped.validar_nacionalidad()
    if nacionalidad == "Argentina" or nacionalidad == "Otro - Argentina":
      dni = ValidacionesHuesped.validar_dni()
      grupo_sanguineo = ValidacionesHuesped.validar_grupo_sanguineo()
      seguro_vida = ValidacionesHuesped.validar_seguro_vida()
      huesped_id =conexion.IngresarHuesped(nombre, apellido, None, dni, nacionalidad, grupo_sanguineo, seguro_vida)
    else:
      numero_de_pasaporte = ValidacionesHuesped.validar_numero_pasaporte()
      grupo_sanguineo = ValidacionesHuesped.validar_grupo_sanguineo()
      seguro_vida = ValidacionesHuesped.validar_seguro_vida()
      huesped_id =conexion.IngresarHuesped(nombre, apellido, numero_de_pasaporte, None, nacionalidad, grupo_sanguineo, seguro_vida)
   
    

    empleado_id = self.id_empleado
    fecha_checkin = ValidacionesReserva.validar_checkin() 
    fecha_checkout = ValidacionesReserva.validar_checkout(fecha_checkin) 
    habitacion_id = conexion.obtener_id_habitacion_por_numero()
    estado = ValidacionesHabitaciones.validaciones_estado_hab()
    tipo_reserva = "Hospedaje"
    
    conexion.IngresarReserva(empleado_id, fecha_checkin, fecha_checkout,habitacion_id, estado, huesped_id, tipo_reserva)
    print("\n")
    
    
  ## CHECKIN ##
  
  def modificar_checkin(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    ##si el numeroID no esta dentro de la base de datos, volver a ingresarlo
    while True:
        numeroID = input("Ingresar ID del huesped a modificar: ")
        
        if conexion.IDExists(numeroID):
            break  #sale del loop si es true
        else:
            print("El ID ingresado no existe en la base de datos. Por favor, inténtelo de nuevo.")
            print("\n")
    print("\n")
    
    bucle = 0
    while bucle != 1:
      print("\n")
      print("Seleccione una opción a modificar:")
      print("1. Nombre")
      print("2. Apellido")
      print("3. Pasaporte")
      print("4. DNI")
      print("5. Nacionalidad")
      print("6. Grupo Sanguineo")
      print("7. Seguro de vida")
      print("8. Salir de modificar")
      print("\n")
      
      eleccion = input("Ingrese el número de la opción: ")
      print("\n")

      if eleccion == "1":
        campo = "nombre"
      elif eleccion == "2":
        campo = "apellido"
      elif eleccion == "3":
        campo = "numero_pasaporte"
      elif eleccion == "4":
        campo = "dni"
      elif eleccion == "5":
        campo = "nacionalidad"
      elif eleccion == "6":
        campo = "grupo_sanguineo"
      elif eleccion == "7":
        campo = "seguro_vida"
      elif eleccion == "8":
        bucle = 1
        print("Has salido del menu modificar huesped")

      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
    
      print("\n")
      if eleccion != "8":
        print("\n")
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}:")
        conexion.ModificarHuespedes(numeroID, campo, nuevo_valor)
        print(f"Se ha modificado el campo {campo} satisfactoriamente.")
        print("\n")
        print("\n")

  def eliminar_checkin(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    print("\n")
    while True:
        numeroID = input("Ingresar ID del huesped a modificar/eliminar: ")
        
        if conexion.IDExists(numeroID):
            break  #sale del loop si es true
        else:
            print("El ID ingresado no existe en la base de datos. Por favor, inténtelo de nuevo.")
            print("\n")
    print("\n")
    
    conexion.HuespedEliminar(numeroID)
    print("\n")
    
  def mostrar_checkin(self):
    print("### Lista checkin - Huespedes ###")
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaHuesped()
    huespedes = conexion.MostrarHuespedes()

    if len(huespedes) > 0:
      for huesped in huespedes:
        print(
          f"ID: {huesped[0]}, Nombre: {huesped[1]}, Apellido: {huesped[2]}, Pasaporte: {huesped[3]}, DNI: {huesped[4]}, Nacionalidad: {huesped[5]}, Grupo sanguineo: {huesped[6]}, Seguro de vida: {huesped[7]}"
          )
        print("\n")
    else:
      print("No hay huespedes registrados")
      print("\n")

  #menu hospedaje
  #menu actividades

  def mostrar_menu_actividades(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú Actividades ===")
      print("Seleccione una opción:")
      print("1. Ver Actividades disponibles")
      print("2. Ver reservas")
      print("3. Reservar actividad")
      print("4. Modificar reserva")
      print("5. Eliminar reserva")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.mostrar_actividad()
      elif eleccion == "2":
        self.ver_reservas_actividades()
      elif eleccion == "3":
        self.hacer_reserva_de_actividades()
      elif eleccion == "4":
        self.modificar_reserva_actividades()
      elif eleccion == "5":
        self.eliminar_reserva_actividades()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def mostrar_actividad(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaActividad()
    actividades = conexion.MostrarActividades()
    print("## Listado de Actividades Disponibles ##")

    if len(actividades) > 0:
          for actividad in actividades:
            print(
                f"ID: {actividad[0]}, Nombre: {actividad[1]}, Tipo Actividad: {actividad[2]}, Capacidad: {actividad[3]}"
            )
            
    else:
          print("No hay actividades")
          print("\n")
    print("\n")

  def ver_reservas_actividades(self):
    print("## Listado de Reservas Actividades ##")
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaActividadReserva()
    reservas = conexion.MostrarActividadReserva()

    if len(reservas) > 0:
          for reserva in reservas:
            print(
                f"ID Reserva Actividad: {reserva[0]}, ID Actividad: {reserva[1]}, ID Reserva: {reserva[2]}"
            )
            print("\n")
    else:
          print("No hay reservas de actividades.")
          print("\n")
    
    print("\n")

  def hacer_reserva_de_actividades(self):
    validacion = ValidacionesActividades()
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaActividadReserva()
    actividad_id = validacion.validarActividadId()
    reserva_id = validacion.validarReservaId()
  
    conexion.IngresarReservaActividad(actividad_id, reserva_id)
    print("\n")

  def modificar_reserva_actividades(self):
    print("Modificando reserva de actividades...")
    print("\n")

  def eliminar_reserva_actividades(self):
    print("Eliminando reserva de actividades...")
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaActividadReserva()
    print("\n")
    while True:
        numeroID = input("Ingresar ID de la reserva a modificar/eliminar: ")
        
        if conexion.IDActividadReservaExiste(numeroID):
          break  #sale del loop si es true
        else:
            print("El ID ingresado no existe en la base de datos. Por favor, inténtelo de nuevo.")
            print("\n")
    print("\n")
    
    conexion.EliminarActividadReserva(numeroID)
    print("\n")
    
    
  #menu actividades
  #menu limpieza

  def mostrar_limpieza(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú Limpieza ===")
      print("Seleccione una opción:")
      print("1. Ver estado de las habitaciones")
      print("2. Ver habitaciones disponibles para limpieza")
      print("3. Modificar estado")
      print("4. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.mostrar_estado_de_habitaciones()
      elif eleccion == "2":
        self.mostrar_habitaciones_disponibles_para_limpieza()
      elif eleccion == "3":
        self.modificar_estado_de_las_habitaciones()
      elif eleccion == "4":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def mostrar_estado_de_habitaciones(self):
    print("Mostrando estados de las habitaciones...")
    print("\n")

  def mostrar_habitaciones_disponibles_para_limpieza(self):
    print("Mostrando habitaciones disponibles para limpiar...")
    print("\n")

  def modificar_estado_de_las_habitaciones(self):
    print("Modificando estado de la habitación...")
    print("\n")
  #menu limpieza
  #menu ABM

  def mostrar_abm(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM ===")
      print("Seleccione una opción:")
      print("1. Habitaciones")
      print("2. Empleados")
      print("3. Actividades")
      print("4. Huespedes")
      print("5. Control maestro BD")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.mostrar_menu_habitacion()
      elif eleccion == "2":
        self.mostrar_menu_empleado()
      elif eleccion == "3":
        self.mostrar_menu_abm_actividad()
      elif eleccion == "4":
        self.mostrar_menu_huesped()
      elif eleccion == "5":
        self.mostrar_menu_controlmaestro()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  #menu abm - habitaciones
  def mostrar_menu_habitacion(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Habitaciones ===")
      print("Seleccione una opción:")
      print("1. Crear Habitacion")
      print("2. Modificar Habitacion")
      print("3. Eliminar Habitacion")
      print("4. Mostrar Habitaciones")
      print("5. Filtrar Habitaciones")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        validacion = ValidacionesHabitaciones()
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        piso = validacion.validacionPiso()
        numero = validacion.validar_numero_habitacion(piso)
        precio = validacion.validacion_precio()
        capacidad = validacion.validacionCantidad()
        tipoDeHabitacion = validacion.validacion_tipo_de_habitacion()
        conexion.IngresarHabitacion(numero, precio, piso, capacidad, tipoDeHabitacion)
      elif eleccion == "2":
        print("Modificando habitacion ...")
      elif eleccion == "3":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        print("\n")
        numeroID= input("Ingresar ID a eliminar")
        print("\n")
        conexion.ModificarEliminar(numeroID)
      elif eleccion == "4":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        habitaciones = conexion.MostrarHabitaciones()

        if len(habitaciones) > 0:
          for habitacion in habitaciones:
            print(
                f"ID: {habitacion[0]}, Número: {habitacion[1]}, Precio: {habitacion[2]}, Piso: {habitacion[3]}, Capacidad: {habitacion[4]}, Tipo de Habitacion: {habitacion[5]}, Disponibilidad: {habitacion[6]}"
            )
            print("\n")
        else:
          print("No hay habitaciones")
          print("\n")

      elif eleccion == "5":
        self.mostrar_menu_habitaciones_filtros()

      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_abm()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
  #menu abm - habitaciones

  #menu filtros - habitaciones

  def mostrar_menu_habitaciones_filtros(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Habitaciones - Filtrar Habitaciones===")
      print("Seleccione una opción:")
      print("1. Filtrar por piso")
      print("2. Filtrar por cantidad Maxima")
      print("3. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        validacion = ValidacionesHabitaciones()
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        piso = validacion.validacionPiso()
        habitaciones = conexion.MostrarHabitacionesPorPiso(piso)

        if len(habitaciones) > 0:
          for habitacion in habitaciones:
            print(
                f"ID: {habitacion[0]}, Número: {habitacion[1]}, Precio: {habitacion[2]}, Piso: {habitacion[3]}, Estado de Limpieza: {habitacion[4]}, Capacidad Actual: {habitacion[5]}, Capacidad Máxima: {habitacion[6]}, Tipo de Habitación: {habitacion[7]}"
            )
            print("\n")

      elif eleccion == "2":
        validacion = ValidacionesHabitaciones()
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        capacidadMaxima = validacion.validacionCantidadMaxima()
        habitaciones = conexion.MostrarHabitacionesPorCantidadMaxima(
            capacidadMaxima)
        if len(habitaciones) > 0:
          for habitacion in habitaciones:
            print(
                f"ID: {habitacion[0]}, Número: {habitacion[1]}, Precio: {habitacion[2]}, Piso: {habitacion[3]}, Estado de Limpieza: {habitacion[4]}, Capacidad Actual: {habitacion[5]}, Capacidad Máxima: {habitacion[6]}, Tipo de Habitación: {habitacion[7]}"
            )
            print("\n")

      elif eleccion == "3":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu_habitacion()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
#menu filtros - habitaciones

#menu abm - empleados

  def mostrar_menu_empleado(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Empleados ===")
      print("Seleccione una opción:")
      print("1. Crear Empleado")
      print("2. Modificar Empleado")
      print("3. Eliminar Empleado")
      print("4. Mostrar Empleados")
      print("5. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        
        
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaEmpleados()
        
        nombre = input("Ingrese nombre del empleado: ")
        nombre = ValidacionesEmpleado.validar_nombre(nombre)
          
        apellido = input("Ingresar apellido: ")
        apellido = ValidacionesEmpleado.validar_apellido(apellido)
          
        dni = ValidacionesEmpleado.validar_dni()
        isAdmin = ValidacionesEmpleado.validar_administrador()
        telefono = ValidacionesEmpleado.validar_telefono()
        contrasena = ValidacionesEmpleado.validar_contrasena() 
        conexion.IngresarEmpleados(nombre, apellido, dni, isAdmin,telefono,contrasena)

      elif eleccion == "2":
        self.mostrar_menu_empleado()
      elif eleccion == "3":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaEmpleados()
        print("\n")
        numeroID= input("Ingresar ID a eliminar")
        print("\n")
        conexion.EmpleadoEliminar(numeroID)
      elif eleccion == "4":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaEmpleados()
        empleados = conexion.MostrarEmpleados()

        if len(empleados) > 0:
          for empleado in empleados:
            print(
                f"ID: {empleado[0]}, Nombre: {empleado[1]}, Apellido: {empleado[2]}, Dni: {empleado[3]}, Es Admin: {empleado[4]}, Telefono: {empleado[5]}, Contraseña: {empleado[6]}"
            )
            print("\n")
        else:
          print("No hay empleados")
          print("\n")
      elif eleccion == "5":
        print("Volviendo...")
        print("\n")
        self.mostrar_abm()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )


#menu abm - empleados

#menu abm - actividades
  def mostrar_menu_abm_actividad(self):
    bucle = 0
    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Actividades ===")
      print("Seleccione una opción:")
      print("1. Crear Actividad")
      print("2. Modificar Actividad")
      print("3. Eliminar Actividad")
      print("4. Mostrar Actividades")
      print("5. Filtrar Actividades")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
          validacion = ValidacionesActividades()
          nombreBD = "househunter.db"
          conexion = Conexion(nombreBD)
          conexion.CrearTablaActividad()
          nombre = validacion.validacionNombre()
          tipo_actividad = validacion.validarTipoActividad()
          #capacidad = input("Ingrese la capacidad:")
          #reserva_id = validacion.validarReservaId()
  
          conexion.IngresarActividad(nombre, tipo_actividad)
          
      elif eleccion == "2":
          self.modificar_actividad()
          
      elif eleccion == "3":
          nombreBD = "househunter.db"
          conexion = Conexion(nombreBD)
          conexion.CrearTablaActividad()
          print("\n")
          numeroID= input("Ingresar ID a eliminar")
          print("\n")
          conexion.EliminarActividad(numeroID)
          
      elif eleccion == "4":
          nombreBD = "househunter.db"
          conexion = Conexion(nombreBD)
          conexion.CrearTablaActividad()
          actividades = conexion.MostrarActividades()

          if len(actividades) > 0:
            for actividad in actividades:
              print(
                  f"ID: {actividad[0]}, Nombre: {actividad[1]}, Tipo de Actividad: {actividad[2]}, Capacidad: {actividad[3]} "
              )
              print("\n")
          else:
            print("No hay actividades disponibles.")
            print("\n")

      elif eleccion == "5":
          #self.mostrar_menu_habitaciones_filtros()
          print("Mostranfo filtros para activiades...")

      elif eleccion == "6":
          print("Volviendo...")
          print("\n")
          self.mostrar_abm()
      else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )

#metodos abm - actividades
  def modificar_actividad(self):
    nombreBD = "househunter.db"
    conexion = Conexion(nombreBD)
    conexion.CrearTablaActividad()
    print("\n")
    
    #########################################################################
    
    numeroID= ValidacionesActividades.validarActividadId()
    campo = ""
    bucle = 0
    while bucle != 1:
      print("\n")
      print("## Menú Modificar Actividad ##")
      print("Seleccione una opción a modificar:")
      print("1. Nombre de la actividad")
      print("2. Tipo de Actividad")
      print("3. Capacidad")
      print("4. Salir de modificar")
      print("\n")
      
      eleccion = input("Ingrese el número de la opción: ")
      print("\n")

      if eleccion == "1":
        campo = "nombre"
      elif eleccion == "2":
        campo = "tipo_actividad"
      elif eleccion == "3":
        campo = "capacidad"  
      elif eleccion == "4":
        bucle = 1
        print("Has salido del menu modificar actividad.")

      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
    
      print("\n")
      if eleccion != "4":
        print("\n")
        if campo != "tipo_actividad":
          nuevo_valor = input(f"Ingrese el nuevo valor para {campo}:")
        
        else:
          nuevo_valor = ""  
        nuevo_valor = ValidacionesActividades.validarCampos(campo, nuevo_valor)
        conexion.ModificaActividad(numeroID, campo, nuevo_valor)
        print(f"Se ha modificado el campo {campo} satisfactoriamente.")
        print("\n")
        print("\n")
    ##########################################################################
    
    
#menu abm - actividades

#menu abm - huesped
  def mostrar_menu_huesped(self):
          bucle = 0

          while bucle != 1:
              print("\n")
              print(f"=== Menú ABM - Huéspedes ===")
              print("Seleccione una opción:")
              print("1. Crear Huésped")
              print("2. Modificar Huésped")
              print("3. Eliminar Huésped")
              print("4. Mostrar Huéspedes")
              print("5. Filtrar Huéspedes")
              print("6. Volver")
              print("\n")

              eleccion = input("Ingrese el número de la opción: ")

              if eleccion == "1":
                ValidacionesHuesped()
                nombreBD = "househunter.db"
                conexion = Conexion(nombreBD)
                conexion.CrearTablaHuesped()
                nombre = ValidacionesHuesped.validar_nombre()
                apellido = ValidacionesHuesped.validar_apellido()
                nacionalidad = ValidacionesHuesped.validar_nacionalidad()
                if nacionalidad == "Argentina" or nacionalidad == "Otro - Argentina":
                  dni = ValidacionesHuesped.validar_dni()
                  grupo_sanguineo = ValidacionesHuesped.validar_grupo_sanguineo()
                  seguro_vida = ValidacionesHuesped.validar_seguro_vida()
                  conexion.IngresarHuesped(nombre, apellido, None, dni, nacionalidad, grupo_sanguineo, seguro_vida)
                else:
                  numero_de_pasaporte = ValidacionesHuesped.validar_numero_pasaporte()
                  grupo_sanguineo = ValidacionesHuesped.validar_grupo_sanguineo()
                  seguro_vida = ValidacionesHuesped.validar_seguro_vida()
                  conexion.IngresarHuesped(nombre, apellido, numero_de_pasaporte, None, nacionalidad, grupo_sanguineo, seguro_vida)

              elif eleccion == "2":
                  print("Modificando huésped ...")
                  # Lógica para modificar huésped

              elif eleccion == "3":
                  nombreBD = "househunter.db"
                  conexion = Conexion(nombreBD)
                  conexion.CrearTablaHuesped()
                  print("\n")
                  self.eliminar_checkin()
                  
            

              elif eleccion == "4":
                  nombreBD = "househunter.db"
                  conexion = Conexion(nombreBD)
                  conexion.CrearTablaHuesped()
                  huespedes = conexion.MostrarHuespedes()

                  if len(huespedes) > 0:
                      for huesped in huespedes:
                          print(
                              f"ID: {huesped[0]}, Nombre: {huesped[1]}, Apellido: {huesped[2]}, Número de Pasaporte: {huesped[3]}, DNI: {huesped[4]}, Nacionalidad: {huesped[5]}, Grupo Sanguíneo: {huesped[6]}, Seguro de Vida: {'Sí' if huesped[7] else 'No'}"
                          )
                          print("\n")
                  else:
                      print("No hay huéspedes")
                      print("\n")

              elif eleccion == "5":
                  self.mostrar_menu_huespedes_filtros()

              elif eleccion == "6":
                  print("Volviendo...")
                  print("\n")
                  self.mostrar_abm()
              else:
                  print(
                      "Error: Opción no válida. Por favor, seleccione una opción válida."
                  )
#menu abm - huesped




#Menu contro maestro
def mostrar_menu_controlmaestro(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Control maestror ===")
      print("Seleccione una opción:")
      print("1. Crear tablas")
      print("2. Eliminar tablas")
      print("3. Setear tablas")
      print("4. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":  
        self.mostrar_menu_controlmaestro_crear()
        
      elif eleccion == "2":
        self.mostrar_menu_controlmaestro_eliminar()
      elif eleccion == "3":
        self.mostrar_menu_controlmaestro_setear()()
      elif eleccion == "4":
        print("Volviendo...")
        print("\n")
        self.mostrar_abm()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
#Menu contro maestro

#menu ABM - Menu contro maestro - Eliminar
def mostrar_menu_controlmaestro_eliminar(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Control maestro - Eliminar ===")
      print("Seleccione una opción:")
      print("1. Eliminar tabla Habitacion")
      print("2. Eliminar tabla Reserva")
      print("3. Eliminar tabla Empleado")
      print("4. Eliminar tabla Actividad")
      print("5. Eliminar tabla Huesped")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":  
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.EliminarTablaHabitacion()
        
      elif eleccion == "2":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.EliminarTablaReserva()
      elif eleccion == "3":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.EliminarTablaEmpleados()
      elif eleccion == "4":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaActividad()
      elif eleccion == "5":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHuesped()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu_controlmaestro()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

#menu ABM - Menu contro maestro - Eliminar

#menu ABM - Menu contro maestro - Crear


def mostrar_menu_controlmaestro_crear(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Control maestro - Crear ===")
      print("Seleccione una opción:")
      print("1. Crear tabla Habitacion")
      print("2. Crear tabla Reserva")
      print("3. Crear tabla Empleado")
      print("4. Crear tabla Actividad")
      print("5. Crear tabla Huesped")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":  
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        
      elif eleccion == "2":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaReserva()
      elif eleccion == "3":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaEmpleados()
      elif eleccion == "4":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaActividad()
      elif eleccion == "5":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHuesped()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu_controlmaestro()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

#menu ABM - Menu contro maestro - crear


#menu ABM - Menu contro maestro - Setear


def mostrar_menu_controlmaestro_setear(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Control maestro - Setear ===")
      print(f"=== Utilizar estos metodos al tener tablas vacias ===")
      print("Seleccione una opción:")
      print("1. Setear tabla Habitacion")
      print("2. Setear tabla Reserva")
      print("3. Setear tabla Empleado")
      print("4. Setear tabla Actividad")
      print("5. Setear tabla Huesped")
      print("6. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":  
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.InsertarDatosPruebaHabitacion()
        
      elif eleccion == "2":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.InsertarDatosPruebaReserva()
      elif eleccion == "3":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.InsertarDatosPruebaEmpleados()
      elif eleccion == "4":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.InsertarDatosPruebaActividad()
      elif eleccion == "5":
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.InsertarDatosPruebaHuesped()
      elif eleccion == "6":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu_controlmaestro()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

#menu ABM - Menu contro maestro - Setear


#menu abm huesped filtros
def mostrar_menu_huespedes_filtros(self):
    bucle = 0

    while bucle != 1:
      print("\n")
      print(f"=== Menú ABM - Huespedes - Filtrar Huespedes===")
      print("Seleccione una opción:")
      print("1. Filtrar por ID")
      print("2. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        validacion = ValidacionesHabitaciones()
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        conexion.CrearTablaHabitacion()
        piso = validacion.validacionPiso()
        habitaciones = conexion.MostrarHabitacionesPorPiso(piso)

        if len(habitaciones) > 0:
          for habitacion in habitaciones:
            print(
                f"ID: {habitacion[0]}, Número: {habitacion[1]}, Precio: {habitacion[2]}, Piso: {habitacion[3]}, Estado de Limpieza: {habitacion[4]}, Capacidad Actual: {habitacion[5]}, Capacidad Máxima: {habitacion[6]}, Tipo de Habitación: {habitacion[7]}"
            )
            print("\n")

      elif eleccion == "2":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu_habitacion()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )
#menu abm huesped filtros