class Empleado:
    def __init__(self, id: int, nombre: str, apellido: str, dni: int, isAdmin: int, telefono: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.isAdmin = isAdmin
        self.telefono = telefono