def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial


number = 5
print(calculate_factorial(number))