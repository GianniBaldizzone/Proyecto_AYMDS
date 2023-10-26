from ValidacionesHabitaciones import ValidacionesHabitaciones
from bd import Conexion


class Menu:
  
  #menu principal
  def mostrar_menu(self):
    bucle = 0

    while bucle != 1:
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
        self.mostrar_actividades()
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

  def mostrar_reservas(self):
    bucle = 0

    while bucle != 1:
      print(f"=== Menú Reserva ===")
      print("Seleccione una opción:")
      print("1. Ver reservas")
      print("2. Hacer una reserva")
      print("3. Cancelar reserva")
      print("4. Modificar reserva")
      print("5. Volver")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.ver_reservas()
      elif eleccion == "2":
        self.hacer_reserva()
      elif eleccion == "3":
        self.modificar_reserva()
      elif eleccion == "4":
        self.eliminar_reserva()
      elif eleccion == "5":
        print("Volviendo...")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def ver_reservas(self):
    print("Mostrando reservas...")
    print("\n")

  def hacer_reserva(self):
    print("Haciendo reserva...")
    print("\n")

  def modificar_reserva(self):
    print("Modificando reserva...")
    print("\n")

  def eliminar_reserva(self):
    print("Eliminando reserva...")
    print("\n")
#menu reservas
#menu hospedaje

  def mostrar_hospedaje(self):
    bucle = 0

    while bucle != 1:
      print(f"=== Menú Hospedajes ===")
      print("Seleccione una opción:")
      print("1. Ver hospedajes")
      print("2. Hacer nuevo Check_in")
      print("3. Modificar Check-in")
      print("4. Eliminar Check-in")
      print("5. Volver")

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
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def ver_hospedajes(self):
    print("Mostrar hospedajes...")
    print("\n")

  def check_in(self):
    print("Haciendo el Check-in...")
    print("\n")

  def modificar_checkin(self):
    print("Modificando Check-in...")
    print("\n")

  def eliminar_checkin(self):
    print("Eliminando Check-in...")
    print("\n")
#menu hospedaje
#menu actividades

  def mostrar_actividades(self):
    bucle = 0

    while bucle != 1:
      print(f"=== Menú Actividades ===")
      print("Seleccione una opción:")
      print("1. Ver Actividades disponibles")
      print("2. Ver reservas")
      print("3. Reservar actividad")
      print("4. Modificar reserva")
      print("5. Eliminar reserva")
      print("6. Volver")

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
    print("Mostrando actividades disponibles...")
    print("\n")

  def ver_reservas_actividades(self):
    print("Mostrando reservas de actividades...")
    print("\n")

  def hacer_reserva_de_actividades(self):
    print("Realizando reserva de actividades...")
    print("\n")

  def modificar_reserva_actividades(self):
    print("Modificando reserva de actividades...")
    print("\n")

  def eliminar_reserva_actividades(self):
    print("Eliminando reserva de actividades...")
    print("\n")
#menu actividades
#menu limpieza

  def mostrar_limpieza(self):
    bucle = 0

    while bucle != 1:
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
      print(f"=== Menú ABM ===")
      print("Seleccione una opción:")
      print("1. Habitaciones")
      print("2. Empleados")
      print("3. Volver")
      print("\n")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        self.mostrar_menu_habitacion()
      elif eleccion == "2":
        self.mostrar_menu_empleado()
      elif eleccion == "3":
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
        capacidadMaxima = validacion.validacionCantidadMaxima()
        tipoDeHabitacion = validacion.validacion_tipo_de_habitacion()
        conexion.IngresarHabitacion(numero, precio, piso, capacidadMaxima, tipoDeHabitacion)
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
                f"ID: {habitacion[0]}, Número: {habitacion[1]}, Precio: {habitacion[2]}, Piso: {habitacion[3]}, Estado de Limpieza: {habitacion[4]}, Capacidad Actual: {habitacion[5]}, Capacidad Máxima: {habitacion[6]}, Tipo de Habitación: {habitacion[7]}"
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
        nombre = input("Ingresar nombre")
        apellido = input("Ingresar apellido")
        dni = input("Ingresar dni")
        isAdmin = input("Ingresar isAdmin")
        telefono = input("Ingresar telefono")
        
        conexion.IngresarEmpleados(nombre, apellido, dni, isAdmin,telefono)
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
                f"ID: {empleado[0]}, Nombre: {empleado[1]}, Apellido: {empleado[2]}, Dni: {empleado[3]}, Es Admin: {empleado[4]}, Telefono: {empleado[5]}"
            )
            print("\n")
        else:
          print("No hay empleados")
          print("\n")
      elif eleccion == "5":
        print("Volviendo...")
        print("\n")
        self.mostrar_menu()
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )


#menu abm - empleados
#menu abm
