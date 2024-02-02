from math import sqrt

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("x1={:.2f}, x2={:.2f}".format(x1, x2))
elif delta == 0:
    x = -b / (2 * a)
    print("x={:.2f}".format(x))
else:
    print("To równanie nie ma rozwiązań rzeczywistych")
