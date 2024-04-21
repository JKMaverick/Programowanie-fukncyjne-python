import functools

lista_liczb = [1, 3, 5, 6, 2]

suma = functools.reduce(lambda a, b: a + b, lista_liczb)

print(f"Suma elementów listy wynosi: {suma}")