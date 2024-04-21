def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = generate_fibonacci()

first_10_fibonacci_numbers = [next(fibonacci_generator) for _ in range(10)]

print("Pierwsze 10 liczb ciągu Fibonacciego:", first_10_fibonacci_numbers)