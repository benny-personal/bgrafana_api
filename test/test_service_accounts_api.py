# coding: utf-8

"""
    Grafana HTTP API.

    The Grafana backend exposes an HTTP API, the same API is used by the frontend to do everything from saving dashboards, creating users and updating data sources.

    The version of the OpenAPI document: 0.0.1
    Contact: hello@grafana.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bgrafana_api.api.service_accounts_api import ServiceAccountsApi  # noqa: E501


class TestServiceAccountsApi(unittest.TestCase):
    """ServiceAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceAccountsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_service_account(self) -> None:
        """Test case for create_service_account

        Create service account  # noqa: E501
        """
        pass

    def test_create_token(self) -> None:
        """Test case for create_token

        CreateNewToken adds a token to a service account  # noqa: E501
        """
        pass

    def test_delete_service_account(self) -> None:
        """Test case for delete_service_account

        Delete service account  # noqa: E501
        """
        pass

    def test_delete_token(self) -> None:
        """Test case for delete_token

        DeleteToken deletes service account tokens  # noqa: E501
        """
        pass

    def test_list_tokens(self) -> None:
        """Test case for list_tokens

        Get service account tokens  # noqa: E501
        """
        pass

    def test_retrieve_service_account(self) -> None:
        """Test case for retrieve_service_account

        Get single serviceaccount by Id  # noqa: E501
        """
        pass

    def test_search_org_service_accounts_with_paging(self) -> None:
        """Test case for search_org_service_accounts_with_paging

        Search service accounts with paging  # noqa: E501
        """
        pass

    def test_update_service_account(self) -> None:
        """Test case for update_service_account

        Update service account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
