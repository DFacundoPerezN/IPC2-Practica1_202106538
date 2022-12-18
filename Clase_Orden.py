class Orden:
    
    def __init__(self, postre: str, tiempo: float, nombre_cliente: str, numero_orden1=1):
        self.numero = numero_orden1
        self.tipo=self.postre=postre
        self.tiempo= tiempo
        self.nombre_cliente=nombre_cliente
    