def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum


if __name__ == "__main__":
    lst = [1, 2, 4, 5, 6]
    n = 6
    result = find_missing_number(lst, n)
    print(result)