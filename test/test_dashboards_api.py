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

from bgrafana_api.api.dashboards_api import DashboardsApi  # noqa: E501


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_calculate_dashboard_diff(self) -> None:
        """Test case for calculate_dashboard_diff

        Perform diff on two dashboards.  # noqa: E501
        """
        pass

    def test_delete_dashboard_by_uid(self) -> None:
        """Test case for delete_dashboard_by_uid

        Delete dashboard by uid.  # noqa: E501
        """
        pass

    def test_get_dashboard_by_uid(self) -> None:
        """Test case for get_dashboard_by_uid

        Get dashboard by uid.  # noqa: E501
        """
        pass

    def test_get_dashboard_tags(self) -> None:
        """Test case for get_dashboard_tags

        Get all dashboards tags of an organisation.  # noqa: E501
        """
        pass

    def test_get_home_dashboard(self) -> None:
        """Test case for get_home_dashboard

        Get home dashboard.  # noqa: E501
        """
        pass

    def test_import_dashboard(self) -> None:
        """Test case for import_dashboard

        Import dashboard.  # noqa: E501
        """
        pass

    def test_post_dashboard(self) -> None:
        """Test case for post_dashboard

        Create / Update dashboard  # noqa: E501
        """
        pass

    def test_trim_dashboard(self) -> None:
        """Test case for trim_dashboard

        Trim defaults from dashboard.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()