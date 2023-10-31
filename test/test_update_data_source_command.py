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

from bgrafana_api.models.update_data_source_command import UpdateDataSourceCommand  # noqa: E501

class TestUpdateDataSourceCommand(unittest.TestCase):
    """UpdateDataSourceCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateDataSourceCommand:
        """Test UpdateDataSourceCommand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateDataSourceCommand`
        """
        model = UpdateDataSourceCommand()  # noqa: E501
        if include_optional:
            return UpdateDataSourceCommand(
                access = '',
                basic_auth = True,
                basic_auth_user = '',
                database = '',
                is_default = True,
                json_data = bgrafana_api.models.json.Json(),
                name = '',
                secure_json_data = {
                    'key' : ''
                    },
                type = '',
                uid = '',
                url = '',
                user = '',
                version = 56,
                with_credentials = True
            )
        else:
            return UpdateDataSourceCommand(
        )
        """

    def testUpdateDataSourceCommand(self):
        """Test UpdateDataSourceCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
