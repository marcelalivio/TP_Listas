# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo

lista_elementos =("Marcela", "Livio", 25, "Buenos Aires")
lista_penultima=lista_elementos[2]
print(lista_penultima)

# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia=[]
lista_vacia.append("Me gusta comer chocolate")
lista_vacia.append("Mientras miro Game of Thrones")
lista_vacia.append("Aunque no puedo comer demasiado, porque luego me duele el estomago")
print(lista_vacia)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente. Imprimir la lista resultante por pantalla. ¡
animales = ["perro", "gato", "conejo", "pez"]
animales[1]= ("loro") 
animales[3]= ("oso")
print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza: creo que lo quehace este programa es encontrar el numero mas grande de la lista y eliminarlo, tal como se muestra a continuacion:
numeros= [8, 15, 3, 22,7]
numeros.remove(max(numeros))
print(numeros)

# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por antalla los dos primeros.
lista= list(range(10,35, 5))
print(lista)
dos_primeros= lista[0:2]
print(dos_primeros)

# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores.
autos = ["sedan", "polo", "suran", "gol"]
autos[1]=("fiat")
autos[2]=("porsche")
print(autos)

# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# Agregar "jugo" a la lista del tercer cliente usando append.
# Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# Eliminar "pan" de la lista del primer cliente.
# Imprimir la lista resultante por pantalla

compras[2]
compras[2].append("jugo")

compras[1][1]="tallarines"

compras[0].remove("pan")

print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada=[15,"True",[25.5, 57.9, 30.6],"False"]
print(lista_anidada)
