x=int(input("input number in dec" ))

def dec_to_bin(x): 
    if x >= 1:
        dec_to_bin(x // 2)
    print(x % 2, end='')
dec_to_bin(x)
print()    