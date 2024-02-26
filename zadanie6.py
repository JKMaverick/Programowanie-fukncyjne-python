def oblicz_kwadraty(liczby):
    return list(map(lambda x: x**2, liczby))

lista_liczb = [1, 2, 3, 4, 5]

kwadraty = oblicz_kwadraty(lista_liczb)
print("Kwadraty liczb:", kwadraty)
