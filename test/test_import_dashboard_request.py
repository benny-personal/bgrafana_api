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

from bgrafana_api.models.import_dashboard_request import ImportDashboardRequest  # noqa: E501

class TestImportDashboardRequest(unittest.TestCase):
    """ImportDashboardRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportDashboardRequest:
        """Test ImportDashboardRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportDashboardRequest`
        """
        model = ImportDashboardRequest()  # noqa: E501
        if include_optional:
            return ImportDashboardRequest(
                dashboard = None,
                folder_id = 56,
                folder_uid = '',
                inputs = [
                    bgrafana_api.models.import_dashboard_input_definition_of_input_parameters_when_importing_a_dashboard/.ImportDashboardInput definition of input parameters when importing a dashboard.(
                        name = '', 
                        plugin_id = '', 
                        type = '', 
                        value = '', )
                    ],
                overwrite = True,
                path = '',
                plugin_id = ''
            )
        else:
            return ImportDashboardRequest(
        )
        """

    def testImportDashboardRequest(self):
        """Test ImportDashboardRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
