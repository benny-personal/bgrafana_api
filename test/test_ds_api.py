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

from bgrafana_api.api.ds_api import DsApi  # noqa: E501


class TestDsApi(unittest.TestCase):
    """DsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_query_metrics_with_expressions(self) -> None:
        """Test case for query_metrics_with_expressions

        DataSource query metrics with expressions.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
