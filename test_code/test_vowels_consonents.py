from Code.vowels_consonents import count_vowels_and_consonants


def test_vowels_and_consonants():
    assert count_vowels_and_consonants("Hello World") == (3, 7)


def test_only_vowels():
    assert count_vowels_and_consonants("aeiou") == (5, 0)


def test_only_consonants():
    assert count_vowels_and_consonants("bcdfg") == (0, 5)


def test_with_numbers_and_spaces():
    assert count_vowels_and_consonants("Python 123!") == (1, 5)


def test_empty_text():
    assert count_vowels_and_consonants("") == (0, 0)
