import os

#Fuciones
def generador_tabla(filas, columnas, matriz):
    # Esta funcion genera la matriz con los datos en 0
    if filas == '' or columnas == '':
        print("ERROR, Ingrese un valor para cantidad de tipos de panes y/o cantidad de dias")
        return
    filas = int(filas)
    columnas = int(columnas)
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)

def tabla_usuario(matriz):
    #Imprime la tabla de datos con la "Decoracion"
    dias=[]
    print("plan de produccion")

    print("*"*(16+len(matriz[0])*8),"\n")
    
    print(" " * 16,end="")

    for i in range(1, len(matriz[0]) + 1):
        dias.append(i)
    print(*dias,sep="\t")

    pan_id = 1
    for i in matriz:
        print("tipo de pan",str(pan_id),end="")
        print("", *i,sep="\t")
        pan_id +=1
    print("*"*(16+len(matriz[0])*8))


#Variables
nombre_archivo = "tabla.txt" #path al Archivo
matriz = []
precios = []
existe_archivo = os.path.exists(nombre_archivo)

#If para ver si exciste el archivo.txt para usar ese como matriz
if existe_archivo:
    modo = 0 #modo 0, modifica matriz, modo1, modifica precios de panes, modo 2, sale

    archivo = open(nombre_archivo,"r")
    linea = archivo.readline()

    while True:
        if modo >= 2:
            print("tabla cargada desde archivo")
            tabla_usuario(matriz)
            break

        linea = linea.strip()
        if linea == "":
            modo += 1
        else:
            contenido = linea.strip("[]").split(",")

            array = []
            for i in contenido:
                array.append(int(i))

            if modo == 0:
                matriz.append(array)
            else:
                precios = array
        linea = archivo.readline()
else:
    archivo = open(nombre_archivo,"x")
    archivo.close()


#cuerpo del programa
while True:
    print("SISTEMA DE PLANIFICACIÓN DE PRODUCCIÓN DE PAN")
    print(" 1.Generar plan de producción",
          " 2.Ingresar cantidad de panes producidos",
          " 3.Visualizar ingreso total por tipo de pan",
          " 4.Visualizar Ingreso total por dia",
          " 5.Salir del programa",
          sep="\n")
    opcion = input("\nSeleccione su opcion: ")

    if opcion == '1':
        if existe_archivo:
            print("\n\n\n")
            seguro = input("ESTA ACCION ES IRREVERSIBLE, DESEA CONTINUAR? (N/s): ")
            
            if seguro != "s" or seguro != "S":
                print("Saliendo")
                break
            else:
                matriz = []

        ca_Tipo_pan = input("Ingrese Número de tipos de panes: ")
        ca_dias = input("Ingrese Número de días de produccion: ")
        print()

        generador_tabla(ca_Tipo_pan,ca_dias,matriz)

        tabla_usuario(matriz)

    elif opcion == '2':
        pan_id=1
        for i in range(len(matriz)):
            print("\n Tipo de pan",str(pan_id))
            pan_id += 1
            precio = int(input("Ingrese el precio de la unidad de pan$: "))
            
            precios.append(precio)

            for j in range(len(matriz[i])):
                while True:
                    print("Ingrese cantidad de panes producidos en el día", str(j),":",end="")
                    cantidad = int(input())
                    if cantidad >=1000 and cantidad <=2000:
                        break
                    else:
                        print("Error, la cantidad de panes a producir por día ")
                matriz[i][j] = cantidad
        tabla_usuario(matriz)
        
        #limpia la tabla del archivo antes de guardar
        archivo = open(nombre_archivo,"w")
        archivo.write("")
        archivo.close


        archivo = open(nombre_archivo,"a")
        for i in matriz:
            print(i)
            archivo.write(str(i)+"\n")

        archivo.write("\n\n")
        archivo.write(str(precios))
        archivo.close()

    elif opcion == '3':
        if len(matriz) == 0:
            print("Error: No hay datos ingresados, Use opción 1 y 2 primero")
        else:
            print("\nIngreso total por tipo de pan:")
            print("*" * 40)
            pan_id = 1
            for i in range(len(matriz)):
                total = sum(matriz[i])  # Suma todas las cantidades de la fila
                print(f"Tipo de pan {pan_id}: {total} panes producidos en total")
                pan_id += 1
            print("*" * 40)

    elif opcion == '4':
        if len(matriz) == 0:
            print("Error: No hay datos ingresados. Use la opción 1 y 2 primero.")
        else:
            print("\nIngreso total por día:")
            print("*" * 40)
            for j in range(len(matriz[0])):  # Recorre cada columna (día)
                total_dia = 0
                for i in range(len(matriz)):  # Suma todos los tipos de pan del día
                    total_dia += matriz[i][j]
                print(f"Día {j + 1}: {total_dia}  produccion total")
            print("*" * 40)

    elif opcion == '5':
        print("Fin de la ejecucion")
        break
    else:
        print("ERROR: Ingrese un valor valido")
