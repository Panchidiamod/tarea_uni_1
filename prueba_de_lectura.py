matriz = []
lista_precios = []
modo = 0
ruta = "hola.txt"

archivo = open(ruta, "r")
linea = archivo.readline()

while True:
    if modo >= 2:
        break
    linea = linea.strip()
    if linea == "":
        modo += 1
        
    else:
        linea = linea.strip('[]')
        partes = linea.split(',')
        
        numeros = []
        for parte in partes:
            numeros.append(int(parte))
            
        if modo == 0:
            matriz.append(numeros)
        else:
            lista_precios = numeros
    linea= archivo.readline()




print(matriz)
print(lista_precios)

