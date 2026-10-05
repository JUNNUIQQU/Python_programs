def check_prime_number(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = 7
print(check_prime_number(number))