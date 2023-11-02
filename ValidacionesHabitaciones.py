from bd import Conexion

class ValidacionesHabitaciones:

  def validacionPiso(self):
    bucle1 = True

    while bucle1:
      print("*** Ingresar piso ***")
      print("Piso 0")
      print("Piso 1")
      print("Piso 2")
      print("Piso 3")
      print("Piso 4")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "0":
        piso = 0
        print("El piso seleccionado fue 0")
        return piso
        bucle1 = False
      elif eleccion == "1":
        piso = 1
        print("El piso seleccionado fue 1")
        return piso
        bucle1 = False
      elif eleccion == "2":
        piso = 2
        print("El piso seleccionado fue 2")
        return piso
        bucle1 = False
      elif eleccion == "3":
        piso = 3
        print("El piso seleccionado fue 3")
        return piso
        bucle1 = False
      elif eleccion == "4":
        piso = 4
        print("El piso seleccionado fue 4")
        return piso
        bucle1 = False
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  def validacionCantidad(self):
    bucle2 = 0

    while bucle2 != 1:
      print(f"*** Ingresar Cantidad Maxima ***")
      print("1 Personas")
      print("2 Personas")
      print("3 Personas")

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        cantMaxima = 1
        return cantMaxima
      elif eleccion == "2":
        cantMaxima = 2
        return cantMaxima
      elif eleccion == "3":
        cantMaxima = 3
        return cantMaxima
      else:
        print(
            "Error Opción no válida ---> Por favor seleccione una opción válida"
        )

  

    
  def validacion_precio(self):
      bucle2 = 0

      while bucle2 != 1:
        print(f"*** Ingresar Precio ***")
        print("No se puede asignarle mas de 50.000 pesos")
        eleccion = input("Ingrese el número de la opción: ")
        numero = float(eleccion)
        if numero <= 50000 and numero >0:
          print ("Precio ingresado con exito!!!")
          return numero
        else:  
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
  
  def validacion_tipo_de_habitacion(self):
      bucle2 = 0

      while bucle2 != 1:
        print(f"*** Ingresar tipo de habitacion ***")
        print("1. Plata")
        print("2. Gold")
        print("3. Diamante")

        eleccion = input("Ingrese el número de la opción: ")

        if eleccion == "1":
          tipoDeHabitacion= "Plata"
          return tipoDeHabitacion
        elif eleccion == "2":
          tipoDeHabitacion = "Oro"
          return tipoDeHabitacion

        elif eleccion == "3":
          tipoDeHabitacion = "Diamante"
          return tipoDeHabitacion
        else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
          
  def validaciones_id_hab():
      nombreBD = "househunter.db"
      conexion = Conexion(nombreBD)
      while True:
        habitacion_id = input("Ingrese el ID de la habitacion:")
        if habitacion_id is None:
          print("Error: Parece que no has ingresado ningún ID.")
          print("Por favor, ingrese un dato válido.")
          continue
         # Validar que el id sea un número entero mayor que 0
        try:
              habitacion_id = int(habitacion_id)  # Intenta convertir el valor a un entero
              if habitacion_id <= 0:
                  print("Error: El ID debe ser un número entero mayor que 0.")
                  print("Por favor, ingrese un dato válido.")
                  continue
        except ValueError:
              print("Error: El ID debe ser un número entero mayor que 0.")
              print("Por favor, ingrese un dato válido.")
              continue

        if not conexion.existeIDHab(habitacion_id):
              print("Error: La habitación con el ID proporcionado no existe en la base de datos.")
              print("Por favor, ingrese un dato válido.")
              continue
        return habitacion_id
  
  def validaciones_estado_hab():
    bucle = True

    while bucle:
      print("*** Seleccionar Tipo de Estado ***")
      print("1. Disponible")
      print("2. Ocupado")
            

      eleccion = input("Ingrese el número de la opción: ")

      if eleccion == "1":
        estado = "Disponible"
        print("El tipo de estado seleccionado fue Disponible.")
        return estado
      elif eleccion == "2":
        estado = "Actividad"
        print("El tipo de reserva seleccionado fue Actividad.")
        return estado
      else:
        print("Error: Opción no válida. Por favor, seleccione una opción válida.")
      
      
  def validar_numero_habitacion(self, piso):

    if piso == 0:
      bucle4 = 0
  
      while bucle4 != 1:
        print(f"*** Ingresar numero de habitación ***")
        print("***El rango es entre 1 y 20 segun tu piso***")
        eleccion = input("Ingrese el número : ")
        numero = int(eleccion)
        if numero >= 1 and numero <= 20:
          return numero
        else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
    elif piso == 1:
      bucle4 = 0
  
      while bucle4 != 1:
        print(f"*** Ingresar numero de habitación ***")
        print("***El rango es entre 101 y 120 segun tu piso***")
        eleccion = input("Ingrese el número : ")
        numero = int(eleccion)
        if numero >= 101 and numero <= 120:
          return numero
        else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
  
    elif piso == 2:
      bucle4 = 0
  
      while bucle4 != 1:
        print(f"*** Ingresar numero de habitación ***")
        print("***El rango es entre 201 y 220 segun tu piso***")
        eleccion = input("Ingrese el número : ")
        numero = int(eleccion)
        if numero >= 201 and numero<= 220:
          return numero
        else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
  
    elif piso == 3:
      bucle4 = 0
  
      while bucle4 != 1:
        print("\n")
        print(f"*** Ingresar numero de habitación ***")
        print("***El rango es entre 301 y 320 segun tu piso***")
        eleccion = input("Ingrese el número : ")
        numero = int(eleccion)
        if numero >= 301 and numero <= 320:
          return numero
        else:
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
  
    elif piso == 4:
      bucle4 = 0
  
      while bucle4 != 1:
        print(f"*** Ingresar numero de habitación ***")
        print("***El rango es entre 301 y 320 segun tu piso***")
        eleccion = input("Ingrese el número : ")
        numero = int(eleccion)
        if numero>=401 and numero<=20:
          return numero
        else:
          print("\n")
          print(
              "Error Opción no válida ---> Por favor seleccione una opción válida"
          )
          print("\n")
  
    else:
      print("\n")
      print("Error no identificado ---> el piso fue mal seleccionado")
      print("\n")


    
  @staticmethod
  def validarHabitacionId():
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        
        while True:
            habitacion_id = input("Ingrese el ID de la habitacion: ")
            
                # Validar que el id no sea nulo
            if habitacion_id is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                habitacion_id = int(habitacion_id)  # Intenta convertir el valor a un entero
                if habitacion_id <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            if not conexion.existeIDHab(habitacion_id):
                print("Error: La habitacion con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            return habitacion_id
           
  
  #modificar este metodo
  @staticmethod
  def validarCampos(campo,nuevo_valor):
        while True:
            
                # Validar que el id no sea nulo
            if nuevo_valor is None:
                print("Error: Parece que no has ingresado ningún valor.")
                print("Por favor, ingrese un dato válido.")
                continue
            
            if campo == "nombre":
                while True:
                    if nuevo_valor.strip().isalpha():
                        return nuevo_valor.strip()
                    else:
                        print("Error: El nombre no puede estar vacío y debe contener solo letras.")
                        nuevo_valor = input("Por favor, ingrese el nombre nuevamente: ")
                        
            elif campo == "tipo_actividad":
                bucle = True

                while bucle:
                        print("*** Seleccionar Tipo de Actividad***")
                        print("1. Paga")
                        print("2. Gratuita")
                        
                        nuevo_valor = input("Ingrese el número de la opción: ")

                        if nuevo_valor == "1":
                            tipo_actividad = "Paga"
                            print("El tipo de actividad seleccionado fue Paga.")
                            return tipo_actividad
                            
                        elif nuevo_valor == "2":
                            tipo_actividad = "Gratuita"
                            print("El tipo de actividad seleccionado fue Gratuita.")
                            return tipo_actividad
                    
                        else:
                            print("Error: Opción no válida. Por favor, seleccione una opción válida.")
                            
            elif campo == "capacidad":
                while True:
                    if nuevo_valor.isdigit() and int(nuevo_valor) > 0 and int(nuevo_valor) <= 14:
                        return int(nuevo_valor)
                    else:
                        print("Error: La capacidad tiene que ser un entero entre el 1 y 14.")
                        nuevo_valor = input("Ingrese nuevamente la capacidad:")
                  
                 
                        
            else:
                print(
                    "Error Opción no válida ---> Por favor seleccione una opción válida"
                )

#def validar_numero_habitacion(piso):
  #if piso in {0, 1, 2, 3, 4}:
      #rango_min = piso * 100 + 1
      #rango_max = piso * 100 + 20
      #bucle4 = 0

      #while bucle4 != 1:
          #print(f"*** Ingresar número de habitación ***")
          #print(f"*** El rango es entre {rango_min} y {rango_max} según tu piso ({piso}) ***")
         # eleccion = input("Ingrese el número: ")

          #if eleccion.isdigit():
              #numero = int(eleccion)
              #if rango_min <= numero <= rango_max:
                  #return numero
              #else:
                  #print("Error: El número de habitación no está dentro del rango válido. Por favor, seleccione un número válido.")
          #else:
              #print("Error: La entrada no es un número válido. Por favor, ingrese un número válido.")
  #else:
      #print("\n")
      #print("Error no identificado ---> el piso fue mal seleccionado")
      #print("\n")