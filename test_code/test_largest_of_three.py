from Code.largest_of_three  import find_largest_using_list

def test_find_largest_using_list_basic():
    assert find_largest_using_list(10, 20, 15) == 20

def test_find_largest_using_list_all_equal():
    assert find_largest_using_list(5, 5, 5) == 5

def test_find_largest_using_list_negative_numbers():
    assert find_largest_using_list(-3, -1, -10) == -1

def test_find_largest_using_list_mixed_signs():
    assert find_largest_using_list(-5, 0, 3) == 3

def test_find_largest_using_list_floats():
    assert find_largest_using_list(1.5, 2.7, 2.1) == 2.7