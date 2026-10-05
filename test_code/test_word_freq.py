from Code.word_freq import word_frequency

def test_single_word():
    assert word_frequency("hello") == {"hello": 1}

def test_two_same_words():
    assert word_frequency("hello hello") == {"hello": 2}

def test_different_words():
    result = word_frequency("hello world")
    assert result == {"hello": 1, "world": 1}

def test_mixed_frequency():
    result = word_frequency("hello world hello")
    assert result == {"hello": 2, "world": 1}

def test_empty_string():
    assert word_frequency("") == {}

def test_case_insensitive():
    result = word_frequency("Hello hello HELLO")
    assert result == {"hello": 3}