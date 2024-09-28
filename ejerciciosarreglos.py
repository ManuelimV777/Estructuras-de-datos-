# Definimos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
print(numeros)  # Imprimimos la lista original

# Añadimos el número 11 al final de la lista
numeros[len(numeros):] = [11]
print(numeros)  # Imprimimos la lista después de añadir el número 11

# Insertamos el número 20 al inicio de la lista
numeros.insert(0, 20)
# Insertamos el número 30 al final de la lista
numeros.insert(len(numeros), 30)
# Añadimos el número 40 al final de la lista
numeros.append(40)
print(numeros)  # Imprimimos la lista después de las inserciones

# Eliminamos el primer elemento con valor 1 de la lista
numeros.remove(1)
print(numeros)  # Imprimimos la lista después de la eliminación

# Invertimos el orden de los elementos en la lista
numeros.reverse()
# Contamos cuántas veces aparece el número 11 en la lista
numeros.count(11)
print(numeros)  # Imprimimos la lista después de invertir el orden

# Limpiamos todos los elementos de la lista
numeros.clear()
print(numeros)  # Imprimimos la lista después de limpiarla

# Definimos una lista con elementos de diferentes tipos
lista = [12, True, 13, False, 14, "abc", 15]
# Imprimimos el tipo del segundo elemento de la lista
print(type(lista[1]))
