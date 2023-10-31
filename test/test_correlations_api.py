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

from bgrafana_api.api.correlations_api import CorrelationsApi  # noqa: E501


class TestCorrelationsApi(unittest.TestCase):
    """CorrelationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CorrelationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_correlation(self) -> None:
        """Test case for create_correlation

        Add correlation.  # noqa: E501
        """
        pass

    def test_delete_correlation(self) -> None:
        """Test case for delete_correlation

        Delete a correlation.  # noqa: E501
        """
        pass

    def test_get_correlation(self) -> None:
        """Test case for get_correlation

        Gets a correlation.  # noqa: E501
        """
        pass

    def test_get_correlations(self) -> None:
        """Test case for get_correlations

        Gets all correlations.  # noqa: E501
        """
        pass

    def test_get_correlations_by_source_uid(self) -> None:
        """Test case for get_correlations_by_source_uid

        Gets all correlations originating from the given data source.  # noqa: E501
        """
        pass

    def test_update_correlation(self) -> None:
        """Test case for update_correlation

        Updates a correlation.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
