def fibonacci(n):
    fibonacci_sequence = [0, 1]  
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])  
    return fibonacci_sequence

n_terminos = int(input("Ingrese el numero: "))
resultado = fibonacci(n_terminos)
print("Sucesión de Fibonacci:")
for i, num in enumerate(resultado):
    print(f"{i + 1}: {num}")
