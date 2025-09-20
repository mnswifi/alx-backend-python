#!/usr/bin/env python3
"""Unit tests for client.GithuborgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from clients import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("clients.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected result"""
        expected_url = f"https://api.github.com/orgs/{org_name}"

        # Configure the mock return value
        mock_get_json.return_value = {"org": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        # Check that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(expected_url)

        # Check that org property returns mocked value
        self.assertEqual(result, {"org": org_name})

    if __name__ == "__main__":
        unittest.main()
