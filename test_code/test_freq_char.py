from Code.freq_char import count_character_frequency


def test_character_frequency():
    assert count_character_frequency("hello") == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1
    }


def test_repeated_characters():
    assert count_character_frequency("aaa") == {
        "a": 3
    }


def test_empty_string():
    assert count_character_frequency("") == {}


def test_string_with_spaces():
    assert count_character_frequency("a b") == {
        "a": 1,
        " ": 1,
        "b": 1
    }