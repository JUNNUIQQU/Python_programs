from Code.palindrome import is_palindrome


def test_palindrome_number():
    assert is_palindrome(121) is True


def test_not_palindrome_number():
    assert is_palindrome(123) is False


def test_single_digit_number():
    assert is_palindrome(7) is True


def test_zero():
    assert is_palindrome(0) is True