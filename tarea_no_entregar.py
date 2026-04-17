#import pandas as pd
#import time

tipos_pan=[]
cantidad_pan=[]



def gen_produc():
    pass

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
        gen_produc()
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
