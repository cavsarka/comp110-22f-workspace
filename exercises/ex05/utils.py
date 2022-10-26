"""EX05 - 'list' Utility Functions."""

__author__ = "730615401"


def only_evens(nums: list[int]) -> list:
    """Given a list of integers, returns a new list of only the even integers from the list."""
    evens_list = []
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            evens_list.append(nums[i])
        i += 1
    return evens_list


def concat(list_one: list[int], list_two: list[int]) -> list:
    """Given two lists of ints, combines the two in a new list."""
    i = 0
    n = 0
    new_list = []
    while i < len(list_one):
        new_list.append(list_one[i])
        i += 1
    while n < len(list_two):
        new_list.append(list_two[n])
        n += 1
    return new_list


def sub(list: list[int], start_index: int, end_index: int) -> list:
    """Given a list of integers and a start and end index, returns the values of the list between the indexes as a new list."""
    if start_index < 0:
        start_index = 0
    if end_index > len(list):
        end_index = len(list)
    i = start_index
    new_list = []
    while i < end_index:
        new_list.append(list[i])
        i += 1
    return new_list