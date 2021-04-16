def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)




n = int(input("Enter an integer :"))
print(fact(n))