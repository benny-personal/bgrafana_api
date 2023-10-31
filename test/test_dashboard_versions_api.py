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

from bgrafana_api.api.dashboard_versions_api import DashboardVersionsApi  # noqa: E501


class TestDashboardVersionsApi(unittest.TestCase):
    """DashboardVersionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardVersionsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_dashboard_version_by_id(self) -> None:
        """Test case for get_dashboard_version_by_id

        Get a specific dashboard version.  # noqa: E501
        """
        pass

    def test_get_dashboard_version_by_uid(self) -> None:
        """Test case for get_dashboard_version_by_uid

        Get a specific dashboard version using UID.  # noqa: E501
        """
        pass

    def test_get_dashboard_versions_by_id(self) -> None:
        """Test case for get_dashboard_versions_by_id

        Gets all existing versions for the dashboard.  # noqa: E501
        """
        pass

    def test_get_dashboard_versions_by_uid(self) -> None:
        """Test case for get_dashboard_versions_by_uid

        Gets all existing versions for the dashboard using UID.  # noqa: E501
        """
        pass

    def test_restore_dashboard_version_by_id(self) -> None:
        """Test case for restore_dashboard_version_by_id

        Restore a dashboard to a given dashboard version.  # noqa: E501
        """
        pass

    def test_restore_dashboard_version_by_uid(self) -> None:
        """Test case for restore_dashboard_version_by_uid

        Restore a dashboard to a given dashboard version using UID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()