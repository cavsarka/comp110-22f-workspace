"""Tests for EX05 - 'list' Utility Functions."""


from utils import only_evens
from utils import sub
from utils import concat

# Only Evens Tests


def test_only_evens_only_odds() -> None:
    """Edge case testing a list with no Even Numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_use_one() -> None:
    """Use case testing a list I made up."""
    xs: list[int] = [1, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(xs) == [4, 6, 8]


def test_only_evens_use_two() -> None:
    """Another use case testing a list I made up."""
    xs: list[int] = [1, 4, 12, 5, 3, 9, 10]
    assert only_evens(xs) == [4, 12, 10]


# Concat


def test_concat_use_one() -> None:
    """Use case testing numbers I made up."""
    xs: list[int] = [1, 3, 5, 7, 9]
    ys: list[int] = [2, 4, 6, 8, 10]
    assert concat(xs, ys) == [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]


def test_concat_edge() -> None:
    """Edge case testing two empty lists.""" 
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_use_two() -> None:
    """Use case testing numbers I made up."""
    xs: list[int] = [1, 4, 12, 5, 3, 9, 10]
    ys: list[int] = [3, 4, 5]
    assert concat(xs, ys) == [1, 4, 12, 5, 3, 9, 10, 3, 4, 5]


# Sub


def test_sub_edge() -> None:
    """Edge case testing a negative starting index and a ending index greater than the length of the list."""
    xs: list[int] = [3, 4, 5, 6, 5]
    start_index = -4
    end_index = 20
    assert sub(xs, start_index, end_index) == [3, 4, 5, 6, 5]


def test_sub_use_one() -> None:
    """Use case testing numbers I made up."""
    xs: list[int] = [3, 4, 5, 6, 5]
    start_index = 2
    end_index = 4
    assert sub(xs, start_index, end_index) == [5, 6]


def test_sub_use_two() -> None:
    """Use case testing numbers I made up."""
    xs: list[int] = [7, 5, 2, 4, 5, 1, 6, 1]
    start_index = 1
    end_index = 6
    assert sub(xs, start_index, end_index) == [5, 2, 4, 5, 1]