from bd import Conexion
from datetime import datetime
class ValidacionesReserva:
    @staticmethod
    def validar_checkin():
        bucle=0
        fecha_checkin=0
        fecha_actual = datetime.now()
        print("Fecha checkin")
        while bucle != 1:
            
            try:
                año = int(input("Ingrese año"))
                mes = int(input("Ingrese mes"))
                dia = int(input("Ingrese dia"))
                hora = int(input("Ingrese hora"))
                minutos = int(input("Ingrese minutos"))
                fecha_checkin =  datetime(año,mes,dia, hora,minutos)
                
                if fecha_checkin.date() > fecha_actual.date():
                    bucle = 1
                    print("Fecha válida.")
                    print(fecha_checkin)
                else:
                    print("Fecha inválida. La fecha de check-in debe ser posterior a la fecha actual.")
            except ValueError:
                print("Fecha inválida.")
                print(type(fecha_checkin))
                print(fecha_checkin)
                print("Parece que has ingresado la fecha en otro formato. Por favor, introduzca la fecha en numeros.")
        return fecha_checkin
        
    
    @staticmethod
    def validar_checkout(fecha_checkin):
        bucle=0
        fecha_checkout=0
        print("Fecha checkout")
        while bucle != 1:
            
            try:
                año = int(input("Ingrese año"))
                mes = int(input("Ingrese mes"))
                dia = int(input("Ingrese dia"))
                hora = int(input("Ingrese hora"))
                minutos = int(input("Ingrese minutos"))
                fecha_checkout =  datetime(año,mes,dia, hora,minutos)
                
                if fecha_checkout.date() > fecha_checkin.date():
                    bucle = 1
                    print("Fecha válida.")
                    print(fecha_checkout)
                else:
                    print("Fecha inválida. La fecha de check-out debe ser posterior a la fecha de check-in.")
            except ValueError:
                print("Fecha inválida.")
                print(type(fecha_checkout))
                print(fecha_checkout)
                print("Parece que has ingresado la fecha en otro formato. Por favor, introduzca la fecha en numeros.")
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
    def validar_id_reserva():
        nombreBD = "househunter.db"
        conexion = Conexion(nombreBD)
        while True:
            numeroID = input("Ingrese el ID de la reserva que quiere eliminar/modificar: ")
            
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
            
            if not conexion.IDReservaExists(numeroID):
                print("Error: La reserva con el ID proporcionado no existe en la base de datos.")
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
        