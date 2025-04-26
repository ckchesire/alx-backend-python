#!/usr/bin/env python3
"""
Module provides a method that returns the sum of a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list comprising integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): list of int and float values.

    Returns:
        float: returns the total sum of all numbers in the list as a float.
    """
    return sum(mxd_lst)
