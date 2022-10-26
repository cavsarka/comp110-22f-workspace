"""EX04 - Lists."""


__author__ = "730615401"


def all(num_list: list[int], num: int) -> bool:
    """Checks if a given int is the same as all the ints in an index."""
    i = 0
    same = True
    if len(num_list) == 0:
        same = False
    while i < len(num_list):
        if num_list[i] != num:
            same = False
            i += 1
        else:
            i += 1
    return same  


def max(num_list: list[int]) -> int:
    """Finds max value for given ints in a list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    i = 0
    greatest_num = -1000000000
    while i < len(num_list):
        if num_list[i] > greatest_num:
            greatest_num = num_list[i]
            i += 1
        else: 
            i += 1
    return greatest_num
    

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Checks if two lists are the same size and their elements are the same."""
    if len(list_one) != len(list_two):
        return False
    i = 0
    same = True
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            same = False
            i += 1
        else: 
            i += 1
    return same