#!/usr/bin/env python3
""" Unit test for GithubOrgClient class."""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test for the  GithubOrgClient.org method."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns the correct payload."""
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test to check that _public_repos_url returns repos_url from org"""

        test_payload = {
                "repos_url": "https://api.github.com/orgs/testorg/repos"
                }

        with patch.object(
                GithubOrgClient,
                "org",
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            self.assertEqual(
                    result,
                    "https://api.github.com/orgs/testorg/repos")
            mock_org.assert_called_once()

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected repo names"""

        expected_payload = [
                {"name": "repo1"},
                {"name": "repo2"},
                {"name": "repo3"},
        ]
        mock_get_json.return_value = expected_payload

        with patch.object(
                GithubOrgClient,
                "_public_repos_url",
                new_callable=PropertyMock) as mock_repos_url:
            fake_url = "https://fakeurl.com/orgs/testorg/repos"
            mock_repos_url.return_value = fake_url
            client = GithubOrgClient("testorg")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(fake_url)
            mock_repos_url.assert_called_once()
