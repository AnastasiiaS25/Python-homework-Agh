# Liczby doskonałe
for i in range(2,100000):
    s = 0
    for j in range (1, int( i // 2) + 1):                     #dla rewizji liczb nieparzystych,
        if i % j == 0:
            s += j                                            #suma dzielników musi wzrosnąć
    if s == i:
        print(i)



