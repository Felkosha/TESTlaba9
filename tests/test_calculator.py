import pytest

from app.calculator import add, subtract, multiply, divide, is_even


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize("n, expected", [(2, True), (3, False), (0, True), (-4, True)])
def test_is_even(n, expected):
    assert is_even(n) is expected
