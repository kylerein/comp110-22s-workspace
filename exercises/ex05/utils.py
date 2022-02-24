"""Function Skeletons and Implementations."""

__author__ = "730403326"


def only_evens(entry: list[int]) -> list[int]:
    """From a list of integers, return the even integers."""
    output: list = []
    for num in entry:
        if num % 2 == 0:
            output.append(num)
    return output