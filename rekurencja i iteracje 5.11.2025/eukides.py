x=int(input("Podaj pierwszą liczbę: "))
y=int(input("Podaj drugą liczbę: "))
if x<y:
    while x<y:
        x=x-y
else:
    while y<x:
        y=y-x
print("NWD to:",x)
