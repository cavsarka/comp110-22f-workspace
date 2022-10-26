"""Tests for EX07 - Dictionary."""


from dictionary import invert
from dictionary import favorite_color
from dictionary import count

# invert test


def invert_test_edge() -> None:
    """Edge testing an empty dictionary."""
    dictionary = {}
    assert invert(dictionary) == {}


def invert_test_use_one() -> None:
    """Use testing a dictionary of languages."""
    dictionary = {"hello": "hola", "how are you": "como estas", "good morning": "buenos dias"}
    assert invert(dictionary) == {"hola": "hello", "como estas": "how are you", "buenos dias": "good morning"}


def invert_test_use_two() -> None:
    """Use testing a dictionary of basketball players."""
    dictionary = {"lebron": "james", "stephen": "curry", "lamelo": "ball", "michael": "jordan"}
    assert invert(dictionary) == {"james": "lebron", "curry": "stephen", "ball": "lamelo", "jordan": "michael"}


# favorite_color test


def favorite_color_test_edge() -> None:
    """Edge testing an empty dictionary."""
    dictionary = {}
    assert favorite_color(dictionary) == {}


def favorite_color_test_use_one() -> None:
    """Use testing a dictionary I made up."""
    dictionary = {"Joe": "Yellow", "Cam": "Yellow", "Patrick": "Green"}
    assert favorite_color(dictionary) == "Yellow"


def favorite_color_test_use_two() -> None:
    """Use testing a dictionary I made up."""
    dictionary = {"Chinmay": "Purple", "Claire": "White", "Jeff": "Pink"}
    assert favorite_color(dictionary) == "Purple"


# Count test


def count_test_edge() -> None:
    """Edge testing an empty list."""
    list = []
    assert count(list) == {}


def count_test_use_one() -> None:
    """Use testing a list I made up."""
    list = ["green", "blue", "yellow", "blue", "green", "green"]
    assert count(list) == {"green": 3, "blue": 2, "yellow": 1}


def count_test_use_two() -> None:
    """Use testing a list I made up."""
    list = ["mike", "mike", "joe", "cam"]
    assert count(list) == {"mike": 2, "joe": 1, "cam": 1}