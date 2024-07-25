def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("enter the number:"))
fib_series = [fibonacci(i) for i in range(num_terms)]
print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
