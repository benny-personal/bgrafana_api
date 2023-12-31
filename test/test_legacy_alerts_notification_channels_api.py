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

from bgrafana_api.api.legacy_alerts_notification_channels_api import LegacyAlertsNotificationChannelsApi  # noqa: E501


class TestLegacyAlertsNotificationChannelsApi(unittest.TestCase):
    """LegacyAlertsNotificationChannelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LegacyAlertsNotificationChannelsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_alert_notification_channel(self) -> None:
        """Test case for create_alert_notification_channel

        Create notification channel.  # noqa: E501
        """
        pass

    def test_delete_alert_notification_channel(self) -> None:
        """Test case for delete_alert_notification_channel

        Delete alert notification by ID.  # noqa: E501
        """
        pass

    def test_delete_alert_notification_channel_by_uid(self) -> None:
        """Test case for delete_alert_notification_channel_by_uid

        Delete alert notification by UID.  # noqa: E501
        """
        pass

    def test_get_alert_notification_channel_by_id(self) -> None:
        """Test case for get_alert_notification_channel_by_id

        Get notification channel by ID.  # noqa: E501
        """
        pass

    def test_get_alert_notification_channel_by_uid(self) -> None:
        """Test case for get_alert_notification_channel_by_uid

        Get notification channel by UID.  # noqa: E501
        """
        pass

    def test_get_alert_notification_channels(self) -> None:
        """Test case for get_alert_notification_channels

        Get all notification channels.  # noqa: E501
        """
        pass

    def test_get_alert_notification_lookup(self) -> None:
        """Test case for get_alert_notification_lookup

        Get all notification channels (lookup).  # noqa: E501
        """
        pass

    def test_notification_channel_test(self) -> None:
        """Test case for notification_channel_test

        Test notification channel.  # noqa: E501
        """
        pass

    def test_update_alert_notification_channel(self) -> None:
        """Test case for update_alert_notification_channel

        Update notification channel by ID.  # noqa: E501
        """
        pass

    def test_update_alert_notification_channel_by_uid(self) -> None:
        """Test case for update_alert_notification_channel_by_uid

        Update notification channel by UID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
