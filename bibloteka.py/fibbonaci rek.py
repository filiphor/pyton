def liczba_fibonacciego(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return liczba_fibonacciego(n - 1) + liczba_fibonacciego(n - 2)

def fibonacci_rekurencyjnie(n):
    wynik = []
    for i in range(n):
        wynik.append(liczba_fibonacciego(i))
    return wynik

print(fibonacci_rekurencyjnie(10))
