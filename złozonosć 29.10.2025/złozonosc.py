import time

def lin_search(lst,val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i
        lst=[1,2,3,4,5,6,7,8,9,10]
        print(lin_search(lst,9))

End=time.time()
print(end - start)
n=int(input("podaj liczbe:"))
start = time.time

suma=0
i=1
while i<=n:
   suma+=i
   i+=1
print(suma)
End=time.time()
print(end-time)