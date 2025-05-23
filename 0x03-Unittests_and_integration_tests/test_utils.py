#!/usr/bin/env python3
"""This module has the unit tests for the utility functions."""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test if access_nested_map returns the expected output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test to see if KeyError is raised when an invalid path is parsed."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(cm.exception.args[0]))


class TestGetJson(unittest.TestCase):
    """Unit tests for the get_json function."""

    @parameterized.expand([
        ("http://mysite.com", {"payload": True}),
        ("http://alxswe.com", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns payload and calls requests.get once"""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
