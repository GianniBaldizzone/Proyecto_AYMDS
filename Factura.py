from datetime import date

class Factura:
    def __init__(self, id: int, fecha_facturacion: date, estado_de_pago: str, descuento: float, monto_total: float):
        self.id = id
        self.fecha_facturacion = fecha_facturacion
        self.estado_de_pago = estado_de_pago
        self.descuento = descuento
        self.monto_total = monto_total