"""Test funtions for Utils."""

__author__ = "730403326"


from utils import only_evens


def test_only_evens() -> None:
    "Tests a set of numbers to see which of them are even."
    trial: list[int] = [1, 2, 3, 4]
    assert only_evens(trial) == [2, 4]


def test_only_evens2() -> None:
    "Tests a set of numbers to see which of them are even."
    trial: list[int] = [5, 6, 7, 8]
    assert only_evens(trial) == [6, 8]


def test_only_evens_edge() -> None:
    trial: list[int] = []
    assert only_evens(trial) == []


def test_sub() -> None:
    trial: 


def test_concat() -> None: