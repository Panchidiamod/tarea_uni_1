"""Integrantes Francisco Galdames, Richard Paredes
Fecha de entrega:"""

#import pandas as pd
#import time

tipos_pan=[]
cantidad_pan=[]



def gen_produc(fila, columna):
    """Funcion usada para retorna una matriz
    en base a 2 datos de entrada, Filas Y columnas"""

while True:
    print("Menu", "\n")
    print(" 1.Generar plan de produccion",
          " 2.ingresar cantidad de panes producidos",
          " 3.vizualizar ingresp total",
          " 4.Visualiza Ingreso total por dia",
          " 5.Salir del programa",
          sep="\n")
    opcion = int(input("\nSeleccione una opcion: "))

    if opcion == 1:
        columna = int(input("Cuantos dias quiere visializar en la tabla"))
        fila = int(input("Cuantas variedades de pan quiere"))
        gen_produc(fila, columna)
    elif opcion == 2:
        print("2")
    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        print("Fin de la ejecucion")
        break
    else:
        print("ERROR: ingrese un valor valido")
