def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


number = 12345
print(sum_of_digits(number))