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

from bgrafana_api.models.create_role_form import CreateRoleForm  # noqa: E501

class TestCreateRoleForm(unittest.TestCase):
    """CreateRoleForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateRoleForm:
        """Test CreateRoleForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRoleForm`
        """
        model = CreateRoleForm()  # noqa: E501
        if include_optional:
            return CreateRoleForm(
                description = '',
                display_name = '',
                var_global = True,
                group = '',
                hidden = True,
                name = '',
                permissions = [
                    bgrafana_api.models.permission_is_the_model_for_access_control_permissions/.Permission is the model for access control permissions.(
                        action = '', 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        scope = '', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                uid = '',
                version = 56
            )
        else:
            return CreateRoleForm(
        )
        """

    def testCreateRoleForm(self):
        """Test CreateRoleForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
