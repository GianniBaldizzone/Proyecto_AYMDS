from bd import Conexion
from datetime import datetime
class ValidacionesReserva:
    
    @staticmethod
    def validar_checkout(fecha_checkin):
        bucle=0
        fecha_checkout=0
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
            

            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                tipo_reserva = "Reserva"
                print("El tipo de reserva seleccionado fue Reserva.")
                return tipo_reserva
            elif eleccion == "2":
                tipo_reserva = "Actividad"
                print("El tipo de reserva seleccionado fue Actividad.")
                return tipo_reserva
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción válida.")