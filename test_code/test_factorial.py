from Code.factorial import calculate_factorial


def test_factorial_of_five():
    assert calculate_factorial(5) == 120


def test_factorial_of_zero():
    assert calculate_factorial(0) == 1


def test_factorial_of_one():
    assert calculate_factorial(1) == 1