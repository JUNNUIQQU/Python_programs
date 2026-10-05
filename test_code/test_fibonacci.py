from Code.fibonacci_series import generate_fibonacci_series


def test_fibonacci_series():
    assert generate_fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_series_one_number():
    assert generate_fibonacci_series(1) == [0]


def test_fibonacci_series_zero_numbers():
    assert generate_fibonacci_series(0) == []