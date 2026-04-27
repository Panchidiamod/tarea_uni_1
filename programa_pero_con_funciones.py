import os

ARCHIVO = "tabla.txt"
while True:
    print("SISTEMA DE PLANIFICACIÓN DE PRODUCCIÓN DE PAN")
    print(" 1.Generar plan de producción",
          " 2.Ingresar cantidad de panes producidos",
          " 3.Visualizar ingreso total por tipo de pan",
          " 4.Visualizar Ingreso total por dia",
          " 5.Salir del programa",
          sep="\n")
    opcion = input("\nSeleccione su opcion: ")

    if opcion == '1' and os.path.exists(ARCHIVO) == False:
        filas = int(input())
        columnas = int(input())
    elif opcion == '2':
        print()
    elif opcion == '3':
        print()
    elif opcion == '4':
        print()
    elif opcion == '5':
        print()
        break
    else:
        print("esoja una opcion valida")
