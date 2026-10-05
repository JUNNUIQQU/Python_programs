from Code.missing_num import find_missing_number

def test_missing_middle():
    assert find_missing_number([1, 2, 4, 5], 5) == 3

def test_missing_first():
    assert find_missing_number([2, 3, 4, 5], 5) == 1

def test_missing_last():
    assert find_missing_number([1, 2, 3, 4], 5) == 5

def test_missing_in_large_list():
    assert find_missing_number([1, 2, 3, 5, 6, 7, 8, 9, 10], 10) == 4

def test_single_missing():
    assert find_missing_number([1], 2) == 2
