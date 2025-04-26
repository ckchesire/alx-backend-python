#!/usr/bin/env python3
"""
Module provides a function that returns the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function calculates the sum of a list of floats.

    Args:
        input_list (List[float]): list of float numbers.

    Returns:
        float: The cumulative sum of all float numbers in the list.
    """
    return sum(input_list)
