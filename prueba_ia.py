def leer_archivo(ruta):
    matriz = []
    array = []
    seccion_actual = "matriz"

    f = open(ruta, 'r')
    
    linea = f.readline()       # Lee la primera línea
    
    while linea:               # Mientras haya líneas por leer
        linea = linea.strip()
        
        if linea == "":
            seccion_actual = "array"
        else:
            linea = linea.strip('[]')
            partes = linea.split(',')
            
            numeros = []
            for parte in partes:
                numeros.append(int(parte))
            
            if seccion_actual == "matriz":
                matriz.append(numeros)
            else:
                for numero in numeros:
                    array.append(numero)
        
        linea = f.readline()   # Lee la siguiente línea
    
    f.close()

    return matriz, array

matriz_p, arra_p = leer_archivo("hola.txt")

print(matriz_p)
print(arra_p)
