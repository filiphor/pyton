def konwerter():
    print("1. Dziesiętny na Binarny")
    print("2. Binarny na Dziesiętny")
    wybor = input("Wybierz opcję (1 lub 2): ")

    if wybor == "1":
        liczba_dziesietna = int(input("Podaj liczbę dziesiętną: "))
        wynik_binarny = bin(liczba_dziesietna)[2:]
        print(f"Wynik binarny: {wynik_binarny}")
    
    elif wybor == "2":
        tekst_binarny = input("Podaj liczbę binarną: ")
        try:
            wynik_dziesietny = int(tekst_binarny, 2)
            print(f"Wynik dziesiętny: {wynik_dziesietny}")
        except ValueError:
            print("To nie jest poprawna liczba binarna!")
    
    else:
        print("Nieprawidłowy wybór.")

konwerter()
