from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator."""
        # Setup an empty list of strings
        result: list[str] = []
        # Loop thorugh each item in self.items
        # is instance now needed w/ the Union to be compatable w/ the str
        if isinstance(rhs, str):
            for item in self.items:
                # For each item, append the concatention of item and rhs to result list
                result.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            # Build up the result list by concatenating
            # each item in self.items w/ corresponding item in rhs.items
        # Return a newly constructed StrArray whose items are result
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)