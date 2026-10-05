from Code.common_elements import find_common_elements

def test_no_common_elements():
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []

def test_some_common_elements():
    result = find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
    assert sorted(result) == [3, 4]

def test_all_common_elements():
    result = find_common_elements([1, 2, 3], [3, 2, 1])
    assert sorted(result) == [1, 2, 3]

def test_empty_list1():
    assert find_common_elements([], [1, 2, 3]) == []

def test_empty_list2():
    assert find_common_elements([1, 2, 3], []) == []

def test_both_empty():
    assert find_common_elements([], []) == []

def test_with_duplicates():
    result = find_common_elements([1, 2, 2, 3], [2, 2, 4])
    assert result == [2]