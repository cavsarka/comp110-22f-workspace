"""Dictionary related utility functions."""

__author__ = "730615401"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for key in table:
        stored_values: list[str] = []
        if len(table[key]) < rows:
            for value in table[key]:
                stored_values.append(value)
            result[key] = stored_values
        else:
            i = 0
            while i < rows:
                stored_values.append(table[key][i])
                i += 1
            result[key] = stored_values
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Product a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for col in table:
        if col in columns:
            result[col] = table[col]
    return result


def concat(data_one: dict[str, list[str]], data_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column based tables combined."""
    result: dict[str, list[str]] = {}
    for key in data_one:
        result[key] = data_one[key]
    for key in data_two:
        if key in result:
            for value in data_two[key]:
                result[key].append(value)
        else:
            result[key] = data_two[key]
    return result


def count(data_list: list[str]) -> dict[str, int]:
    """Counts the amount of times a value appears in a list."""
    result: dict[str, int] = {}
    for item in data_list: 
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

# Define your functions below 