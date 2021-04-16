numbers = []
for i in range(0,5):
    number = int(input("Veuillez entrer un entier :"))
    numbers.append(number)

list.sort(numbers)
for number in numbers:
    print(number)