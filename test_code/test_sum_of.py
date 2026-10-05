from Code.sum_of import sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(12345) == 15


def test_single_digit():
    assert sum_of_digits(7) == 7


def test_zero():
    assert sum_of_digits(0) == 0


def test_negative_number():
    assert sum_of_digits(-123) == 6