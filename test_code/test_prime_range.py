from Code.prime_range import primes_in_range


def test_primes_in_range():
    assert primes_in_range(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_small_range():
    assert primes_in_range(2, 5) == [2, 3, 5]


def test_range_without_primes():
    assert primes_in_range(8, 10) == []


def test_single_prime_number():
    assert primes_in_range(7, 7) == [7]