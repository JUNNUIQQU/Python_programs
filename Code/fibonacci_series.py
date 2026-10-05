def generate_fibonacci_series(number):
    fibonacci = []
    first = 0
    second = 1

    for i in range(number):
        fibonacci.append(first)
        first, second = second, first + second

    return fibonacci


number = 7
print(generate_fibonacci_series(number))