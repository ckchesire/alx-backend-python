#!/usr/bin/env python3
"""
Module provides a method that returns the floor value of a float.
"""
import math


def floor(n: float) -> int:
    """
    Function to return the floor of a floating point number.

    Args:
        n (float): Floating point number

    Returns:
        int: Returns the largest number less than or equal to n.
    """
    return math.floor(n)
