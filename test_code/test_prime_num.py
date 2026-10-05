from Code.prime_num import check_prime_number


def test_prime_number():
    assert check_prime_number(7) is True


def test_non_prime_number():
    assert check_prime_number(10) is False


def test_number_one():
    assert check_prime_number(1) is False


def test_number_two():
    assert check_prime_number(2) is True