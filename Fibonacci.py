def nums(n):
    # Caso base: si n es 0, el número de Fibonacci es 0
    if n == 0:
        return 0
    # Caso base: si n es 1, el número de Fibonacci es 1
    elif n == 1:
        return 1
    else:
        # Llamada recursiva para calcular el número de Fibonacci
        return nums(n-1) + nums(n-2)

def main():
    try:
        # Solicitar al usuario que ingrese un número
        n = int(input("Ingrese un número para calcular el enésimo número de Fibonacci: "))
        if n < 0:
            print("Ingrese un número entero no negativo.")
        else:
            # Calcular y mostrar el enésimo número de Fibonacci
            print(f"El enésimo número de Fibonacci del número: {n} es: {nums(n)}.")
    except ValueError:
        print("Ingrese un número entero válido.")

if __name__ == "__main__":
    main()