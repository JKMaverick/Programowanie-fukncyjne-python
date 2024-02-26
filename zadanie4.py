import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {elapsed_time:.6f} sekund")
        return result
    return wrapper

# Przykład użycia dekoratora
@timeit
def przykladowa_funkcja():
    # Symulacja obliczeń
    for _ in range(100000000):
        pass
    print("Obliczenia zakończone")

przykladowa_funkcja()