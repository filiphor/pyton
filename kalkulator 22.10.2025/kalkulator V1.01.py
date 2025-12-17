#i/o
dzialanie = (input("podaj operator(+,-,*,/,%,**):"))
x=float(input("podaj pierwsza liczbe:"))
y=float(input("podaj druga liczbe:"))

#obliczanie
#plus
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
    try:
        z=x/y
    except ZeroDivisionError:
        print("nie dziel przez zero")
        
    
#modulo
elif dzialanie == "%":
    try:
        z=x%y
    except ZeroDivisionError:
        print("nie dziel przez zero")
elif dzialanie =="**":
    z=x**y
else: print("zly operator")

print(z)
