"""EX07 - Dictionary."""

__author__ = "730615401"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, switch the keys and the values."""
    new_dict: dict[str, str] = {}
    for key in original:
        if original[key] not in new_dict:
            new_dict[original[key]] = key
        else:
            raise KeyError("Duplicate")
    return new_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Given a dictionary of person and their favorite color, return what color is most chosen."""
    color_counts = {}
    for key in names_and_colors:
        if names_and_colors[key] in color_counts:
            color_counts[names_and_colors[key]] += 1
        else:
            color_counts[names_and_colors[key]] = 1
    max_value: int = 0
    max_color: str = ""
    for key in color_counts:
        if color_counts[key] > max_value:
            max_color = key
            max_value = color_counts[key]
    return max_color


def count(given_list: list[str]) -> dict[str, int]:
    """Given a list of strings, return how many times each item in the list exists in the list."""
    item_dict = {}
    for item in given_list:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    return item_dict