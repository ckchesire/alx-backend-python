#!/usr/bin/env python3
"""
Module  that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): A string key.
        v (int or float): A numeric value to be squared.

    Returns:
        Tuple[str, float]: return string and the float square of the number.
    """
    return (k, float(v ** 2))
