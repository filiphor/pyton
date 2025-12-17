if 5>3:#tu wymagany jest":" w przeciwnyma razie 
    #synatax error
    print("prawda")

a=10/0#blad logiczny

try:
    x=int(input("podaj liczbe"))
    print(10/x)
except ZeroDivisionError:
    print("nie mozna dzielic przez zero")
except ValueError:
    print("to nie liczba")

lista=[1,2,3]
try:
    print(lista[5])
except IndexError:
    print("nie ma takiego elemetu w lisci")