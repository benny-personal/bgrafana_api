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

from bgrafana_api.api.signed_in_user_api import SignedInUserApi  # noqa: E501


class TestSignedInUserApi(unittest.TestCase):
    """SignedInUserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SignedInUserApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_change_user_password(self) -> None:
        """Test case for change_user_password

        Change Password.  # noqa: E501
        """
        pass

    def test_clear_help_flags(self) -> None:
        """Test case for clear_help_flags

        Clear user help flag.  # noqa: E501
        """
        pass

    def test_get_signed_in_user(self) -> None:
        """Test case for get_signed_in_user

        """
        pass

    def test_get_signed_in_user_org_list(self) -> None:
        """Test case for get_signed_in_user_org_list

        Organizations of the actual User.  # noqa: E501
        """
        pass

    def test_get_signed_in_user_team_list(self) -> None:
        """Test case for get_signed_in_user_team_list

        Teams that the actual User is member of.  # noqa: E501
        """
        pass

    def test_get_user_auth_tokens(self) -> None:
        """Test case for get_user_auth_tokens

        Auth tokens of the actual User.  # noqa: E501
        """
        pass

    def test_get_user_quotas(self) -> None:
        """Test case for get_user_quotas

        Fetch user quota.  # noqa: E501
        """
        pass

    def test_revoke_user_auth_token(self) -> None:
        """Test case for revoke_user_auth_token

        Revoke an auth token of the actual User.  # noqa: E501
        """
        pass

    def test_set_help_flag(self) -> None:
        """Test case for set_help_flag

        Set user help flag.  # noqa: E501
        """
        pass

    def test_star_dashboard(self) -> None:
        """Test case for star_dashboard

        Star a dashboard.  # noqa: E501
        """
        pass

    def test_star_dashboard_by_uid(self) -> None:
        """Test case for star_dashboard_by_uid

        Star a dashboard.  # noqa: E501
        """
        pass

    def test_unstar_dashboard(self) -> None:
        """Test case for unstar_dashboard

        Unstar a dashboard.  # noqa: E501
        """
        pass

    def test_unstar_dashboard_by_uid(self) -> None:
        """Test case for unstar_dashboard_by_uid

        Unstar a dashboard.  # noqa: E501
        """
        pass

    def test_update_signed_in_user(self) -> None:
        """Test case for update_signed_in_user

        Update signed in User.  # noqa: E501
        """
        pass

    def test_user_set_using_org(self) -> None:
        """Test case for user_set_using_org

        Switch user context for signed in user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
