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

from bgrafana_api.models.add_data_source200_response import AddDataSource200Response  # noqa: E501

class TestAddDataSource200Response(unittest.TestCase):
    """AddDataSource200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddDataSource200Response:
        """Test AddDataSource200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddDataSource200Response`
        """
        model = AddDataSource200Response()  # noqa: E501
        if include_optional:
            return AddDataSource200Response(
                datasource = bgrafana_api.models.data_source.DataSource(
                    access = '', 
                    access_control = {
                        'key' : True
                        }, 
                    basic_auth = True, 
                    basic_auth_user = '', 
                    database = '', 
                    id = 56, 
                    is_default = True, 
                    json_data = bgrafana_api.models.json.Json(), 
                    name = '', 
                    org_id = 56, 
                    read_only = True, 
                    secure_json_fields = {
                        'key' : True
                        }, 
                    type = '', 
                    type_logo_url = '', 
                    uid = '', 
                    url = '', 
                    user = '', 
                    version = 56, 
                    with_credentials = True, ),
                id = 65,
                message = 'Data source added',
                name = 'My Data source'
            )
        else:
            return AddDataSource200Response(
                datasource = bgrafana_api.models.data_source.DataSource(
                    access = '', 
                    access_control = {
                        'key' : True
                        }, 
                    basic_auth = True, 
                    basic_auth_user = '', 
                    database = '', 
                    id = 56, 
                    is_default = True, 
                    json_data = bgrafana_api.models.json.Json(), 
                    name = '', 
                    org_id = 56, 
                    read_only = True, 
                    secure_json_fields = {
                        'key' : True
                        }, 
                    type = '', 
                    type_logo_url = '', 
                    uid = '', 
                    url = '', 
                    user = '', 
                    version = 56, 
                    with_credentials = True, ),
                id = 65,
                message = 'Data source added',
                name = 'My Data source',
        )
        """

    def testAddDataSource200Response(self):
        """Test AddDataSource200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
