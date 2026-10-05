from Code.palindrome_string import is_palindrome_string


def test_palindrome_string():
    assert is_palindrome_string("madam") is True


def test_not_palindrome_string():
    assert is_palindrome_string("hello") is False


def test_single_character():
    assert is_palindrome_string("a") is True


def test_empty_string():
    assert is_palindrome_string("") is True


def test_palindrome_with_numbers():
    assert is_palindrome_string("1221") is True