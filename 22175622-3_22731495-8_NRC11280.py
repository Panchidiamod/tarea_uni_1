# Francisco Javier Galdames Parra 22175622-3
# Richard Paredes 22731495-8

matriz = []
while True:

    #print del menu

    print("#"*5,"Menu","#"*5, "\n")
    print(" 1.Generar plan de produccion",
          " 2.ingresar cantidad de panes producidos",
          " 3.vizualizar ingresp total",
          " 4.Visualiza Ingreso total por dia",
          " 5.Salir del programa",
          sep="\n")
    opcion = int(input("\nSeleccione una opcion: "))

    #generador de array para la tabla de produccion
    #solo se genera la tabla, no los indicadores de esta(dias y tipos)

    if opcion == 1:

        filas = int(input("inserte cuantos tipos de pan quiere ingresar: "))
        columnas = int(input("inserte cuantos dias quiere ver en la tabla de datos: "))

        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(0)
            matriz.append(fila)

        #imprime la tabla en modo debug (osea solo la tabla sin datos)
        for i in matriz:
            print(i)

        print("\n")

        #Tabla para el usuario
        print("Tabla de produccion")
        print("\n")

        print("Dia"," " * 11, end=" ")
        for dia in range(1, columnas +1):
            print(dia," "*5, end= " ")
        print()
        print("-" * 50)
        pan_id = 0
        for i in matriz:
            print("tipo de pan","(" + str(pan_id) + ")",end="")
            print("",*i, sep="\t")
            pan_id += 1

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
