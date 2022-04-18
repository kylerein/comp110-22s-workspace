"""Dictionary related utility functions."""

__author__ = "730403346"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    # Read that file

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Head function."""
    result: dict[str, list[str]] = {}

    first_row: list[str] = list(table.keys())
    for column in first_row:
        n_rows: list[str] = []
        i: int = 0
        while i < number_rows:
            if i < len(table[column]):
                n_rows.append(table[column][i])
            i += 1
        result[column] = n_rows

    return result


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Select function."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = table[column]
    
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat function."""
    result: dict[str, list[str]] = {}
    for column in first.keys():
        result[column] = first[column]
    for column in second.keys():
        result[column] = second[column] 
    return result


def count(given: list[str]) -> dict[str, int]:
    """Count function."""
    result: dict[str, int] = {}
    for item in given:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def average(given: list[str]) -> float:
    """Given list of values, converts data to integers and produces average."""
    result: float = 0.0
    for number in given:
        result += int(number)
    result = result / len(given)
    return result