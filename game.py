from random import randint

target_number = randint(1, 100)
guess = 0

while guess != target_number:
    guess = int(input("Odgadnij liczbę od 1 do 100 "))
    if guess > target_number:
        print("Za dużo")
    elif guess < target_number:
        print("Za mało")
    else:
        print("Brawo")
