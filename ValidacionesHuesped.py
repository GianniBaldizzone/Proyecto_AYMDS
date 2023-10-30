class ValidacionesHuesped:
    
    @staticmethod
    def validar_nombre(nombre):
        while True:
            if nombre and nombre.strip().isalpha():
                return nombre.strip()
            else:
                print("Error: El nombre no puede estar vacío y debe contener solo letras.")
                nombre = input("Por favor, ingrese el nombre nuevamente: ")

    @staticmethod
    def validar_apellido(apellido):
        while True:
            if apellido and apellido.strip().isalpha():
                return apellido.strip()
            else:
                print("Error: El apellido no puede estar vacío y debe contener solo letras.")
                apellido = input("Por favor, ingrese el apellido nuevamente: ")

    @staticmethod
    def validar_numero_pasaporte():
        while True:
            numero_pasaporte = input("Ingrese el número de pasaporte: ")
            if numero_pasaporte.isdigit() and int(numero_pasaporte) > 0:
                return int(numero_pasaporte)
            else:
                print("Error: El número de pasaporte debe ser un número entero positivo.")

    @staticmethod
    def validar_dni():
        while True:
            dni = input("Ingrese el DNI: ")
            if dni.isdigit() and 10000000 <= int(dni) <= 99999999:
                return int(dni)
            else:
                print("Error: El DNI debe ser un número entero de 8 dígitos.")
    
    @staticmethod
    def validar_nacionalidad():
        bucle = True

        while bucle:
            print("*** Seleccionar Nacionalidad ***")
            print("1. Argentina")
            print("2. Brasil")
            print("3. Chile")
            print("4. Colombia")
            print("5. México")
            print("6. Perú")
            print("7. Otro")

            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                nacionalidad = "Argentina"
                print("La nacionalidad seleccionada fue Argentina")
                return nacionalidad
            elif eleccion == "2":
                nacionalidad = "Brasil"
                print("La nacionalidad seleccionada fue Brasil")
                return nacionalidad
            elif eleccion == "3":
                nacionalidad = "Chile"
                print("La nacionalidad seleccionada fue Chile")
                return nacionalidad
            elif eleccion == "4":
                nacionalidad = "Colombia"
                print("La nacionalidad seleccionada fue Colombia")
                return nacionalidad
            elif eleccion == "5":
                nacionalidad = "México"
                print("La nacionalidad seleccionada fue México")
                return nacionalidad
            elif eleccion == "6":
                nacionalidad = "Perú"
                print("La nacionalidad seleccionada fue Perú")
                return nacionalidad
            elif eleccion == "7":
                otra_nacionalidad = input("Ingrese la nacionalidad: ")
                nacionalidad = f"Otro - {otra_nacionalidad}"
                print(f"La nacionalidad seleccionada fue {nacionalidad}")
                return nacionalidad
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción válida.")

        
    @staticmethod
    def validar_grupo_sanguineo():
        bucle = True

        while bucle:
            print("*** Seleccionar Grupo Sanguíneo ***")
            print("1. A+")
            print("2. A-")
            print("3. B+")
            print("4. B-")
            print("5. AB+")
            print("6. AB-")
            print("7. O+")
            print("8. O-")

            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                grupo_sanguineo = "A+"
                print("El grupo sanguíneo seleccionado fue A+")
                return grupo_sanguineo
            elif eleccion == "2":
                grupo_sanguineo = "A-"
                print("El grupo sanguíneo seleccionado fue A-")
                return grupo_sanguineo
            elif eleccion == "3":
                grupo_sanguineo = "B+"
                print("El grupo sanguíneo seleccionado fue B+")
                return grupo_sanguineo
            elif eleccion == "4":
                grupo_sanguineo = "B-"
                print("El grupo sanguíneo seleccionado fue B-")
                return grupo_sanguineo
            elif eleccion == "5":
                grupo_sanguineo = "AB+"
                print("El grupo sanguíneo seleccionado fue AB+")
                return grupo_sanguineo
            elif eleccion == "6":
                grupo_sanguineo = "AB-"
                print("El grupo sanguíneo seleccionado fue AB-")
                return grupo_sanguineo
            elif eleccion == "7":
                grupo_sanguineo = "O+"
                print("El grupo sanguíneo seleccionado fue O+")
                return grupo_sanguineo
            elif eleccion == "8":
                grupo_sanguineo = "O-"
                print("El grupo sanguíneo seleccionado fue O-")
                return grupo_sanguineo
            else:
                print("Error: Opción no válida. Por favor, seleccione una opción válida.")

        
    @staticmethod
    def validar_seguro_vida():
        while True:
            opcion = input("¿El huésped tiene seguro de vida? (si/no): ").strip().lower()
            if opcion == "si":
                return "si"
            elif opcion == "no":
                return "no"
            else:
                print("Error: Por favor, ingrese 'Sí' o 'No' para indicar si el huésped tiene seguro de vida.")