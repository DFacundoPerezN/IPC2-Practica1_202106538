from Nodo_Encabezado import *

class ListaDoble():
    def __init__(self):
        self.inicio=None

    def estaVacia(self):
        return self.inicio==None

    def insertar(self,dato):
        new= Nodo(dato)
        if self.inicio is None:
            print("la cola estaba vacia")
            self.inicio=new
        
        else:
            tmp=self.inicio

            while tmp.siguiente is not None:
                tmp=tmp.siguiente

            tmp.siguiente = new
            new.anterior = tmp
    
    def sacarPrimero(self): #Cola
        tmp=self.inicio

        if tmp==None:
            print("la lista esta vacia")
            return tmp

        elif tmp.siguiente == None:
            print("solo hay uno en la cola")
            self.inicio=None
            return tmp

        else:
            self.inicio=tmp.siguiente
            tmp.siguiente.anterior=None
            return tmp
            

    def sacarUltimo(self):
        tmp= self.inicio

        if tmp==None:
            print("la lista esta vacia")
            return tmp

        elif tmp.siguiente == None:
            print("solo hay uno en la cola")
            self.inicio=None
            return tmp

        else:
            while tmp.siguiente is not None:
                tmp=tmp.siguiente
            tmp.anterior.siguiente=None
            return tmp

    def cantidad(self):
        tmp = self.inicio
        cantidad=0
        while tmp is not None:
            tmp=tmp.siguiente
            print(cantidad)
            cantidad=cantidad+1
        return cantidad

'''listaPrueba= ListaDoble()
listaPrueba.insertar("Uno")
listaPrueba.insertar("Dos")
listaPrueba.insertar("Tres")
print("Cantidad: ", listaPrueba.cantidad())
nodoSalida=listaPrueba.sacarPrimero()
print(nodoSalida.dato)
nodoSalida2=listaPrueba.sacarPrimero()
print(nodoSalida2.dato)
print(listaPrueba.sacarPrimero().dato)'''

