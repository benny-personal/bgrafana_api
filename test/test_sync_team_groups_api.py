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

from bgrafana_api.api.sync_team_groups_api import SyncTeamGroupsApi  # noqa: E501


class TestSyncTeamGroupsApi(unittest.TestCase):
    """SyncTeamGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SyncTeamGroupsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_team_group_api(self) -> None:
        """Test case for add_team_group_api

        Add External Group.  # noqa: E501
        """
        pass

    def test_get_team_groups_api(self) -> None:
        """Test case for get_team_groups_api

        Get External Groups.  # noqa: E501
        """
        pass

    def test_remove_team_group_api(self) -> None:
        """Test case for remove_team_group_api

        Remove External Group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
