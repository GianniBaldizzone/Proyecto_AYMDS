from datetime import date

class DetalleFactura:
    def __init__(self, fecha: date, montoTotal: float, estado: str, descuento: float):
        self.fecha = fecha
        self.montoTotal = montoTotal
        self.estado = estado
        self.descuento = descuento