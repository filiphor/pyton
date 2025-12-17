#czy liczba jest podziena przez 2 lub 8


with open("/Users/e-horabik/pyton-1/bin-bcd/liczby.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    number = int(line.strip())
    if number % 2 == 0:
        print(f"Liczba {number} jest podzielna przez 2.")
    else:
        print(f"Liczba {number} nie jest podzielna przez 2.")
    
    if number % 8 == 0:
        print(f"Liczba {number} jest podzielna przez 8.")
    else:
        print(f"Liczba {number} nie jest podzielna przez 8.")
