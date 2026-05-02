import os 

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
lista = [87,545,6543,786]

archivo_f = "hola.txt"

if os.path.exists(archivo_f):
    print("archivo existe")
else:
    print("generando archivo")
    archivo = open(archivo_f,"x")
    archivo.close()

archivo = open(archivo_f,"a")

for i in matriz:
    print(i)
    archivo.write(str(i)+ "\n")


archivo.write("\n" + str(lista)+" ")
archivo.close()
print("archivo guardado")
