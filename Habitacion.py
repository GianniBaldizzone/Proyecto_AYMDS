class Habitacion:
    def __init__(self, id: int, numero: int, piso: int, estadoDeLimpieza: str, precio: float, capacidadActual: int, capacidadMaxima: int, TipoDeHabitación: str):
        self.id = id
        self.numero = numero
        self.piso = piso
        self.estadoDeLimpieza = estadoDeLimpieza
        self.precio = precio
        self.capacidadActual = capacidadActual
        self.capacidadMaxima = capacidadMaxima
        self.TipoDeHabitación = TipoDeHabitación
