
x=int(input("dej liczbe do rozkladania na czynniki pierwsze: "))
def czynniki_pierwsze(n):
    czynnki=[]
    dzielnik=2
    while n != 1:
        while n % dzielnik == 0:
            czynnki.append(dzielnik)
            n //= dzielnik
        dzielnik += 1
    return czynnki
print(czynniki_pierwsze(x))
