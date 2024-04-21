def liczby_parzyste():
    i = 0
    while True:
        yield i
        i += 2

generator_parzystych = liczby_parzyste()
for liczba in generator_parzystych:
    print(liczba)
