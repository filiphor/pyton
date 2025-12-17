def fibonacci_iteracyjnie(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    ciag = [0, 1]
    while len(ciag) < n:
        nastepna_liczba = ciag[-1] + ciag[-2]
        ciag.append(nastepna_liczba)
    return ciag

print(fibonacci_iteracyjnie(10))
