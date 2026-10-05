from Code.second_largest import find_second_largest


def test_second_largest():
    assert find_second_largest([10, 25, 15, 30, 20]) == 25


def test_second_largest_with_negative_numbers():
    assert find_second_largest([-10, -5, -20, -1]) == -5


def test_second_largest_with_duplicates():
    assert find_second_largest([10, 20, 20, 5]) == 10


def test_second_largest_with_two_numbers():
    assert find_second_largest([5, 10]) == 5