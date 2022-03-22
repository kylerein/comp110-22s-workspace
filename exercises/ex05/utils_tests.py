"""Test funtions for Utils."""

__author__ = "730403326"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Tests a set of numbers to see which of them are even."""
    trial: list[int] = [1, 2, 3, 4]
    assert only_evens(trial) == [2, 4]


def test_only_evens2() -> None:
    """Tests a set of numbers to see which of them are even."""
    trial: list[int] = [5, 6, 7, 8]
    assert only_evens(trial) == [6, 8]


def test_only_evens_edge() -> None:
    """Empty list."""
    trial: list[int] = []
    assert only_evens(trial) == []


def test_sub() -> None:
    """Tests a use case."""
    trial: list[int] = [1, 2, 3, 4]
    assert sub(trial, 1, 3) == [2, 3]


def test_sub2() -> None:
    """Tests a use case."""
    trial: list[int] = [5, 6, 7, 8]
    assert sub(trial, 0, 2) == [5, 6]


def test_sub_edge() -> None:
    """Empty list."""
    trial: list[int] = []
    assert sub(trial, 0, 5) == []


def test_concat() -> None:
    """Tests a use case."""
    trial1: list[int] = [1, 2, 3]
    trial2: list[int] = [4, 5, 6]
    assert concat(trial1, trial2) == [1, 2, 3, 4, 5, 6]


def test_concat2() -> None:
    """Tests a use case."""
    trial1: list[int] = [4, 5, 6]
    trial2: list[int] = [7, 8, 9]
    assert concat(trial1, trial2) == [4, 5, 6, 7, 8, 9]


def test_concat_edge() -> None:
    """Tests an edge case."""
    trial1: list[int] = []
    trial2: list[int] = []
    assert concat(trial1, trial2) == []
