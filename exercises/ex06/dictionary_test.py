"""Test functions for dictionary."""

__author__ = "730403346"


from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test invert."""
    dict1: dict[str, str] = {"Kyle": "Reinheimer", "a": "b"}
    assert invert(dict1) == {"Reinheimer": "Kyle", "b": "a"}


def test_invert2() -> None:
    """Test invert."""
    dict1: dict[str, str] = {"Max": "Dimuccio", "c": "d"}
    assert invert(dict1) == {"Dimuccio": "Max", "d": "c"}


def test_invert_edge() -> None:
    """Test invert as edge case."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


def test_favorite_color() -> None:
    """Test favorite color."""
    dict_c: dict[str, str] = {"Mark": "green", "Kyle": "red", "Andy": "blue"}
    color: list[str] = [""]
    color == ["green"]
    assert favorite_color(dict_c) == "green"


def test_favorite_color2() -> None:
    """Test favorite color."""
    dict_c: dict[str, str] = {"Bill": "red", "Fred": "blue", "Stu": "blue"}
    color: list[str] = [""]
    color == ["blue"]
    assert favorite_color(dict_c) == "blue"


def test_favorite_color_edge() -> None:
    """Test favorite color as edge case."""
    dict_c: dict[str, str] = {}
    color: list[str] = [""]
    color == [""]
    assert favorite_color(dict_c) == ""


def test_count() -> None:
    """Test count."""
    random: list[str] = ["bill", "phil", "phil", "carl", "joe", "phil", "carl"]
    dict0: dict[str, int] = {"phil": 3, "carl": 2, "bill": 1, "joe": 1}
    assert count(random) == dict0


def test_count2() -> None:
    """Test count."""
    random: list[str] = ["mandy", "mandy", "mandy", "carl", "carl", "phil", "orange"]
    dict0: dict[str, int] = {"mandy": 3, "carl": 2, "phil": 1, "orange": 1}
    assert count(random) == dict0


def test_count_edge() -> None:
    """Test count as edge case."""
    random: list[str] = [""]
    dict0: dict[str, int] = {}
    assert count(random) == dict0
