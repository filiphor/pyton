def silnia_iteracyjnie(n):
    wynik = 1
    for liczba in range(1, n + 1):
        wynik *= liczba
    return wynik

print(silnia_iteracyjnie(5))
