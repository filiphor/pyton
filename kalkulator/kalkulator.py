#i/o
dzialanie = (input("podaj operator(+,-,*,/,%,**):"))
x=float(input("podaj pierwsza liczbe:"))
y=float(input("podaj druga liczbe:"))

#obliczanie
#plusr
if dzialanie == "+":
    z=x+y
#minus
elif dzialanie == "-":
    z=x-y
#mnozenie
elif dzialanie == "*":
    z=x*y
#dzielenie
elif dzialanie == "/":
    if y == "0":
        print("pamietaj cholero nigdy nie dziel przez zero")
    else:
        z=x/y
#modulo
elif dzialanie == "%":
    if y == "0":
        print("pamietaj cholero nigdy nie dziel przez zero")
    else:
        z=x%y

elif dzialanie =="**":
    z=x**y
else: print("zly operator")

print(z)
