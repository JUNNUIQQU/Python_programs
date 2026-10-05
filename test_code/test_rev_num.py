from Code.rev_num import reverse_number


def test_reverse_number():
    assert reverse_number(12345) == 54321


def test_reverse_single_digit():
    assert reverse_number(7) == 7


def test_reverse_number_with_zero():
    assert reverse_number(1200) == 21


def test_reverse_zero():
    assert reverse_number(0) == 0