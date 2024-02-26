lista_slow = ["jabłko", "banan", "truskawka", "gruszka", "śliwka", "malina", "winogrono"]

def dlugosc_wieksza_niz_5(slowo):
    return len(slowo) > 5

wybrane_slowa = list(filter(dlugosc_wieksza_niz_5, lista_slow))

print("Słowa o długości większej niż 5 liter:")
print(wybrane_slowa)