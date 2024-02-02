weight = int(input("Podaj swoją wagę w kg "))
height = float(input("Podaj swój wzorst w m "))

bmi = weight / height ** 2

print("Twoje BMI to {:.2f}".format(bmi))
# print(f"Twoje BMI to {bmi:.2f}")  # alternatywnie za powyższą linijkę; proszę zwrócić uwagę na literkę f przed otwierającym cudzysłowem
