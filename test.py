def my_func(a, b):
    summ = a + b
    print(f'{a} + {b} = {summ}')
    return summ, a, b


z = my_func(4, 5)
print(z)