import os

#Fuciones
def generador_tabla(filas:int, columnas:int, matriz):
    # Esta funcion genera la matriz con los datos en 0
    if filas == '' or columnas == '':
        print("ERROR, Ingrese un valor para cantidad de tipos de panes y/o cantidad de dias")
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
ARCHIVO = "tabla.txt" #path al Archivo
MATRIZ = []
existe_archivo = os.path.exists(ARCHIVO)

#If para ver si exciste el archivo.txt para usar ese como matriz
if existe_archivo:
    #matriz_texto = open(ARCHIVO,"r")
    pass
else:
    archivo = open(ARCHIVO,"x")
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

    if opcion == '1' and existe_archivo:
        opcion_alerta = input("ATENCION, YA EXISTE UNA TABLA DE DATOS, desea continuar(s/N) ")

    elif opcion == '1' and (not existe_archivo):
        ca_Tipo_pan = int(input("Ingrese Número de tipos de panes: "))
        ca_dias = int(input("Ingrese Número de días de produccion: "))
        print()

        generador_tabla(ca_Tipo_pan,ca_dias,MATRIZ)

        tabla_usuario(MATRIZ)

    elif opcion == '2':
        pan_id=1
        for i in range(len(MATRIZ)):
            print("\n Tipo de pan",str(pan_id))
            pan_id += 1
            precio = int(input("Ingrese el precio de la unidad de pan$: "))
            for j in range(len(MATRIZ[i])):
                while True:
                    print("Ingrese cantidad de panes producidos en el día", str(j),":",end="")
                    cantidad = int(input())
                    if cantidad >=1000 and cantidad <=2000:
                        break
                    else:
                        print("Error, la cantidad de panes a producir por día ")
                MATRIZ[i][j] = cantidad
        tabla_usuario(MATRIZ)

        for i in MATRIZ:
            print(i)

    elif opcion == '3':
        print()
    elif opcion == '4':
        print()
    elif opcion == '5':
        print("Fin de la ejecucion")
        break
    else:
        print("ERROR: Ingrese un valor valido")
