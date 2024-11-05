def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:   
        for number in numbers:
            file.write(f"{number}\n")

# Leer números del archivo
input_file = 'archivo_medio_desordenadso.txt'
numbers = read_numbers_from_file(input_file)

# Ordenar números usando bubble sort
bubble_sort(numbers)

# Escribir números ordenados a un nuevo archivo
output_file = 'numeros_ordenados.txt'
write_numbers_to_file(numbers, output_file)

print("Archivo ordenado creado exitosamente.")
