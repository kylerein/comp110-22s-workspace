"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730403346"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes Values."""
        self.values = values
 
    def __str__(self) -> str:
        """String method."""
        return f"Simpy({(self.values)})"

    def fill(self, value: float, number: int) -> None:
        """Fill method."""
        i: int = 0
        self.values = []
        while i < number:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float) -> None:
        """Arange method."""
        step: float = 1.0
        assert step != 0.0
        self.values: list[float]
        i: int = 0
        num_steps: int = int((stop - start) / step)
        while i < num_steps:
            print(start + i * step)
            self.values.append(start + i * step)
            i += 1

    def arange(self, start: float, stop: float, step: float) -> None:
        """Arange method."""
        assert step != 0.0
        self.values: list[float]
        i: int = 0
        num_steps: int = int((stop - start) / step)
        while i < num_steps:
            print(start + i * step)
            self.values.append(start + i * step)
            i += 1

    def sum(self) -> float:
        """Sum method."""
        total: float = 0.0
        i: int = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add Operator Overload."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Pow operator."""
        result: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Eq operator."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Greater than operator."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __getitem__(self, rhs: int) -> float:
        """Gets the item from index rhs."""
        return self.values[rhs]

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Does more mask stuff."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.values.append(item)
        else:
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
        return result