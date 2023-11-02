from bd import Conexion
from datetime import datetime
from datetime import datetime, timedelta
class ValidacionesReserva:
    
    

    def validar_checkin_reserva():
        fecha_checkin = None
        fecha_actual = datetime.now()
        fecha_minima = fecha_actual + timedelta(days=7)
        print("Fecha de check-in")

        while fecha_checkin is None or fecha_checkin < fecha_minima:
            try:
                año = int(input("Ingrese el año: "))
                mes = int(input("Ingrese el mes: "))
                dia = int(input("Ingrese el día: "))
                hora = int(input("Ingrese la hora: "))
                minutos = int(input("Ingrese los minutos: "))


                if año < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31 or hora < 0 or hora > 23 or minutos < 0 or minutos > 59:
                    print("Error: Valores de fecha y hora no válidos. Por favor, ingrese nuevamente.")
                    continue

                fecha_checkin = datetime(año, mes, dia, hora, minutos)

                if fecha_checkin < fecha_minima:
                    print("Error: La fecha de check-in debe ser al menos 7 días después de la fecha actual. Por favor, ingrese nuevamente.")
                else:
                    print("Fecha válida.")

            except ValueError:
                print("Error: Ingrese valores numéricos válidos. Por favor, ingrese nuevamente.")

        return fecha_checkin
    
    
    
    
    
    
    
    
    
    
    
    #El metodo valida que la fecha de chekin sea a las 10 am del mismo dia, si pasaron las 10 del dia actual valida que sean las 10 am de mañana
    
    @staticmethod
    def validar_checkin():
        bucle = 0
        fecha_checkin = None
        fecha_actual = datetime.now()
        fecha_minima_hoy = datetime(fecha_actual.year, fecha_actual.month, fecha_actual.day, 10, 0)  # Hoy a las 10:00 AM
        fecha_minima_manana = fecha_actual + timedelta(days=1)
        fecha_minima_manana = datetime(fecha_minima_manana.year, fecha_minima_manana.month, fecha_minima_manana.day, 10, 0)  # Mañana a las 10:00 AM

        print("Fecha de check-in")

        while bucle != 1:
            try:
                año = int(input("Ingrese el año: "))
                mes = int(input("Ingrese el mes: "))
                dia = int(input("Ingrese el día: "))
                hora = int(10)  # Fijar la hora en 10:00 AM
                minutos = int(0)  # Fijar los minutos en 0

                fecha_checkin = datetime(año, mes, dia, hora, minutos)

                if (fecha_actual.time() < datetime(fecha_actual.year, fecha_actual.month, fecha_actual.day, 10, 0).time() and fecha_checkin.date() == fecha_actual.date()) or fecha_checkin == fecha_minima_manana:
                    bucle = 1
                    print("Fecha válida.")
                    print(fecha_checkin)
                else:
                    print("Error: La fecha de check-in debe ser a las 10:00 AM del día actual o del día siguiente en caso de que sea después de las 10:00 AM. Por favor, ingrese nuevamente.")

            except ValueError:
                print("Error: Ingrese valores numéricos válidos. Por favor, introduzca la fecha en números.")

        return fecha_checkin
    
    @staticmethod
    def validar_checkout(fecha_checkin):
        bucle = 0
        fecha_checkout = None
        hora_checkout = 14  # Hora fija a las 14:00 (2:00 PM)
        minutos_checkout = 0  # Minutos fijos en 0

        print("Fecha checkout")

        while bucle != 1:
            try:
                año = int(input("Ingrese el año: "))
                mes = int(input("Ingrese el mes: "))
                dia = int(input("Ingrese el día: "))

                fecha_checkout = datetime(año, mes, dia, hora_checkout, minutos_checkout)

                if fecha_checkout.date() >= fecha_checkin.date() + timedelta(days=1):
                    bucle = 1
                    print("Fecha válida.")
                    print(fecha_checkout)
                else:
                    print("Error: La fecha de check-out debe tener como mínimo un día de diferencia con respecto al check-in. Por favor, ingrese nuevamente.")

            except ValueError:
                print("Error: Ingrese valores numéricos válidos. Por favor, introduzca la fecha en números.")

        return fecha_checkout
        
    @staticmethod
    def validaciones_tipo_reserva():
        bucle = True

        while bucle:
            print("*** Seleccionar Tipo de Reserva ***")
            print("1. Reserva")
            print("2. Actividad")
            print("3. Hospedaje")
            

            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                tipo_reserva = "Reserva"
                print("El tipo de reserva seleccionado fue Reserva.")
                return tipo_reserva
            elif eleccion == "2":
                tipo_reserva = "Actividad"
                print("El tipo de reserva seleccionado fue Actividad.")
                return tipo_reserva
            elif eleccion == "3":
                tipo_reserva = "Hospedaje"
                print("El tipo de reserva seleccionado fue Hospedaje.")
                return tipo_reserva
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción válida.")
                
    @staticmethod
    def validar_id_reserva_reserva(self):
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        while True:
            numeroID = input("Ingrese el ID de la reserva de tipo 'Reserva' que quiere eliminar/modificar: ")

            # Validar que el id no sea nulo
            if numeroID is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                numeroID = int(numeroID)  # Intenta convertir el valor a un entero
                if numeroID <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue

            if not conexion.IDReservaExists(numeroID, tipo="Reserva"):
                print("Error: La reserva de tipo 'Reserva' con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            return numeroID
    
    @staticmethod
    def validar_id_reserva_hospedaje(self):
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        while True:
            numeroID = input("Ingrese el ID de la reserva de tipo 'Hospedaje' que quiere eliminar/modificar: ")

            # Validar que el id no sea nulo
            if numeroID is None:
                print("Error: Parece que no has ingresado ningún ID.")
                print("Por favor, ingrese un dato válido.")
                continue

            # Validar que el id sea un número entero mayor que 0
            try:
                numeroID = int(numeroID)  # Intenta convertir el valor a un entero
                if numeroID <= 0 :
                    print("Error: El ID debe ser un número entero mayor que 0.")
                    print("Por favor, ingrese un dato válido.")
                    continue
            except ValueError:
                print("Error: El ID debe ser un número entero mayor que 0.")
                print("Por favor, ingrese un dato válido.")
                continue

            if not conexion.IDReservaExists(numeroID, tipo="Hospedaje"):
                print("Error: La reserva de tipo 'Hospedaje' con el ID proporcionado no existe en la base de datos.")
                print("Por favor, ingrese un dato válido.")
                continue
            return numeroID
        
    @staticmethod
    def validar_campos(campo):
            if campo == "empleado_id":
                    # Aquí puedes realizar la validación para el nuevo valor del empleado_id
                    if not ValidacionesReserva.validar_id_reserva():
                        print("Error: El valor de empleado_id no es válido.")
                        return False

                    elif campo == "fecha_checkout":
                        # Aquí puedes realizar la validación para el nuevo valor de la fecha_checkout
                        if not ValidacionesReserva.validar_checkout():
                            print("Error: La fecha de checkout no es válida.")
                            return False
        