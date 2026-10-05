def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]


numbers = [10, 25, 15, 30, 20]
print(find_second_largest(numbers))
