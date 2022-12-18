class Nodo:
    def __init__(self,dato):
        self.dato = dato    
        self.anterior=None
        self.siguiente=None

class NodoEncabezado:
    def __init__(self,id):
        self.id:int = id
        self.anterior=None
        self.siguiente=None