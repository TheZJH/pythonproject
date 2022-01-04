def test_assert_01():
    assert 1 in [2, 3, 4]


def test_assert_02():
    a = 1
    b = 2
    assert a < b


def test_assert_03():
    assert 'fizz' not in 'fizzbuzz'
