def multiply(*args):
    sum_of_multiply = 1

    for num in args:
        sum_of_multiply *= num

    return sum_of_multiply


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
