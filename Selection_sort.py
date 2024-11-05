def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encuentra el valor mínimo en la lista desordenada
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el valor mínimo con el primer valor desordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

# Leer números del archivo desordenado
input_file = 'numeros_medio_desordenados.txt'
numbers = read_numbers_from_file(input_file)

# Ordenar números usando selection sort
selection_sort(numbers)

# Escribir números ordenados en un nuevo archivo
output_file = 'numeros_ordenados.txt'
write_numbers_to_file(numbers, output_file)

print("Archivo ordenado creado exitosamente.")
