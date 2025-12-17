
a = int(input("ile chcesz liczb Fibonacciego wyświetlić? "))

x = 0
y = 1
a = 1 
while a >1:
    a = a - 1
    if x < y:
        x = x + y
        print(x)
       
    else:
        y = x + y
        print(y)
    


    