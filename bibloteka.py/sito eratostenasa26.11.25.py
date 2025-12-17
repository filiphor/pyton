def sito_eratostenesa(n):
    if n < 2:
        return []
    
    sito = [True] * (n + 1)
    sito[0] = sito[1] = False
    

    for liczba in range(2, int(n**0.5) + 1):
        if sito[liczba]:

            for wielokrotnosc in range(liczba * liczba, n + 1, liczba):
                sito[wielokrotnosc] = False

    liczby_pierwsze = [i for i, czy_pierwsza in enumerate(sito) if czy_pierwsza]
    return liczby_pierwsze
