#Zadanie 3: Za dużo, za mało

number = input("Odgadnij liczbę od 1 do 1000:")
import random

random_number = random.randint(0, 1000)
print(random_number)

if (int(number)) > 1000:
    print("Za duzo")
elif (int(number)) < 0:
    print("Za malo")
else:print("Super")


