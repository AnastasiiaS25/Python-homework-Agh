# Zadanie 1: Współczynnik BMI

name= input("Enter your name: ")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height **2 )
if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")
else:print(f"{name} is overweight by {bmi} BMI")
