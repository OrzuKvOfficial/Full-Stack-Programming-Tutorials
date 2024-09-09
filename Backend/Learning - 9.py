def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = 10  # Fibonacci sonlarining soni
fib_numbers = fibonacci(n)
print(f"{n} ta Fibonacci sonlari: {fib_numbers}")
