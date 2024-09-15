def encontrarElemento(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

if __name__ == '__main__':
    arr = [12, 34, 10, 6, 40]
    key = 12
    n = len(arr)

    arreglo = encontrarElemento(arr, n, key)
    if arreglo != -1:
        print("Elemento encontado en la posición: " + str(arreglo + 1))
    else:
        print("Elemento no encontrado")
