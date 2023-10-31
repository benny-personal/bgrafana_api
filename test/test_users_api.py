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

from bgrafana_api.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UsersApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_user_by_id(self) -> None:
        """Test case for get_user_by_id

        Get user by id.  # noqa: E501
        """
        pass

    def test_get_user_by_login_or_email(self) -> None:
        """Test case for get_user_by_login_or_email

        Get user by login or email.  # noqa: E501
        """
        pass

    def test_get_user_org_list(self) -> None:
        """Test case for get_user_org_list

        Get organizations for user.  # noqa: E501
        """
        pass

    def test_get_user_teams(self) -> None:
        """Test case for get_user_teams

        Get teams for user.  # noqa: E501
        """
        pass

    def test_search_users(self) -> None:
        """Test case for search_users

        Get users.  # noqa: E501
        """
        pass

    def test_search_users_with_paging(self) -> None:
        """Test case for search_users_with_paging

        Get users with paging.  # noqa: E501
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
