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

from bgrafana_api.api.admin_api import AdminApi  # noqa: E501


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_admin_get_settings(self) -> None:
        """Test case for admin_get_settings

        Fetch settings.  # noqa: E501
        """
        pass

    def test_admin_get_stats(self) -> None:
        """Test case for admin_get_stats

        Fetch Grafana Stats.  # noqa: E501
        """
        pass

    def test_pause_all_alerts(self) -> None:
        """Test case for pause_all_alerts

        Pause/unpause all (legacy) alerts.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
