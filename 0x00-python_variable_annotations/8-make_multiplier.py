#!/usr/bin/env python3
"""
Module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by a predefined multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: returns float multiplied by the multiplier.
    """
    return lambda x: x * multiplier
