#zliczanie liter w tekscie


tekst = input("Podaj tekst: ")
litera = input("Podaj literę do policzenia: ")

licznik = 0
for znak in tekst:
    if znak == litera:
        licznik += 1

print(f"litra  {litera} wystepuje {licznik} razy")
