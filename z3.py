def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)
    #fact = 1
    #for i in range(1, number+1):
     #   fact *= i
    #return fact


print(factorial(int(input())))
