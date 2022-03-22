"""Function Skeletons and Implementations."""

__author__ = "730403326"


def only_evens(entry: list[int]) -> list[int]:
    """From a list of integers, return the even integers."""
    output: list[int] = []
    for num in entry:
        if num % 2 == 0:
            output.append(num)
    return output


def sub(entry: list[int], start: int, end: int) -> list[int]:
    """From a list of ints, a start index and an end index, return the start to end -1.""" 
    output: list[int] = []
    empty_list: list[int] = []
    if list[int] == empty_list:
        return output
    if start < 0:
        start = 0
    if end > len(entry):
        end = len(entry)
    while start < end:
        output.append(entry[start])
        start += 1
    return output


def concat(entry1: list[int], entry2: list[int]) -> list[int]:
    """Concatenate two lists together."""
    output: list[int] = entry1
    for num in entry2:
        output.append(num)
    return output
    