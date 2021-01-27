def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact


print(factorial(int(input())))