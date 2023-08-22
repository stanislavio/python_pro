import pytest

from lecture7.example1 import factorial


def add(*args):
    return sum(args)


@pytest.mark.parametrize(
    "a, b, result", [(1, 1, 2), (2, 3, 5), (4, 7, 11)]
)
def test_add(a, b, result):
    assert add(a, b) == result, "Function add must return 3"


def sum_recursive1(n):
    if n <= 1:
        return 1

    return n + sum_recursive1(n - 1)


def test_sum_recursive1():
    result = sum_recursive1(10)
    assert result == 55, 'Incorrect'


def test_factorial():
    result = factorial(10)

    result2 = factorial(-5)

    assert result == 3628800

    assert result2 == 1
