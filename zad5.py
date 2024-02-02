#Hipoteza Collatza

n = int(input("Enter number: "))

while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n % 2 != 0:
            n = 3 * n + 1
        print(n)



