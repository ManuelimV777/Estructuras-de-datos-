def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

# Leer números del archivo desordenado
input_file = 'numeros_ordenados.txt'
numbers = read_numbers_from_file(input_file)

# Ordenar números usando insertion sort
insertion_sort(numbers)

# Escribir números ordenados en un nuevo archivo
output_file = 'numeros_ordenados2.txt'
write_numbers_to_file(numbers, output_file)

print("Archivo ordenado creado exitosamente.")
