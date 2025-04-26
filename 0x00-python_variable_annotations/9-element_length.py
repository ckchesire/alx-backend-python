#!/usr/bin/env python3
"""
Module provides a function that returns the length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence
        types (like str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: Each tuple contains the
        original item and its length.
    """
    return [(i, len(i)) for i in lst]
