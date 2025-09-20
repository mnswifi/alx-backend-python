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

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected repos_url"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        # Patch the .org property to return the test_payload
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload

            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            # Check that the _public_repos_url returns the mocked repos_url
            self.assertEqual(result, test_payload["repos_url"])

    @patch("clients.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected repo names list"""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        expected_repo_names = ["repo1", "repo2", "repo3"]

        # Configure the mock return value
        mock_get_json.return_value = test_payload

        # Patch the _public_repos_url property to return a test URL
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=unittest.mock.PropertyMock
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/testorg/repos"

            client = GithubOrgClient("testorg")
            result = client.public_repos()

            # Check that get_json was called once with the mocked repos_url
            mock_get_json.assert_called_once_with(mock_url.return_value)
            mock_url.assert_called_once()

            # Check that public_repos returns the expected list of repo names
            self.assertEqual(result, expected_repo_names)


if __name__ == "__main__":
    unittest.main()
