import pytest


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_failling():
    assert (1, 3, 4) == (1, 3, 5)
