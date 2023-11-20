from functools import reduce
from typing import Callable


def each2d(test: Callable, matrix: list[list]):
    return all(False for element in matrix for arg in element if not test(arg))


# generators
def some2d(test: Callable, matrix: list[list]):
    return any(True for element in matrix for arg in element if test(arg))


# generators
def sum2d(test: Callable, matrix: list[list]):
    return sum(arg for element in matrix for arg in element if test(arg))


# generators
def my_map(f, xs):
    return reduce(lambda x, y: x + [f(y)], xs, [])


# generators
def my_filter(f, xs):
    return reduce(lambda x, y: x + [y] if f(y) else x, xs, [])


# generators
def replicate_each(n, xs):
    return reduce(lambda x, y: x + [y] * n, xs, [])


def non_empty_truths(elements: list) -> list:
    clear_list = [
        elem
        for elem in [
            [arg for arg in element if bool(arg) is True] for element in elements
        ]
        if bool(elem) is True
    ]
    return clear_list
