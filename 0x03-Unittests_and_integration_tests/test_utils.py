#!/usr/bin/env python3

"""Unit tests for access_nested_map in utils.py"""
from parameterized import parameterized
import unittest 
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with valid inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Test that keyError is raised with correct message"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")

class TestGetJson(unittest.TestCase):
    """TestGetJson class to test get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns the expected payload"""
        # Configure the mock to return a response with the specified JSON data
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function with the test URL
        result = get_json(test_url)

        # Assert that the mock was called with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the function returns the expected payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """TestMemoize class to test memoize decorator"""

    def test_memoize(self):
        """Test that memoization caches the result of a method call."""

        class TestClass:
            """TestClass with a method to be memoized"""
            def a_method(self):
                """Method that returns 42"""
                return 42
            
            @memoize
            def a_property(self):
                """Memoized property that calls a_method"""
                return self.a_method()
        
        # Patch a_method to track calls
        with patch.object(TestClass, "a_method", return_value=42) as mock_a_method:
            obj = TestClass()

            # Call the memoized property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Assert that a_method was called only once
            mock_a_method.assert_called_once()

            # Assert that both calls to a_property return the same result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == "__main__":
    unittest.main()