#Zadanie 2: Równianie kwadratowe
from math import sqrt

a= float(input("a= "))
b= float(input("b= "))
c= float(input("c= "))

d = b * b -4 * a * c
if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print("x1 = %.2f: x2 = %.2f:" % (x1,x2))

elif d==0:
    x1 = -d / (2*a)
    print("x1 = %.2f:" % x1)
else:
    print("No root")
