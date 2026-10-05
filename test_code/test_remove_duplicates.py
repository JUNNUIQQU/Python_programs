from Code.remove_duplicates import remove_duplicates

def test_empty_list():
    assert remove_duplicates([]) == []

def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_with_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]

def test_all_same():
    assert remove_duplicates([5, 5, 5, 5]) == [5]

def test_strings():
    assert remove_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]

def test_mixed_types():
    assert remove_duplicates([1, "1", 1, "1"]) == [1, "1"]