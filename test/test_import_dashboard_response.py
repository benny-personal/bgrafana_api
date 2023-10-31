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
import datetime

from bgrafana_api.models.import_dashboard_response import ImportDashboardResponse  # noqa: E501

class TestImportDashboardResponse(unittest.TestCase):
    """ImportDashboardResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportDashboardResponse:
        """Test ImportDashboardResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportDashboardResponse`
        """
        model = ImportDashboardResponse()  # noqa: E501
        if include_optional:
            return ImportDashboardResponse(
                dashboard_id = 56,
                description = '',
                folder_id = 56,
                folder_uid = '',
                imported = True,
                imported_revision = 56,
                imported_uri = '',
                imported_url = '',
                path = '',
                plugin_id = '',
                removed = True,
                revision = 56,
                slug = '',
                title = '',
                uid = ''
            )
        else:
            return ImportDashboardResponse(
        )
        """

    def testImportDashboardResponse(self):
        """Test ImportDashboardResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
