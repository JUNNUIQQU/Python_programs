def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primes_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


start = 1
end = 20
print(primes_in_range(start, end))