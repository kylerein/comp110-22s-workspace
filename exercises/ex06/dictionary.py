"""Where implementation of funciton skeletons and implementations will go."""

__author__ = "730403326"


#   dict1: dict[str, str] = {"Kyle": "Reinheimer", "A": "B"}


# def main() -> None:
# test: dict = {"marc": "yellow:", "bob": "blue", "bill": "greeen"}
# invert(test)

# test2: list[str] = ["beans", "beans", "carrot", "beans"]
# count(test2)


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    result: dict[str, str] = {}
    values: list[str] = []
    for key in a:
        values.append(a[key])
    for key in a:
        if values.count(a[key]) > 1:
            raise KeyError("Cannot invert: duplicate value")
        result[a[key]] = key
    return result


def favorite_color(x: dict[str, str]) -> str:
    """Decides most popular favorite color."""
    result: str = ""
    colors: list[str] = []
    for key in x:
        colors.append(x[key])
    counts: dict[str, int] = {}
    for color in colors:
        if counts[color] == 0:
            counts[color] = 1
        counts[color] = counts[color] + 1
    return result


def count(entry: list[str]) -> dict[str, int]:
    """Count the number of occurences."""
    result: dict[str, int] = {}
    entered_vals: list[str] = []
    print("boutta start for loop")
    for word in entry:
        if entered_vals.count(word) == 0:
            result[word] = 1
            entered_vals.append(word)
        else:
            result[word] = result[word] + 1
        print(result)
    return result