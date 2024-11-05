import random

# Generar una lista con números del 1 al 1,000,000
numeros = list(range(1, 1000001))

# Desordenar la lista
random.shuffle(numeros)

# Escribir los números en un archivo txt
with open('numeros_desordenados.txt', 'w') as file:
    for numero in numeros:
        file.write(f"{numero}\n")

print("Archivo creado exitosamente.")
