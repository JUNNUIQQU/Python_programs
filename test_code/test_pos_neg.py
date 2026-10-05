from Code.pos_neg import check_number_sign


def test_positive_number():
    assert check_number_sign(10) == "Positive"


def test_negative_number():
    assert check_number_sign(-5) == "Negative"


def test_zero():
    assert check_number_sign(0) == "Zero"