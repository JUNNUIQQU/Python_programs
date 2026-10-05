from Code.reverse_string_without_slicing import reverse_string


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"


def test_reverse_word():
    assert reverse_string("Python") == "nohtyP"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("A") == "A"


def test_string_with_spaces():
    assert reverse_string("Hello World") == "dlroW olleH"