def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Ejemplo de uso:
n = 10
print(f"El enesimo número de Fibonacci (método iterativo) de {n} es: {fibonacci_iterative(n)}")