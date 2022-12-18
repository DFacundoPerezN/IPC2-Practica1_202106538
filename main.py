import sys
from Clase_Orden import *
from Lista_Doble import *
import os

colaOrdenes = ListaDoble()

def tiempoTotal():
    tiempo_total=0
    if colaOrdenes.inicio is not None:
        tmp=colaOrdenes.inicio
        while tmp is not None:
            tiempo_total = tiempo_total + tmp.dato.tiempo
            tmp=tmp.siguiente
    else: 
        print("No hay ordenes en la cola")    
    return tiempo_total 

def mostrarInfo():
    print('-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-')
    print('Nombre: Diego Facundo Pérez Nicolau')
    print('Carnet: 202106538')
    print('Correo: dfacundoperezn@gmail.com')
    print('Instagram: @faxx_d.avenidas')
    print('-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-♦-')

def crearOrden():
    print("- 1 \" 6 Galletas con cobertura (tiempo: 1h)\" ")
    print("- 2 \" Rosca Danesa (tiempo: 2h)\" ")
    print("- 3 \" Pastel de Frutas (tiempo: 2.5h)\" ")
    print("- 4 \" Galletas de Jengibre (tiempo: 30min = 0.5h)\" ")
    print("- 5 \" Cupcakes Navideños (tiempo: 1.5h)\" ")
    print(" - cualquier otra opcion devuelve al menu")
    opcion=input("  >>")

    match opcion:
        case '1':
            postre="6 Galletas con cobertura"
            tiempo=1.0
        case '2':
            postre="    Rosca Danesa        "
            tiempo=2.0
        case '3':
            postre="    Pastel de Frutas    "
            tiempo=2.5
        case '4':
            postre="  Galletas de Jengibre  "
            tiempo=0.5
        case '5':
            postre="   Cupcakes Navideños   "
            tiempo=1.5
        case _:
           menuInicio()

    nombre=input("Ingresa tu nombre >>")
    numero= 1+colaOrdenes.cantidad()
    nuevaOrden=Orden( postre, tiempo, nombre, numero)
    colaOrdenes.insertar(nuevaOrden)

def imprimirCola():
    if colaOrdenes.inicio is None:
        print("La cola de espera esta vacia")

    else:
        tmp=colaOrdenes.inicio

        print("+-----------------------------------------------------------+")
        print("No. |            Pedido         |Tiempo| Nombre del Cliente")
        while tmp != None:
            orden=tmp.dato
            print("+-----------------------------------------------------------+")
            print("|",orden.numero ,"|", orden.postre,"| ",orden.tiempo, " |", orden.nombre_cliente)
            tmp=tmp.siguiente
        print("+-----------------------------------------------------------+")
        print("El tiempo total de espera es de: ", tiempoTotal(), "horas")

def menuInicio():
    print("\n ")
    print("♥♥♥ Bienvenido a la Aplicacion de ordenes ♥♥♥")
    print("Opciones: \n- 1 para ver la cola de ordenes")
    print("- 2 para Ingresar una orden a la cola")    
    print("- 3 para sacar la primera orden de la cola")
    print("- 4 para mostrar informacion del desarrollador")
    print("- cualquier otra opcion para salir ")

    opcion=input('Seleccione una opcion >> ')

    match opcion:
        case '1':           #Mostrar tabal de la cola actual
            print("\n Cola actual: ")
            imprimirCola()

            menuInicio()
        case '2':           #introducir una orden a la cola
            print("\n Elige una opcion: ")
            
            crearOrden()
            crearGrafica()

            menuInicio()
        case '3':           #sacar primera orden de la cola
            print('\n')
            orden_sacada=colaOrdenes.sacarPrimero().dato

            print("La orden ", orden_sacada.numero, " de ",orden_sacada.postre, " pedida por ",orden_sacada.nombre_cliente ," esta lista y se sacó de la cola.")
            crearGrafica()

            menuInicio()
        case '4':           #Mostrar informacion del desarrollador
            mostrarInfo()
        
            menuInicio()
        case _:
            print("\nAdios")
            sys.exit()

def textoGrafica():
    aux=colaOrdenes.inicio
    n=0
    text= "\n digraph M{ \n \n"
    text+= " subgraph cluster_0 { \n "
    text+="\t style=filled; \n"
    text+="\t color=palegreen2; \n"
    text+= "\t label = \"Cola de Ordenes\";\n"
    text+= "\t node [style=filled,color=tomato];\n\t"

    while aux is not None:
        orden=aux.dato
        text+= "\t Orden"+str(orden.numero)
        text+= "[label=\" #"+ str(orden.numero)+"\\n Postre: "+ orden.postre+ "\\n Cliente: "+ orden.nombre_cliente+"\"]\n "
        n=orden.numero
        aux=aux.siguiente
    text+=" \tentrada ->"
    while n !=0:
        text+= "Orden"+str(n) +" -> "
        n=n-1

    text+= "salida \n"
    text+= "\t } \n"
    text+="}"

    return text

def crearGrafica():
    try:
        file= open('Graficas_Ordenes/ReporteGrafica.txt', 'w')
    except:
        os.mkdir('Graficas_Ordenes')
    
    contenido=textoGrafica()
    file.write(contenido)
    file.close()
    os.system("dot -Tpng Graficas_Ordenes/ReporteGrafica.txt -o Graficas_Ordenes/ReporteGrafica.png")
    os.system("dot -Tpdf Graficas_Ordenes/ReporteGrafica.txt -o Graficas_Ordenes/ReporteGrafica.pdf")


menuInicio()