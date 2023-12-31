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

from bgrafana_api.api.snapshots_api import SnapshotsApi  # noqa: E501


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SnapshotsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_dashboard_snapshot(self) -> None:
        """Test case for create_dashboard_snapshot

        When creating a snapshot using the API, you have to provide the full dashboard payload including the snapshot data. This endpoint is designed for the Grafana UI.  # noqa: E501
        """
        pass

    def test_delete_dashboard_snapshot(self) -> None:
        """Test case for delete_dashboard_snapshot

        Delete Snapshot by Key.  # noqa: E501
        """
        pass

    def test_delete_dashboard_snapshot_by_delete_key(self) -> None:
        """Test case for delete_dashboard_snapshot_by_delete_key

        Delete Snapshot by deleteKey.  # noqa: E501
        """
        pass

    def test_get_dashboard_snapshot(self) -> None:
        """Test case for get_dashboard_snapshot

        Get Snapshot by Key.  # noqa: E501
        """
        pass

    def test_get_sharing_options(self) -> None:
        """Test case for get_sharing_options

        Get snapshot sharing settings.  # noqa: E501
        """
        pass

    def test_search_dashboard_snapshots(self) -> None:
        """Test case for search_dashboard_snapshots

        List snapshots.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
