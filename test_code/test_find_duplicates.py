from Code.find_duplicates import find_duplicates
def test_no_duplicates():
    assert sorted(find_duplicates([1, 2, 3, 4])) == []

def test_one_duplicate():
    assert sorted(find_duplicates([1, 2, 2, 3])) == [2]

def test_multiple_duplicates():
    assert sorted(find_duplicates([1, 2, 2, 3, 3, 4])) == [2, 3]

def test_all_same():
    assert sorted(find_duplicates([5, 5, 5, 5])) == [5]

def test_empty_list():
    assert find_duplicates([]) == []

def test_with_strings():
    assert sorted(find_duplicates(["a", "b", "a", "c", "b"])) == ["a", "b"]