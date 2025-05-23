#!/usr/bin/env python3
"""
This module has the unit tests for the utility functions
defined in the utils module.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the function access_nested_map in the utils module.
    """

    @parametertized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: dict,
            path: tuple,
            expected: object
    ) -> None:
        """Test if access_nested_map returns the correct value
           when accessing a nested dictionary using a sequence of keys.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
