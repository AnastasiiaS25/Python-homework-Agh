#Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od 1000.

for b in range (1,1001):
    k = b-1
    suma1 = 0
    while k > 0:
        if b % k == 0:
            suma1 += k
        k -= 1
    for a in range(b,1000):
        p = a - 1
        suma2 = 0
        while p > 0:
            if a % p == 0:
                suma2 += p
            p -= 1
        if suma1==a and suma2 == b and a != b:
            print("Znalazłam parę liczb zaprzyjaźnionych:", a,b)
