import random

# Crear lista de números del 1 al 100,000
numeros = list(range(1, 100001))

# Insertar un número al azar cada 20 números
for i in range(19, len(numeros), 20):
    numeros.insert(i, random.randint(1, 100000))

# Escribir los números en un archivo txt
with open('numeros_medio_desordenados.txt', 'w') as file:
    for numero in numeros:
        file.write(f"{numero}\n")

print("Archivo creado exitosamente.")
