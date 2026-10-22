from day11.src.utilities.util import make_sum


def test_make_sum():
    cards = ['A', 'A']

    assert make_sum(cards) == 12;   

def test_make_sum_2():
    cards = ['A', 'A', 'A']

    assert make_sum(cards) == 13;

def test_make_sum_3():
    cards = ['5', '6']

    assert make_sum(cards) == 11;   

def test_make_sum_4():
    cards = ['K', 'J', 'A']

    assert make_sum(cards) == 21;      