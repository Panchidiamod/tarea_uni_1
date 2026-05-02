# Francisco Javier Galdames Parra 22175622-3
# Richard Fabian Paredes Gonzáles 22731495-8

nombre_archivo = "MATRIZ.txt"

matriz = []

print("MENÚ\n")
 
while True:

    #print del menu

    print("SISTEMA DE PLANIFICACIÓN DE PRODUCCIÓN DE PAN")
    print(" 1.Generar plan de producción",
          " 2.Ingresar cantidad de panes producidos",
          " 3.Visualizar ingreso total por tipo de pan",
          " 4.Visualizar Ingreso total por dia",
          " 5.Salir del programa",
          sep="\n")
    opcion = int(input("\nSeleccione su opcion: "))

    #generador de array para la tabla de produccion
    #solo se genera la tabla, no los indicadores de esta(dias y tipos)

    if opcion == 1:

        filas = int(input("Ingrese número de tipo de panes: "))
        columnas = int(input("Ingrese número de dias de produccion: "))
        print()
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(0)
            matriz.append(fila)

        #imprime matriz (DEBUG)
        #for i in matriz:
        #    print(i)

        #print("\n")

        #Tabla para el usuario
        dias = []
        print("Plan de producción")
 
        print("*"*(16+columnas*8),"\n")
        print(" " * 16, end="")
        for i in range(1, columnas +1):
            dias.append(i)
        print(*dias,sep="\t")

        pan_id = 1
        for i in matriz:
            print("tipo de pan",str(pan_id),end="")
            print("",*i, sep="\t")
            pan_id += 1

        print("*"*(16+ columnas*8),"\n")

    elif opcion == 2:
        pan_id = 1
        for i in range(len(matriz)):
            print("\n Tipo de pan",str(pan_id))
            pan_id += 1
            precio = int(input("Ingrese el precio de la unidad de pan $: "))
            for j in range(len(matriz[i])):
                while True:
                    print("Ingrese cantidad de panes producidos en el día", str(j),":",end="")
                    cantidad = int(input())
                    if cantidad >=1000 and cantidad <=2000:
                        break
                    else:
                        print("Error, la cantidad de panes a producir por día ")
                matriz[i][j] = cantidad
        for i in matriz:
            print(i)

    elif opcion == 3:
        print("3")
    elif opcion == 4:
        print("4")
    elif opcion == 5:
        print("Fin de la ejecucion")
        break
    else:
        print("ERROR: ingrese un valor valido")
